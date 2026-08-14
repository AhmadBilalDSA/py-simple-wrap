import path from "node:path";
import { mkdirSync, writeFileSync } from "node:fs";
import { getCommits, type Commit } from "./lib/git.ts";
import { loadConfig, deriveTitle, levelTitleFor, resolveIdentity } from "./lib/config.ts";
import type { GuildId } from "./lib/config.ts";
import { xpForCommit, levelProgress } from "./lib/xp.ts";
import {
  emptyScores,
  scoreFile,
  isFeatureCommit,
  isNewModuleCommit,
  primaryGuild,
  activityMemberships,
  computeGuildChampions,
  GUILD_CATALOG,
  type ActivityScores,
} from "./lib/guilds.ts";
import { evaluateCommitBadges, AUTO_BADGE_META, loadManualBadges, type EarnedBadge, type AutoBadgeId } from "./lib/badges.ts";
import { parseCommitMarkers } from "./lib/commitMarkers.ts";
import { fetchCollaborators, fetchLoginForEmail } from "./lib/collaborators.ts";
import {
  fetchAllIssues,
  buildQuestBoard,
  explorePathsFor,
  issueRefsClosedBy,
  findClosedByAuthor,
  findSuitedOpenIssues,
  findGuildQuest,
} from "./lib/issues.ts";
import { getRepoInfo } from "./lib/repo.ts";

const cwd = process.cwd();
const configPath = process.env.QUEST_CONFIG ?? path.join(cwd, "quest.config.json");
const outPath = process.env.QUEST_OUT ?? path.join(cwd, "site-build", "data", "state.json");
const manualBadgesPath = process.env.QUEST_MANUAL_BADGES ?? path.join(cwd, "manual-badges.json");
const token = process.env.GITHUB_TOKEN ?? process.env.GH_TOKEN;

const config = loadConfig(configPath);
const repo = getRepoInfo(cwd);
const commits = getCommits(cwd).sort((a, b) => a.date.getTime() - b.date.getTime());

interface AuthorAccum {
  name: string;
  email: string;
  xp: number;
  commitCount: number;
  firstCommitAt: Date;
  lastCommitAt: Date;
  scores: ActivityScores;
  badgeEarnedAt: Map<AutoBadgeId, string>;
  closedIssueRefs: Set<number>;
}

const byAuthor = new Map<string, AuthorAccum>();
const knownTopLevelDirs = new Set<string>();
const fileLastModified = new Map<string, Date>();

function accumFor(commit: Commit): AuthorAccum {
  const identity = resolveIdentity(commit.authorName, commit.authorEmail, config);
  let accum = byAuthor.get(identity.key);
  if (!accum) {
    accum = {
      name: identity.name,
      email: identity.email,
      xp: 0,
      commitCount: 0,
      firstCommitAt: commit.date,
      lastCommitAt: commit.date,
      scores: emptyScores(),
      badgeEarnedAt: new Map(),
      closedIssueRefs: new Set(),
    };
    byAuthor.set(identity.key, accum);
  }
  return accum;
}

for (const commit of commits) {
  const markers = parseCommitMarkers(commit.message);
  if (markers.excluded) continue; // "[x] Don't include this commit..." — skip entirely, no accum touched

  const accum = accumFor(commit);
  const changed = commit.files.reduce((sum, f) => sum + f.additions + f.deletions, 0);

  accum.commitCount += 1;
  accum.xp += xpForCommit(config, changed);
  if (commit.date < accum.firstCommitAt) accum.firstCommitAt = commit.date;
  if (commit.date > accum.lastCommitAt) accum.lastCommitAt = commit.date;

  for (const file of commit.files) {
    scoreFile(file, config, accum.scores);
  }
  if (isFeatureCommit(commit.message, config) || markers.feature) accum.scores.architect += changed;
  if (isNewModuleCommit(commit.files, knownTopLevelDirs) || markers.module) accum.scores.moduleSmith += changed;
  if (markers.docs) accum.scores.lorekeeper += changed;

  const earnedIds = evaluateCommitBadges(commit, config, fileLastModified, markers);
  for (const id of earnedIds) {
    if (!accum.badgeEarnedAt.has(id)) accum.badgeEarnedAt.set(id, commit.date.toISOString());
  }

  for (const ref of issueRefsClosedBy(commit.message)) accum.closedIssueRefs.add(ref);
}

// Role guilds (Maintainer/Collaborator) need the GitHub collaborators API.
const roleGuildsEnabled = config.guilds.enabled.includes("maintainer") || config.guilds.enabled.includes("collaborator");
const collaborators =
  roleGuildsEnabled && repo.owner && repo.name ? await fetchCollaborators(repo.owner, repo.name, token) : null;

const loginByEmail = new Map<string, string | null>();
if (collaborators && collaborators.length > 0 && repo.owner && repo.name) {
  const entries = [...byAuthor.values()];
  const logins = await Promise.all(
    entries.map((accum) => (accum.email ? fetchLoginForEmail(repo.owner!, repo.name!, accum.email, token) : Promise.resolve(null)))
  );
  entries.forEach((accum, i) => loginByEmail.set(accum.email, logins[i]));
}

const manualBadges = loadManualBadges(manualBadgesPath);
const now = Date.now();

