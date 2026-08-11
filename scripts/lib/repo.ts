import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import path from "node:path";

export interface RepoInfo {
  owner: string | null;
  name: string | null;
  branch: string | null;
  repoUrl: string | null;
}

function parseOwnerRepoFromRemote(cwd: string): { owner: string; name: string } | null {
  try {
    const url = execFileSync("git", ["remote", "get-url", "origin"], { cwd, encoding: "utf8" }).trim();
    const match = url.match(/[/:]([^/:]+)\/([^/]+?)(\.git)?$/);
    if (!match) return null;
    return { owner: match[1], name: match[2] };
  } catch {
    return null;
  }
}

export function getRepoInfo(cwd: string): RepoInfo {
  const fromEnv = process.env.GITHUB_REPOSITORY;
  let owner: string | null = null;
  let name: string | null = null;

  if (fromEnv?.includes("/")) {
    [owner, name] = fromEnv.split("/");
  } else {
    const parsed = parseOwnerRepoFromRemote(cwd);
    owner = parsed?.owner ?? null;
    name = parsed?.name ?? null;
  }

  let branch = process.env.GITHUB_REF_NAME ?? null;
  if (!branch) {
    try {
      branch = execFileSync("git", ["branch", "--show-current"], { cwd, encoding: "utf8" }).trim() || null;
    } catch {
      branch = null;
    }
  }

  const repoUrl = owner && name ? `https://github.com/${owner}/${name}` : null;
  return { owner, name, branch, repoUrl };
}

const PACKAGE_MANIFESTS = [
  "package.json",
  "pyproject.toml",
  "setup.py",
  "Cargo.toml",
  "go.mod",
  "composer.json",
  "Gemfile",
  "pom.xml",
  "build.gradle",
  "build.gradle.kts",
];

/** Heuristic: does this repo look like a published package/library vs. an application? */
export function looksLikePackage(cwd: string): boolean {
  return PACKAGE_MANIFESTS.some((manifest) => existsSync(path.join(cwd, manifest)));
}
