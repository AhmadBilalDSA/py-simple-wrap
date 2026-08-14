import { execFileSync } from "node:child_process";

export interface FileChange {
  path: string;
  extension: string;
  additions: number;
  deletions: number;
}

export interface Commit {
  hash: string;
  authorName: string;
  authorEmail: string;
  date: Date;
  message: string;
  files: FileChange[];
}

const RECORD_SEP = "\x1f";
const COMMIT_MARK = "\x02COMMIT\x1f";
const BODY_END_MARK = "\x1eEND_OF_COMMIT_QUEST_BODY\x1e";

function extensionOf(path: string): string {
  const base = path.split("/").pop() ?? path;
  if (/^dockerfile$/i.test(base)) return "dockerfile";
  const dot = base.lastIndexOf(".");
  if (dot <= 0) return "";
  return base.slice(dot + 1).toLowerCase();
}

/**
 * Parses the full commit history of `cwd` (a git repo) via `git log --numstat`.
 * Captures the *full* commit message (%B: subject + body), not just the subject line, since
 * self-report markers (see commitMarkers.ts) live in the body below a commit template.
 */
export function getCommits(cwd: string): Commit[] {
  const format = `${COMMIT_MARK}%H${RECORD_SEP}%an${RECORD_SEP}%ae${RECORD_SEP}%aI%n%B%n${BODY_END_MARK}`;
  const raw = execFileSync(
    "git",
    ["log", "--no-color", "--date=iso-strict", `--pretty=format:${format}`, "--numstat"],
    { cwd, encoding: "utf8", maxBuffer: 1024 * 1024 * 64 }
  );

  const commits: Commit[] = [];
  const blocks = raw.split(COMMIT_MARK).filter(Boolean);

  for (const block of blocks) {
    const newlineIdx = block.indexOf("\n");
    const header = newlineIdx === -1 ? block : block.slice(0, newlineIdx);
    const rest = newlineIdx === -1 ? "" : block.slice(newlineIdx + 1);
    const [hash, authorName, authorEmail, dateStr] = header.split(RECORD_SEP);
    if (!hash) continue;

    const endIdx = rest.indexOf(BODY_END_MARK);
    const message = endIdx === -1 ? rest.trim() : rest.slice(0, endIdx).trimEnd();
    const numstatText = endIdx === -1 ? "" : rest.slice(endIdx + BODY_END_MARK.length);

    const files: FileChange[] = [];
    for (const line of numstatText.split("\n")) {
      if (!line.trim()) continue;
      const parts = line.split("\t");
      if (parts.length < 3) continue;
      const [addStr, delStr, path] = parts;
      const additions = addStr === "-" ? 0 : Number(addStr);
      const deletions = delStr === "-" ? 0 : Number(delStr);
      files.push({ path, extension: extensionOf(path), additions, deletions });
    }

    commits.push({
      hash,
      authorName,
      authorEmail,
      date: new Date(dateStr),
      message,
      files,
    });
  }

  return commits;
}
