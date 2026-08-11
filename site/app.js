let STATE = null;

function typewrite(el, text, speedMs = 22) {
  el.textContent = "";
  let i = 0;
  const tick = () => {
    el.textContent = text.slice(0, i);
    i += 1;
    if (i <= text.length) setTimeout(tick, speedMs);
  };
  tick();
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function guildInfo(id) {
  const found = STATE?.guildCatalog.find((g) => g.id === id);
  return found ?? { id, name: id, icon: "⚔️", kind: "activity" };
}

// ---- Router ----

const SCREENS = ["menu", "quest", "leaderboard", "profile"];

function currentRoute() {
  const [screen, param] = location.hash.replace(/^#\/?/, "").split("/");
  return { screen: SCREENS.includes(screen) ? screen : "menu", param };
}

function render(route) {
  for (const screen of SCREENS) {
    document.getElementById(`screen-${screen}`).hidden = screen !== route.screen;
  }
  if (route.screen === "quest") renderQuestBoard();
  if (route.screen === "leaderboard") renderLeaderboard();
  if (route.screen === "profile") renderProfile(route.param);
  if (route.screen === "menu") document.querySelector(".menu__item")?.focus();
}

function navigate(screen, param) {
  location.hash = param ? `/${screen}/${param}` : `/${screen}`;
}

window.addEventListener("hashchange", () => render(currentRoute()));

// ---- Menu ----

function setupMenu() {
  const nav = document.getElementById("menu-nav");
  const items = [...nav.querySelectorAll(".menu__item")];

  nav.addEventListener("click", (e) => {
    const btn = e.target.closest(".menu__item");
    if (!btn) return;
    handleMenuAction(btn);
  });

  nav.addEventListener("keydown", (e) => {
    const idx = items.indexOf(document.activeElement);
    if (e.key === "ArrowDown") {
      e.preventDefault();
      items[(idx + 1 + items.length) % items.length]?.focus();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      items[(idx - 1 + items.length) % items.length]?.focus();
    } else if (e.key === "Enter" && document.activeElement.classList.contains("menu__item")) {
      handleMenuAction(document.activeElement);
    }
  });

  document.addEventListener("keydown", (e) => {
    if (currentRoute().screen !== "menu") return;
    const match = items.find((btn) => btn.dataset.key === e.key);
    if (match) handleMenuAction(match);
  });
}

function handleMenuAction(btn) {
  if (btn.dataset.action === "support") {
    const url = STATE?.meta.repoUrl ?? "https://github.com";
    window.open(url, "_blank", "noopener");
    return;
  }
  if (btn.dataset.route) navigate(btn.dataset.route);
}

document.addEventListener("click", (e) => {
  const back = e.target.closest("[data-route]");
  if (back && !back.classList.contains("menu__item")) navigate(back.dataset.route);
});

// ---- Quest board ----

function questItemHtml(issue) {
  const labels = issue.labels.length ? `<span class="quest-item__labels">${escapeHtml(issue.labels.join(", "))}</span>` : "";
  return `
    <a class="quest-item" href="${issue.url}" target="_blank" rel="noopener">
      <span class="quest-item__num">#${issue.number}</span>${escapeHtml(issue.title)}
      ${labels}
    </a>
  `;
}

function questListHtml(title, issues) {
  if (!issues.length) return "";
  return `
    <div class="quest-section">
      <h3 class="quest-section__title">${title}</h3>
      <ul class="quest-list">${issues.map((i) => `<li>${questItemHtml(i)}</li>`).join("")}</ul>
    </div>
  `;
}

function explorePathHtml(p) {
  const icon = p.kind === "dir" ? "\u{1F5C2}️" : "\u{1F4C4}";
  return `<li><a class="quest-item" href="${p.url}" target="_blank" rel="noopener">${icon} ${escapeHtml(p.label)}</a></li>`;
}

function renderQuestBoard() {
  const heading = document.getElementById("quest-heading");
  const content = document.getElementById("quest-content");
  const quests = STATE?.quests;
  if (!quests) {
    heading.textContent = "The Quest Board";
    content.innerHTML = "";
    return;
  }

  if (quests.mode === "mixed") {
    heading.textContent = "The Quest Board";
    content.innerHTML =
      questListHtml("\u{1F331} Novice Trials", quests.beginner) + questListHtml("⚔️ Greater Quests", quests.other);
  } else if (quests.mode === "beginnerOnly") {
    heading.textContent = "The Quest Board";
    content.innerHTML = questListHtml("\u{1F331} Novice Trials", quests.beginner);
  } else if (quests.mode === "otherOnly") {
    heading.textContent = "The Quest Board";
    content.innerHTML = questListHtml("\u{1F4DC} Open Quests", quests.other);
  } else {
    heading.textContent = "Uncharted Territory";
    content.innerHTML = `
      <p class="explore-note">No open quests await just yet — but every legend starts somewhere. Pick a path to explore:</p>
      <ul class="quest-list">${quests.explorePaths.map(explorePathHtml).join("")}</ul>
    `;
  }
}

// ---- Leaderboard ----

function badgeHtml(badge) {
  const cls = badge.manual ? "badge badge--manual" : "badge";
  return `<span class="${cls}" title="${escapeHtml(badge.label)} — ${escapeHtml(badge.flavor)}">${badge.icon}</span>`;
}

function contributorKey(contributor) {
  return encodeURIComponent(contributor.email);
}

function findContributor(key) {
  const email = decodeURIComponent(key ?? "");
  return STATE?.contributors.find((c) => c.email === email) ?? null;
}

function leaderboardCardHtml(contributor, index) {
  const primary = guildInfo(contributor.primaryGuild);
  const otherGuilds = contributor.guilds.filter((id) => id !== contributor.primaryGuild).map(guildInfo);
  const crests = otherGuilds.map((g) => `<span class="badge" title="${escapeHtml(g.name)}">${g.icon}</span>`).join("");
  const championOf = contributor.championOf ?? [];
  const crown = championOf.length
    ? `<span class="crown" title="Guild Champion: ${escapeHtml(championOf.map((id) => guildInfo(id).name).join(", "))}">👑</span>`
    : "";

  return `
    <article class="card card--clickable" style="animation-delay:${index * 60}ms" data-profile="${contributorKey(contributor)}" tabindex="0" role="button">
      <div class="card__head">
        <span class="card__name"><span class="card__rank">#${contributor.rank}</span>${crown}${escapeHtml(contributor.name)}</span>
        <span class="card__level">Lv.${contributor.level}</span>
      </div>
      <div class="card__subline">${contributor.levelTitle} · ${primary.icon} ${escapeHtml(primary.name)}<span class="card__crests">${crests}</span></div>
      <div class="xp-bar"><div class="xp-bar__fill" data-progress="${Math.round(contributor.levelProgress * 100)}"></div></div>
      <div class="card__stats">${contributor.xp} XP · ${contributor.commitCount} commits</div>
      <div class="badges">${contributor.recentBadges.map(badgeHtml).join("")}</div>
    </article>
  `;
}

function expertsPanelHtml(contributors) {
  const activityGuilds = (STATE?.guildCatalog ?? []).filter((g) => g.kind === "activity");
  if (!activityGuilds.length) return "";

  const rows = activityGuilds
    .map((guild) => {
      const champions = contributors.filter((c) => (c.championOf ?? []).includes(guild.id));
      const names = champions.length
        ? champions
            .map((c) => `<a href="#/profile/${contributorKey(c)}">${escapeHtml(c.name)}</a>`)
            .join(", ")
        : '<span class="experts__vacant">awaiting a champion</span>';
      return `<li><span>${guild.icon} ${escapeHtml(guild.name)}</span><span>${names}</span></li>`;
    })
    .join("");

  return `
    <div class="experts">
      <h3 class="quest-section__title">\u{1F9ED} Ask the Experts</h3>
      <ul class="experts__list">${rows}</ul>
    </div>
  `;
}

function renderLeaderboard() {
  const content = document.getElementById("leaderboard-content");
  const contributors = STATE?.contributors ?? [];
  if (!contributors.length) {
    content.innerHTML = '<p class="roster--empty">No adventurers have answered the call yet. Make the first commit!</p>';
    return;
  }
  content.innerHTML = expertsPanelHtml(contributors) + contributors.map(leaderboardCardHtml).join("");
  requestAnimationFrame(() => {
    content.querySelectorAll(".xp-bar__fill").forEach((el) => {
      el.style.width = `${el.dataset.progress}%`;
    });
  });
}

document.addEventListener("click", (e) => {
  const card = e.target.closest("[data-profile]");
  if (card) navigate("profile", card.dataset.profile);
});

document.addEventListener("keydown", (e) => {
  if (e.key !== "Enter" && e.key !== " ") return;
  const card = document.activeElement?.closest?.("[data-profile]");
  if (card) {
    e.preventDefault();
    navigate("profile", card.dataset.profile);
  }
});

// ---- Profile ----

function fullBadgeHtml(badge) {
  const cls = badge.manual ? "profile-badge profile-badge--manual" : "profile-badge";
  const date = new Date(badge.earnedAt).toLocaleDateString();
  return `
    <li class="${cls}">
      <span class="profile-badge__icon">${badge.icon}</span>
      <span class="profile-badge__body">
        <span class="profile-badge__label">${escapeHtml(badge.label)}${badge.manual ? " ✋" : ""}</span>
        <span class="profile-badge__flavor">${escapeHtml(badge.flavor)}</span>
        <span class="profile-badge__date">earned ${date}</span>
      </span>
    </li>
  `;
}

function renderProfile(key) {
  const content = document.getElementById("profile-content");
  const contributor = findContributor(key);

  if (!contributor) {
    content.innerHTML = '<p class="roster--empty">This adventurer could not be found.</p>';
    return;
  }

  const championOf = contributor.championOf ?? [];
  const guildRows = contributor.guilds
    .map((id) => guildInfo(id))
    .sort((a, b) => (a.id === contributor.primaryGuild ? -1 : b.id === contributor.primaryGuild ? 1 : 0))
    .map((g) => {
      const tags = [
        championOf.includes(g.id) ? '<span class="profile-guild__tag profile-guild__tag--champion">👑 champion</span>' : "",
        g.id === contributor.primaryGuild ? '<span class="profile-guild__tag">primary</span>' : "",
      ].join("");
      return `
        <li class="profile-guild${g.id === contributor.primaryGuild ? " profile-guild--primary" : ""}">
          <span>${g.icon} ${escapeHtml(g.name)}</span>
          ${tags}
        </li>
      `;
    })
    .join("");

  const badgesHtml = [...contributor.badges]
    .sort((a, b) => b.earnedAt.localeCompare(a.earnedAt))
    .map(fullBadgeHtml)
    .join("");

  const relatedIssues = contributor.relatedIssues ?? [];
  const relatedHtml = relatedIssues
    .map((issue) => {
      const tag =
        issue.kind === "closed" ? '<span class="quest-item__tag quest-item__tag--closed">✅ closed</span>' : '<span class="quest-item__tag">💡 suggested</span>';
      return `<li><a class="quest-item" href="${issue.url}" target="_blank" rel="noopener"><span class="quest-item__num">#${issue.number}</span>${escapeHtml(issue.title)} ${tag}</a></li>`;
    })
    .join("");

  content.innerHTML = `
    <div class="profile">
      <div class="profile__head">
        <h2 class="screen-heading">${escapeHtml(contributor.name)}</h2>
        <span class="card__rank">#${contributor.rank} · Lv.${contributor.level} ${escapeHtml(contributor.levelTitle)}</span>
      </div>
      <div class="xp-bar"><div class="xp-bar__fill" data-progress="${Math.round(contributor.levelProgress * 100)}"></div></div>
      <div class="card__stats">${contributor.xp} XP · ${contributor.commitCount} commits</div>
      <div class="card__stats">first seen ${new Date(contributor.firstCommit).toLocaleDateString()} · last active ${new Date(contributor.lastCommit).toLocaleDateString()}</div>

      <h3 class="quest-section__title">Guild Memberships</h3>
      <ul class="profile-guilds">${guildRows}</ul>

      <h3 class="quest-section__title">Related Quests</h3>
      ${relatedHtml ? `<ul class="quest-list">${relatedHtml}</ul>` : '<p class="roster--empty">No related quests yet.</p>'}

      <h3 class="quest-section__title">Achievements</h3>
      ${badgesHtml ? `<ul class="profile-badges">${badgesHtml}</ul>` : '<p class="roster--empty">No badges earned yet — the legend is just beginning.</p>'}
    </div>
  `;

  requestAnimationFrame(() => {
    content.querySelectorAll(".xp-bar__fill").forEach((el) => {
      el.style.width = `${el.dataset.progress}%`;
    });
  });
}

// ---- Boot ----

async function main() {
  const titleEl = document.getElementById("quest-title");
  const introEl = document.getElementById("menu-intro");
  const updatedEl = document.getElementById("quest-updated");

  setupMenu();

  try {
    const res = await fetch("./data/state.json", { cache: "no-store" });
    STATE = await res.json();
  } catch (err) {
    titleEl.textContent = "QUEST DATA NOT FOUND";
    introEl.textContent = "Run the generator to create data/state.json.";
    return;
  }

  if (STATE.meta.accent) {
    document.documentElement.style.setProperty("--accent", STATE.meta.accent);
  }

  titleEl.textContent = STATE.meta.title;
  typewrite(introEl, `${STATE.contributors.length} adventurer(s) have answered the call. What will you do?`);
  updatedEl.textContent = `last updated ${new Date(STATE.meta.generatedAt).toLocaleString()}`;

  render(currentRoute());
}

main();
