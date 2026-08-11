import { existsSync, readFileSync } from "node:fs";
import type { Commit } from "./git.ts";
import type { QuestConfig } from "./config.ts";
import { isFeatureCommit, matchesActivity } from "./guilds.ts";

export type AutoBadgeId =
  | "midnightCommitter"
  | "keeperOfReadme"
  | "typoPaladin"
  | "wardenOfTests"
  | "architectOfRealms"
  | "refactorerOfRuins";

export interface BadgeMeta {
  id: string;
  label: string;
  icon: string;
  flavor: string;
}

export const AUTO_BADGE_META: Record<AutoBadgeId, BadgeMeta> = {
  midnightCommitter: {
    id: "midnightCommitter",
    label: "Midnight Committer",
    icon: "\u{1F319}",
    flavor: "Pushed a commit between midnight and 4am. The muse does not keep business hours.",
  },
  keeperOfReadme: {
    id: "keeperOfReadme",
    label: "Keeper of the Sacred README",
    icon: "\u{1F4DC}",
    flavor: "Improved documentation that future travelers will bless your name for.",
  },
  typoPaladin: {
    id: "typoPaladin",
    label: "The Typo Paladin",
    icon: "⚔️",
    flavor: "Fixed a typo. Small deed, righteous cause.",
  },
  wardenOfTests: {
    id: "wardenOfTests",
    label: "Warden of the Test Suite",
    icon: "\u{1F6E1}️",
    flavor: "Added tests that actually catch something. The realm is safer for it.",
  },
  architectOfRealms: {
    id: "architectOfRealms",
    label: "Architect of New Realms",
    icon: "\u{1F3D7}️",
    flavor: "Shipped an entirely new feature from concept to merge.",
  },
  refactorerOfRuins: {
    id: "refactorerOfRuins",
    label: "Refactorer of Ancient Ruins",
    icon: "\u{1F3FA}",
    flavor: "Cleaned up code so old it had cobwebs and questionable variable names.",
  },
};

export interface EarnedBadge {
  id: string;
  label: string;
  icon: string;
  flavor: string;
  earnedAt: string;
  manual: boolean;
}

/**
 * Checks a single commit against every Tier-1 badge. `fileLastModified` is GLOBAL (shared
 * across all authors, not reset per contributor) and is mutated after the checks run, since
 * "Refactorer of Ancient Ruins" depends on the file's real history, not just this author's.
 */
export function evaluateCommitBadges(
  commit: Commit,
  config: QuestConfig,
  fileLastModified: Map<string, Date>
): AutoBadgeId[] {
  const earned: AutoBadgeId[] = [];
  const t = config.badges.thresholds;
  const totalChanged = commit.files.reduce((sum, f) => sum + f.additions + f.deletions, 0);

  const hour = commit.date.getUTCHours();
  if (hour >= t.midnightCommitter.startHour && hour < t.midnightCommitter.endHour) {
    earned.push("midnightCommitter");
  }

  const docChanged = commit.files
    .filter((f) => matchesActivity(f, config.guilds.activity.lorekeeper))
    .reduce((sum, f) => sum + f.additions + f.deletions, 0);
  if (docChanged >= t.keeperOfReadme.minChangedLines) earned.push("keeperOfReadme");

  if (totalChanged > 0 && totalChanged <= t.typoPaladin.maxChangedLines) earned.push("typoPaladin");

  const testAdditions = commit.files
    .filter((f) => matchesActivity(f, config.guilds.activity.verminHunter) && f.deletions === 0)
    .reduce((sum, f) => sum + f.additions, 0);
  if (testAdditions >= t.wardenOfTests.minAddedLines) earned.push("wardenOfTests");

  if (isFeatureCommit(commit.message, config)) earned.push("architectOfRealms");

  const staleMs = t.refactorerOfRuins.staleDays * 86_400_000;
  for (const file of commit.files) {
    const changed = file.additions + file.deletions;
    const last = fileLastModified.get(file.path);
    if (last && changed >= t.refactorerOfRuins.minChangedLines && commit.date.getTime() - last.getTime() >= staleMs) {
      earned.push("refactorerOfRuins");
      break;
    }
  }
  for (const file of commit.files) fileLastModified.set(file.path, commit.date);

  return earned.filter((id) => config.badges.autoEnabled.includes(id));
}

export interface ManualBadgeDefinition {
  label: string;
  icon: string;
  flavor: string;
}

export interface ManualBadgeAward {
  contributorEmail: string;
  badgeId: string;
  awardedAt: string;
  note?: string;
}

export interface ManualBadgesFile {
  definitions: Record<string, ManualBadgeDefinition>;
  awards: ManualBadgeAward[];
}

export function loadManualBadges(path: string): ManualBadgesFile {
  if (!existsSync(path)) return { definitions: {}, awards: [] };
  const raw = readFileSync(path, "utf8");
  return JSON.parse(raw) as ManualBadgesFile;
}
