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

export function levelTitleFor(config: QuestConfig, level: number): string {
  let best = config.levelTitles[0]?.title ?? "Adventurer";
  for (const entry of config.levelTitles) {
    if (level >= entry.minLevel) best = entry.title;
  }
  return best;
}
