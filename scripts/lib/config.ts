import { readFileSync } from "node:fs";

export interface ActivityRule {
  extensions?: string[];
  pathPatterns?: string[];
  commitMessagePrefixes?: string[];
}

export interface LevelTitle {
  minLevel: number;
  title: string;
}

export interface IdentityAlias {
  canonicalName: string;
  canonicalEmail: string;
  aliasEmails?: string[];
  aliasNames?: string[];
}

export type GuildId =
  | "mergeMage"
  | "lorekeeper"
  | "verminHunter"
  | "architect"
  | "moduleSmith"
  | "maintainer"
  | "collaborator"
  | "newAdventurer";

export interface QuestConfig {
  title: string | null;
  titleSuffix: string;
  theme: { accent: string };
  xp: { base: number; perChangedLine: number; changedLineCap: number };
  level: { divisor: number };
  levelTitles: LevelTitle[];
  guilds: {
    newAdventurerWindowDays: number;
    enabled: GuildId[];
    activity: {
      lorekeeper: ActivityRule;
      verminHunter: ActivityRule;
      architect: ActivityRule;
    };
  };
  badges: {
    autoEnabled: string[];
    thresholds: {
      midnightCommitter: { startHour: number; endHour: number };
      keeperOfReadme: { minChangedLines: number };
      typoPaladin: { maxChangedLines: number };
      wardenOfTests: { minAddedLines: number };
      refactorerOfRuins: { minChangedLines: number; staleDays: number };
    };
  };
  issues: {
    beginnerLabels: string[];
    maxPerCategory: number;
  };
  identityAliases: IdentityAlias[];
}

export function loadConfig(path: string): QuestConfig {
  const raw = readFileSync(path, "utf8");
  return JSON.parse(raw) as QuestConfig;
}

export function deriveTitle(config: QuestConfig, repoName: string | undefined): string {
  if (config.title) return config.title;
  const name = (repoName ?? "this repo").replace(/[-_]+/g, " ").trim().toUpperCase();
  return `${name} ${config.titleSuffix}`.trim();
}

export interface ResolvedIdentity {
  key: string;
  name: string;
  email: string;
}

function norm(value: string): string {
  return value.trim().toLowerCase();
}

/**
 * Folds alternate names/emails (e.g. someone who changed their GitHub handle or committed
 * under an old work email) into one canonical identity, per `identityAliases` in config.
 * Matching is case-insensitive and whitespace-trimmed, since git author info can vary in
 * casing between commits even for the same person/machine.
 */
export function resolveIdentity(authorName: string, authorEmail: string, config: QuestConfig): ResolvedIdentity {
  const email = norm(authorEmail);
  const name = norm(authorName);

  for (const alias of config.identityAliases ?? []) {
    const emailCandidates = [alias.canonicalEmail, ...(alias.aliasEmails ?? [])].map(norm);
    const nameCandidates = [alias.canonicalName, ...(alias.aliasNames ?? [])].map(norm);
    if (emailCandidates.includes(email) || nameCandidates.includes(name)) {
      return { key: norm(alias.canonicalEmail), name: alias.canonicalName, email: alias.canonicalEmail };
    }
  }
  return { key: email || name, name: authorName, email: authorEmail };
}

export function levelTitleFor(config: QuestConfig, level: number): string {
  let best = config.levelTitles[0]?.title ?? "Adventurer";
  for (const entry of config.levelTitles) {
    if (level >= entry.minLevel) best = entry.title;
  }
  return best;
}
