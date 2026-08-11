import { existsSync, readdirSync } from "node:fs";
import path from "node:path";
import type { GuildId, QuestConfig } from "./config.ts";

export interface QuestIssue {
  number: number;
  title: string;
  url: string;
  labels: string[];
}

export interface RelatedIssue extends QuestIssue {
  kind: "closed" | "suited";
}

export interface ExplorePath {
  label: string;
  url: string;
  kind: "file" | "dir";
}

export interface QuestBoardData {
  mode: "mixed" | "beginnerOnly" | "otherOnly" | "explore";
  beginner: QuestIssue[];
  other: QuestIssue[];
  explorePaths: ExplorePath[];
}

function authHeaders(token: string | undefined): Record<string, string> {
  const headers: Record<string, string> = { Accept: "application/vnd.github+json" };
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

interface RawIssue {
  number: number;
  title: string;
  html_url: string;
  state: string;
  labels: Array<string | { name: string }>;
  pull_request?: unknown;
}

function toQuestIssue(issue: RawIssue): QuestIssue {
  const labels = issue.labels.map((label) => (typeof label === "string" ? label : label.name));
  return { number: issue.number, title: issue.title, url: issue.html_url, labels };
}

/** Fetches every issue (open + closed, PRs excluded) in a single call. Null on any failure. */
export async function fetchAllIssues(
  owner: string,
  repo: string,
  token: string | undefined
): Promise<{ open: QuestIssue[]; closed: QuestIssue[] } | null> {
  try {
    const res = await fetch(`https://api.github.com/repos/${owner}/${repo}/issues?state=all&per_page=100`, {
      headers: authHeaders(token),
    });
    if (!res.ok) {
      console.warn(`Contributor Quest: issues API returned ${res.status} — falling back to explore mode.`);
      return null;
    }
    const data = (await res.json()) as RawIssue[];
    const issues = data.filter((issue) => !issue.pull_request);
    return {
      open: issues.filter((issue) => issue.state === "open").map(toQuestIssue),
      closed: issues.filter((issue) => issue.state === "closed").map(toQuestIssue),
    };
  } catch (err) {
    console.warn("Contributor Quest: failed to fetch issues — falling back to explore mode.", err);
    return null;
  }
}

const IGNORED_DIRS = new Set([
  ".git",
  ".github",
  "node_modules",
  ".idea",
  ".vscode",
  "site-build",
  "dist",
  "build",
  ".venv",
]);

function buildExplorePaths(cwd: string, repoUrl: string, branch: string): ExplorePath[] {
  const paths: ExplorePath[] = [];
  const fileCandidates: Array<{ file: string; label: string }> = [
    { file: "README.md", label: "The README — start here" },
    { file: "CONTRIBUTING.md", label: "The Contributing Guide" },
  ];
  for (const candidate of fileCandidates) {
    if (existsSync(path.join(cwd, candidate.file))) {
      paths.push({ label: candidate.label, url: `${repoUrl}/blob/${branch}/${candidate.file}`, kind: "file" });
    }
  }
  if (existsSync(path.join(cwd, "docs"))) {
    paths.push({ label: "The Docs Archive", url: `${repoUrl}/tree/${branch}/docs`, kind: "dir" });
  }

  const entries = readdirSync(cwd, { withFileTypes: true }).filter(
    (entry) => entry.isDirectory() && !entry.name.startsWith(".") && !IGNORED_DIRS.has(entry.name) && entry.name !== "docs"
  );
  for (const entry of entries.slice(0, 4)) {
    paths.push({ label: `Explore ${entry.name}/`, url: `${repoUrl}/tree/${branch}/${entry.name}`, kind: "dir" });
  }
  return paths;
}

export function explorePathsFor(cwd: string, repoUrl: string | null, branch: string | null): ExplorePath[] {
  return repoUrl ? buildExplorePaths(cwd, repoUrl, branch ?? "main") : [];
}

export function buildQuestBoard(openIssues: QuestIssue[] | null, config: QuestConfig, explorePaths: ExplorePath[]): QuestBoardData {
  if (!openIssues) {
    return { mode: "explore", beginner: [], other: [], explorePaths };
  }

  const beginnerLabels = config.issues.beginnerLabels.map((label) => label.toLowerCase());
  const beginner: QuestIssue[] = [];
  const other: QuestIssue[] = [];

  for (const issue of openIssues) {
    const isBeginner = issue.labels.some((label) => beginnerLabels.includes(label.toLowerCase()));
    (isBeginner ? beginner : other).push(issue);
  }

  const max = config.issues.maxPerCategory;
  if (beginner.length === 0 && other.length === 0) {
    return { mode: "explore", beginner: [], other: [], explorePaths };
  }
  if (beginner.length > 0 && other.length > 0) {
    return { mode: "mixed", beginner: beginner.slice(0, max), other: other.slice(0, max), explorePaths: [] };
  }
  if (beginner.length > 0) {
    return { mode: "beginnerOnly", beginner: beginner.slice(0, max * 2), other: [], explorePaths: [] };
  }
  return { mode: "otherOnly", beginner: [], other: other.slice(0, max * 2), explorePaths: [] };
}

const CLOSING_KEYWORDS = /\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)/gi;

/** Issue numbers this commit message would close on merge, per GitHub's closing-keyword syntax. */
export function issueRefsClosedBy(message: string): number[] {
  return [...message.matchAll(CLOSING_KEYWORDS)].map((match) => Number(match[1]));
}

const GUILD_LABEL_HINTS: Partial<Record<GuildId, string[]>> = {
  lorekeeper: ["doc", "documentation"],
  verminHunter: ["bug", "test"],
  architect: ["feature", "enhancement"],
  moduleSmith: ["enhancement", "refactor"],
};

/** Up to `count` open issues whose labels suit the given guild, excluding already-used numbers. */
export function findSuitedOpenIssues(
  openIssues: QuestIssue[],
  usedNumbers: Set<number>,
  guildId: GuildId,
  count: number
): RelatedIssue[] {
  if (count <= 0) return [];
  const hints = GUILD_LABEL_HINTS[guildId] ?? [];
  const candidates = openIssues.filter((issue) => !usedNumbers.has(issue.number));

  const matched =
    hints.length > 0
      ? candidates.filter((issue) => issue.labels.some((label) => hints.some((hint) => label.toLowerCase().includes(hint))))
      : [];
  const pool = matched.length > 0 ? matched : candidates;

  return pool.slice(0, count).map((issue) => ({ ...issue, kind: "suited" as const }));
}

/** Issues this author's commits closed, matched against the fetched closed-issues list. */
export function findClosedByAuthor(closedIssues: QuestIssue[], refs: Set<number>): RelatedIssue[] {
  return closedIssues.filter((issue) => refs.has(issue.number)).map((issue) => ({ ...issue, kind: "closed" as const }));
}
