import type { FileChange } from "./git.ts";
import type { ActivityRule, GuildId, QuestConfig } from "./config.ts";

export interface ActivityScores {
  mergeMage: number;
  lorekeeper: number;
  verminHunter: number;
  architect: number;
  moduleSmith: number;
}

const ACTIVITY_GUILD_IDS: GuildId[] = ["mergeMage", "lorekeeper", "verminHunter", "architect", "moduleSmith"];

export interface GuildCatalogEntry {
  id: GuildId;
  name: string;
  icon: string;
  kind: "activity" | "role" | "temporal";
}

export const GUILD_CATALOG: GuildCatalogEntry[] = [
  { id: "mergeMage", name: "Merge Mage Guild", icon: "\u{1F9D9}", kind: "activity" },
  { id: "lorekeeper", name: "Lorekeepers' Circle", icon: "\u{1F4D6}", kind: "activity" },
  { id: "verminHunter", name: "Vermin Hunters' Guild", icon: "\u{1FAB2}", kind: "activity" },
  { id: "architect", name: "Architects of New Realms", icon: "\u{1F3D7}️", kind: "activity" },
  { id: "moduleSmith", name: "Module Smiths' Guild", icon: "\u{1F9E9}", kind: "activity" },
  { id: "maintainer", name: "Maintainers' Council", icon: "\u{1F451}", kind: "role" },
  { id: "collaborator", name: "Collaborators' Guild", icon: "\u{1F91D}", kind: "role" },
  { id: "newAdventurer", name: "New Adventurers' Guild", icon: "\u{1F331}", kind: "temporal" },
];

export function emptyScores(): ActivityScores {
  return { mergeMage: 0, lorekeeper: 0, verminHunter: 0, architect: 0, moduleSmith: 0 };
}

export function matchesActivity(file: FileChange, rule: ActivityRule): boolean {
  if (rule.extensions?.includes(file.extension)) return true;
  const lowerPath = file.path.toLowerCase();
  return (rule.pathPatterns ?? []).some((pattern) => lowerPath.includes(pattern.toLowerCase()));
}

/** Scores a single changed file into exactly one activity bucket (doc > test > general). */
export function scoreFile(file: FileChange, config: QuestConfig, scores: ActivityScores): void {
  const changed = file.additions + file.deletions;
  if (matchesActivity(file, config.guilds.activity.lorekeeper)) {
    scores.lorekeeper += changed;
  } else if (matchesActivity(file, config.guilds.activity.verminHunter)) {
    scores.verminHunter += changed;
  } else {
    scores.mergeMage += changed;
  }
}

export function isFeatureCommit(message: string, config: QuestConfig): boolean {
  const prefixes = config.guilds.activity.architect.commitMessagePrefixes ?? [];
  const msg = message.trim().toLowerCase();
  return prefixes.some((prefix) => msg.startsWith(prefix.toLowerCase()));
}

function topLevelDir(filePath: string): string | null {
  const idx = filePath.indexOf("/");
  return idx === -1 ? null : filePath.slice(0, idx);
}

/**
 * Global (repo-wide, not per-author) heuristic: a commit "adds a new module" if it touches a
 * top-level directory never seen before in the project's history. Mutates `knownDirs`.
 */
export function isNewModuleCommit(files: FileChange[], knownDirs: Set<string>): boolean {
  let isNew = false;
  for (const file of files) {
    const dir = topLevelDir(file.path);
    if (dir && !knownDirs.has(dir)) {
      knownDirs.add(dir);
      isNew = true;
    }
  }
  return isNew;
}

/** The activity guild this contributor scores highest in, restricted to enabled guilds. */
export function primaryGuild(scores: ActivityScores, enabled: GuildId[]): GuildId {
  let best: GuildId = enabled.includes("mergeMage") ? "mergeMage" : ACTIVITY_GUILD_IDS[0];
  let bestScore = scores[best as keyof ActivityScores] ?? 0;
  for (const id of ACTIVITY_GUILD_IDS) {
    if (!enabled.includes(id)) continue;
    const score = scores[id as keyof ActivityScores];
    if (score > bestScore) {
      bestScore = score;
      best = id;
    }
  }
  return best;
}

/** All activity guilds this contributor has any (enabled) score in. */
export function activityMemberships(scores: ActivityScores, enabled: GuildId[]): GuildId[] {
  return ACTIVITY_GUILD_IDS.filter((id) => enabled.includes(id) && scores[id as keyof ActivityScores] > 0);
}

/**
 * The top scorer(s) per activity guild, repo-wide — "who to tag" if you have a question about
 * that area. Ties (rare) all get the crown rather than picking one arbitrarily; guilds nobody
 * has touched (score 0 for everyone) have no champion.
 */
export function computeGuildChampions(
  entries: Array<{ key: string; scores: ActivityScores }>,
  enabled: GuildId[]
): Map<GuildId, Set<string>> {
  const champions = new Map<GuildId, Set<string>>();
  for (const id of ACTIVITY_GUILD_IDS) {
    if (!enabled.includes(id)) continue;
    let best = 0;
    let holders = new Set<string>();
    for (const entry of entries) {
      const score = entry.scores[id as keyof ActivityScores];
      if (score <= 0) continue;
      if (score > best) {
        best = score;
        holders = new Set([entry.key]);
      } else if (score === best) {
        holders.add(entry.key);
      }
    }
    if (holders.size > 0) champions.set(id, holders);
  }
  return champions;
}
