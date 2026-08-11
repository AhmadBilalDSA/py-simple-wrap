import json
import os
import re
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY")
if not REPO:
    raise SystemExit(
        "GITHUB_REPOSITORY is not set.\n"
        "In the Action this is injected automatically. To run locally, set it yourself, e.g.:\n"
        '  PowerShell:  $env:GITHUB_REPOSITORY = "sara-czasak/py-simple-wrap"\n'
        "  bash:        export GITHUB_REPOSITORY=sara-czasak/py-simple-wrap"
    )

TOKEN = os.environ.get("GITHUB_TOKEN")
FILE_PATH = "CONTRIBUTORS.md"
MARKER_START = "<!-- NEW-CONTRIBUTORS:START -->"
MARKER_END = "<!-- NEW-CONTRIBUTORS:END -->"
ANCHOR = "## ⚔️ The Merge Mages' Hall of Fame"
EXCLUDE_LOGINS = {"allcontributors[bot]", "web-flow"}


def gh_get(url):
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "py-simple-wrap-contributors-bot",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch_merged_pr_authors():
    """Real, live data only — no estimates. Search API, paginated."""
    authors = set()
    page = 1
    while True:
        url = (
            f"https://api.github.com/search/issues?q=repo:{REPO}+type:pr+is:merged"
            f"&per_page=100&page={page}"
        )
        items = gh_get(url).get("items", [])
        if not items:
            break
        for item in items:
            login = item["user"]["login"]
            if login not in EXCLUDE_LOGINS:
                authors.add(login)
        if len(items) < 100:
            break
        page += 1
    return authors


def known_logins_from_file(text):
    """Anyone already linked anywhere in the file counts as known/sorted."""
    return set(re.findall(r"github\.com/([A-Za-z0-9-]+)[\"/]", text))


def build_section(new_logins):
    rows = []
    for login in sorted(new_logins, key=str.lower):
        rows.append(
            '    <td align="center" valign="top" width="16.6%">\n'
            f'      <a href="https://github.com/{login}">\n'
            f'        <img src="https://github.com/{login}.png" width="100px;" alt="{login}"/><br />\n'
            f"        <sub><b>{login}</b></sub>\n"
            "      </a><br />\n"
            "      <sub><i>Needs a guild + blurb — see CONTRIBUTING.md.</i></sub>\n"
            "    </td>"
        )
    chunks = [rows[i : i + 6] for i in range(0, len(rows), 6)]
    table_rows = "\n  </tr>\n  <tr>\n".join("\n".join(chunk) for chunk in chunks)
    return (
        f"{MARKER_START}\n"
        "## 🆕 Newly Arrived\n"
        "🎉 **Welcome to the team!** Thank you for your first merged contribution to "
        "py-simple-wrap — you'll be sorted into a proper guild soon.\n\n"
        "*Detected automatically from merged PRs — not yet sorted into a guild. "
        "Maintainer: give these folks a home!*\n\n"
        "<table>\n  <tr>\n"
        f"{table_rows}\n"
        "  </tr>\n</table>\n\n"
        "---\n\n"
        f"{MARKER_END}"
    )


def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    known = known_logins_from_file(text)
    new_logins = fetch_merged_pr_authors() - known

    has_marker = MARKER_START in text and MARKER_END in text
    marker_pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.DOTALL
    )

    if not new_logins:
        if has_marker:
            text = marker_pattern.sub("", text).rstrip() + "\n"
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                f.write(text)
            print("Newly Arrived section is now empty — removed it.")
        else:
            print("No new contributors. Nothing to do.")
        return

    section = build_section(new_logins)

    if has_marker:
        text = marker_pattern.sub(section, text)
    else:
        idx = text.find(ANCHOR)
        if idx == -1:
            text = text.rstrip() + "\n\n---\n\n" + section + "\n"
        else:
            text = text[:idx] + section + "\n\n" + text[idx:]

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Flagged {len(new_logins)} new contributor(s): {', '.join(sorted(new_logins))}")


if __name__ == "__main__":
    main()
