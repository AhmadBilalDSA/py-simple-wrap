import type { QuestConfig } from "./config.ts";

/** XP earned by a single commit, given the total lines it changed. */
export function xpForCommit(config: QuestConfig, changedLines: number): number {
  const cappedLines = Math.min(changedLines, config.xp.changedLineCap);
  return config.xp.base + cappedLines * config.xp.perChangedLine;
}

/** RPG-style level curve: level growth slows as XP accrues. */
export function levelForXp(config: QuestConfig, xp: number): number {
  return Math.floor(Math.sqrt(xp / config.level.divisor)) + 1;
}

/** XP required to reach a given level, and progress toward the next one. */
export function levelProgress(config: QuestConfig, xp: number) {
  const level = levelForXp(config, xp);
  const xpForLevel = (lvl: number) => Math.pow(lvl - 1, 2) * config.level.divisor;
  const currentFloor = xpForLevel(level);
  const nextFloor = xpForLevel(level + 1);
  const span = nextFloor - currentFloor;
  const progress = span > 0 ? (xp - currentFloor) / span : 1;
  return { level, xpIntoLevel: xp - currentFloor, xpForNextLevel: span, progress };
}
