export interface CollaboratorInfo {
  login: string;
  isAdmin: boolean;
}

function authHeaders(token: string | undefined): Record<string, string> {
  const headers: Record<string, string> = { Accept: "application/vnd.github+json" };
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

/**
 * Lists repo collaborators + permission level. Returns null (rather than throwing) on any
 * failure — this endpoint commonly 403s for org repos when the default GITHUB_TOKEN lacks
 * member-list access, and Maintainer/Collaborator guilds should just be skipped in that case.
 */
export async function fetchCollaborators(
  owner: string,
  repo: string,
  token: string | undefined
): Promise<CollaboratorInfo[] | null> {
  try {
    const res = await fetch(`https://api.github.com/repos/${owner}/${repo}/collaborators?per_page=100`, {
      headers: authHeaders(token),
    });
    if (!res.ok) {
      console.warn(
        `Contributor Quest: collaborators API returned ${res.status} — skipping Maintainer/Collaborator guilds. ` +
          `(This is common for org repos where the default GITHUB_TOKEN lacks member-list access; a PAT with read access to members would fix it.)`
      );
      return null;
    }
    const data = (await res.json()) as Array<{ login: string; permissions?: { admin?: boolean }; role_name?: string }>;
    return data.map((c) => ({
      login: c.login,
      isAdmin: c.permissions?.admin === true || c.role_name === "admin",
    }));
  } catch (err) {
    console.warn("Contributor Quest: failed to fetch collaborators — skipping Maintainer/Collaborator guilds.", err);
    return null;
  }
}

/**
 * Best-effort match of a commit author's email to a GitHub login, via the commits API's
 * `author` field (GitHub resolves this when the email is linked to a verified account).
 */
export async function fetchLoginForEmail(
  owner: string,
  repo: string,
  email: string,
  token: string | undefined
): Promise<string | null> {
  if (!email) return null;
  try {
    const url = `https://api.github.com/repos/${owner}/${repo}/commits?author=${encodeURIComponent(email)}&per_page=1`;
    const res = await fetch(url, { headers: authHeaders(token) });
    if (!res.ok) return null;
    const data = (await res.json()) as Array<{ author: { login: string } | null }>;
    return data[0]?.author?.login ?? null;
  } catch {
    return null;
  }
}