const issuesResult = repo.owner && repo.name ? await fetchAllIssues(repo.owner, repo.name, token) : null;
const explorePaths = explorePathsFor(cwd, repo.repoUrl, repo.branch);
const quests = buildQuestBoard(issuesResult?.open ?? null, config, explorePaths);

const guildChampions = computeGuildChampions(
  [...byAuthor.entries()].map(([key, accum]) => ({ key, scores: accum.scores })),
  config.guilds.enabled
);

const contributors = [...byAuthor.entries()]
  .map(([key, accum]) => {
    const { level, progress } = levelProgress(config, accum.xp);
    const levelTitle = levelTitleFor(config, level);

    const primary = primaryGuild(accum.scores, config.guilds.enabled);
    const guilds = new Set<GuildId>(activityMemberships(accum.scores, config.guilds.enabled));
    guilds.add(primary);

    if (config.guilds.enabled.includes("newAdventurer")) {
      const daysSinceFirst = (now - accum.firstCommitAt.getTime()) / 86_400_000;
      if (daysSinceFirst <= config.guilds.newAdventurerWindowDays) guilds.add("newAdventurer");
    }

    const login = loginByEmail.get(accum.email) ?? null;
    if (login && collaborators) {
      const match = collaborators.find((c) => c.login.toLowerCase() === login.toLowerCase());
      if (match) {
        if (match.isAdmin && config.guilds.enabled.includes("maintainer")) guilds.add("maintainer");
        else if (!match.isAdmin && config.guilds.enabled.includes("collaborator")) guilds.add("collaborator");
      }
    }

    const autoBadges: EarnedBadge[] = [...accum.badgeEarnedAt.entries()].map(([id, earnedAt]) => ({
      ...AUTO_BADGE_META[id],
      earnedAt,
      manual: false,
    }));
    const manualEarned: EarnedBadge[] = manualBadges.awards
      .filter((award) => award.contributorEmail.toLowerCase() === accum.email.toLowerCase())
      .flatMap((award) => {
        const def = manualBadges.definitions[award.badgeId];
        if (!def) return [];
        return [{ id: award.badgeId, label: def.label, icon: def.icon, flavor: def.flavor, earnedAt: award.awardedAt, manual: true }];
      });
    const badges = [...autoBadges, ...manualEarned];
    const recentBadges = [...badges].sort((a, b) => b.earnedAt.localeCompare(a.earnedAt)).slice(0, 3);

    const closedIssues = issuesResult ? findClosedByAuthor(issuesResult.closed, accum.closedIssueRefs).slice(0, 3) : [];
    const suitedIssues = issuesResult
      ? findSuitedOpenIssues(issuesResult.open, new Set(closedIssues.map((i) => i.number)), primary, 3 - closedIssues.length)
      : [];
    const relatedIssues = [...closedIssues, ...suitedIssues];

    const championOf = [...guildChampions.entries()]
      .filter(([, holders]) => holders.has(key))
      .map(([guildId]) => guildId);

    return {
      name: accum.name,
      email: accum.email,
      xp: Math.round(accum.xp),
      level,
      levelTitle,
      levelProgress: Math.max(0, Math.min(1, progress)),
      commitCount: accum.commitCount,
      firstCommit: accum.firstCommitAt.toISOString(),
      lastCommit: accum.lastCommitAt.toISOString(),
      primaryGuild: primary,
      guilds: [...guilds],
      badges,
      recentBadges,
      relatedIssues,
      championOf,
    };
  })
  .sort((a, b) => b.xp - a.xp)
  .map((contributor, index) => ({ rank: index + 1, ...contributor }));

const scoresByEmail = new Map<string, ActivityScores>();
for (const accum of byAuthor.values()) scoresByEmail.set(accum.email, accum.scores);

const guilds = GUILD_CATALOG.filter((g) => config.guilds.enabled.includes(g.id)).map((guild) => {
  const isActivity = guild.kind === "activity";
  const scoreFor = (email: string) => (isActivity ? scoresByEmail.get(email)?.[guild.id as keyof ActivityScores] ?? 0 : 0);

  const topMembers = contributors
    .filter((c) => (isActivity ? scoreFor(c.email) > 0 : c.guilds.includes(guild.id)))
    .sort((a, b) => (isActivity ? scoreFor(b.email) - scoreFor(a.email) : b.xp - a.xp))
    .slice(0, 5)
    .map((c) => ({ name: c.name, email: c.email, rank: c.rank }));

  const questIssue = issuesResult ? findGuildQuest(issuesResult.open, guild.id) : null;

  return { ...guild, topMembers, questIssue };
});

const state = {
  meta: {
    title: deriveTitle(config, repo.name ?? undefined),
    generatedAt: new Date().toISOString(),
    accent: config.theme.accent,
    repoUrl: repo.repoUrl,
  },
  guildCatalog: GUILD_CATALOG.filter((g) => config.guilds.enabled.includes(g.id)),
  guilds,
  quests,
  contributors,
};

mkdirSync(path.dirname(outPath), { recursive: true });
writeFileSync(outPath, JSON.stringify(state, null, 2));
console.log(`Contributor Quest: wrote ${contributors.length} contributor(s) to ${outPath}`);
