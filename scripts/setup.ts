import path from "node:path";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { createInterface } from "node:readline";
import type { GuildId, QuestConfig } from "./lib/config.ts";
import { GUILD_CATALOG } from "./lib/guilds.ts";
import { looksLikePackage } from "./lib/repo.ts";

const cwd = process.cwd();
const configPath = path.join(cwd, "quest.config.json");

// A persistent 'line' listener (rather than readline/promises' question(), which attaches a
// one-shot listener per call) — piped/non-TTY stdin can deliver all lines in a single tick,
// and a one-shot listener drops every line that arrives before the next question() is set up.
const rl = createInterface({ input: process.stdin, output: process.stdout, terminal: process.stdin.isTTY });
const lineQueue: string[] = [];
const waiters: Array<(line: string | null) => void> = [];
rl.on("line", (line) => {
  const waiter = waiters.shift();
  if (waiter) waiter(line);
  else lineQueue.push(line);
});
rl.on("close", () => {
  while (waiters.length) waiters.shift()?.(null);
});

function nextLine(): Promise<string | null> {
  if (lineQueue.length) return Promise.resolve(lineQueue.shift()!);
  return new Promise((resolve) => waiters.push(resolve));
}

async function prompt(text: string): Promise<string> {
  process.stdout.write(text);
  const line = await nextLine();
  return (line ?? "").trim();
}

async function askYesNo(question: string, defaultYes: boolean): Promise<boolean> {
  const hint = defaultYes ? "Y/n" : "y/N";
  const answer = (await prompt(`${question} [${hint}] `)).toLowerCase();
  if (!answer) return defaultYes;
  return answer.startsWith("y");
}

async function ask(question: string, defaultValue: string): Promise<string> {
  const hint = defaultValue ? ` (${defaultValue})` : "";
  const answer = await prompt(`${question}${hint}: `);
  return answer || defaultValue;
}

function suggestionFor(id: GuildId, isPackage: boolean): boolean {
  if (id === "architect") return !isPackage;
  if (id === "moduleSmith") return isPackage;
  return true;
}

async function main() {
  console.log("\n⚔️  Contributor Quest — Setup Wizard ⚔️\n");
  console.log("Answer a few questions to configure the game for this repo.");
  console.log("Press Enter at any prompt to accept the default shown in parentheses/brackets.\n");

  if (!existsSync(configPath)) {
    console.error(`Could not find ${configPath}. Run this from the root of a Contributor Quest repo.`);
    process.exitCode = 1;
    rl.close();
    return;
  }

  const config = JSON.parse(readFileSync(configPath, "utf8")) as QuestConfig;
  const isPackage = looksLikePackage(cwd);
  console.log(
    isPackage
      ? "Detected a package manifest — this looks like a library/package repo.\n"
      : "No package manifest detected — this looks like an application repo.\n"
  );

  console.log("Which guilds should this quest track?\n");
  const enabled: GuildId[] = [];
  for (const guild of GUILD_CATALOG) {
    const suggestion = suggestionFor(guild.id, isPackage);
    const on = await askYesNo(`  ${guild.icon}  ${guild.name}`, suggestion);
    if (on) enabled.push(guild.id);
  }
  config.guilds.enabled = enabled;

  if (enabled.includes("newAdventurer")) {
    const days = await ask(
      "\nHow many days should someone stay a 'New Adventurer' after their first commit?",
      String(config.guilds.newAdventurerWindowDays)
    );
    const parsed = Number(days);
    config.guilds.newAdventurerWindowDays = Number.isFinite(parsed) && parsed > 0 ? parsed : config.guilds.newAdventurerWindowDays;
  }

  if (enabled.includes("maintainer") || enabled.includes("collaborator")) {
    console.log(
      "\nNote: Maintainer/Collaborator guilds need the GitHub collaborators API. This works out of\n" +
        "the box for personal repos; for org repos the default GITHUB_TOKEN may not have access —\n" +
        "if so, those two guilds are silently skipped at build time rather than failing the build."
    );
  }

  const title = await ask("\nCustom title (blank = auto-generate from repo name)", config.title ?? "");
  config.title = title || null;

  const accent = await ask("Accent color (hex)", config.theme.accent);
  config.theme.accent = accent;

  writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");

  console.log("\n✅ Wrote quest.config.json\n");
  console.log("Next steps:");
  console.log("  1. Review quest.config.json (and manual-badges.json if you want hand-awarded badges).");
  console.log("  2. Commit and push to main.");
  console.log("  3. In GitHub: Settings → Pages → Source: GitHub Actions.");
  console.log("  4. Watch the 'Contributor Quest' workflow run, then visit your Pages URL.\n");

  rl.close();
}

main();
