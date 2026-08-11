import { existsSync, readdirSync } from "node:fs";
import path from "node:path";
import type { QuestConfig } from "./config.ts";

export interface QuestIssue {
  number: number;
  title: string;
  url: string;
  labels: string[];
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
  labels: Array<string | { name: string }>;
  pull_request?: unknown;
}

async function fetchOpenIssues(owner: string, repo: string, token: string | undefined): Promise<RawIssue[] | null> {
  try {
    const res = await fetch(`https://api.github.com/repos/${owner}/${repo}/issues?state=open&per_page=100`, {
      headers: authHeaders(token),
    });
    if (!res.ok) {
      console.warn(`Contributor Quest: issues API returned ${res.status} — falling back to explore mode.`);
      return null;
    }
    const data = (await res.json()) as RawIssue[];
    return data.filter((issue) => !issue.pull_request);
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

export async function fetchQuestBoard(
  owner: string | null,
  repoName: string | null,
  repoUrl: string | null,
  branch: string | null,
  cwd: string,
  config: QuestConfig,
  token: string | undefined
): Promise<QuestBoardData> {
  const effectiveBranch = branch ?? "main";
  const explorePaths = repoUrl ? buildExplorePaths(cwd, repoUrl, effectiveBranch) : [];

  const rawIssues = owner && repoName ? await fetchOpenIssues(owner, repoName, token) : null;
  if (!rawIssues) {
    return { mode: "explore", beginner: [], other: [], explorePaths };
  }

  const beginnerLabels = config.issues.beginnerLabels.map((label) => label.toLowerCase());
  const beginner: QuestIssue[] = [];
  const other: QuestIssue[] = [];

  for (const issue of rawIssues) {
    const labels = issue.labels.map((label) => (typeof label === "string" ? label : label.name));
    const isBeginner = labels.some((label) => beginnerLabels.includes(label.toLowerCase()));
    const entry: QuestIssue = { number: issue.number, title: issue.title, url: issue.html_url, labels };
    (isBeginner ? beginner : other).push(entry);
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
