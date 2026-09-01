// The Big Book of Modules — hash router + renderers.
// Reads window.BOOK_DATA, which data/modules.js assigns before this file runs.
// No build step, no fetch(): everything here must work from a file:// URL.

let BOOK = null;

// The synthesized 7th menu entry. It is NOT in the data file — the plan says
// app.js invents it — so it lives here and is spliced in wherever a category
// list or a category lookup happens.
const ALL_CATEGORY = {
  id: "all",
  name: "All modules",
  icon: "📚",
  blurb: "every module in the book, in one alphabetical list",
};

// ---- Helpers ----

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str == null ? "" : String(str);
  return div.innerHTML;
}

// escapeHtml alone leaves quotes intact, which would break out of an attribute.
function escapeAttr(str) {
  return escapeHtml(str).replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

// Only let http(s) and same-folder relative links become buttons, so a bad data
// entry can never smuggle in a javascript: URL.
function safeUrl(url) {
  const raw = typeof url === "string" ? url.trim() : "";
  if (!raw) return null;
  if (/^https?:\/\//i.test(raw)) return raw;
  if (/^(\.{0,2}\/|[\w-]+\/)/.test(raw) && !/^\w+:/.test(raw)) return raw;
  return null;
}

function categories() {
  return BOOK?.categories ?? [];
}

function menuCategories() {
  return [...categories(), ALL_CATEGORY];
}

function findCategory(id) {
  const key = decodeURIComponent(id ?? "");
  if (key === ALL_CATEGORY.id) return ALL_CATEGORY;
  return categories().find((c) => c.id === key) ?? null;
}

function findModule(id) {
  const key = decodeURIComponent(id ?? "");
  return BOOK?.modules.find((m) => m.id === key) ?? null;
}

function byName(a, b) {
  return String(a.name ?? "").localeCompare(String(b.name ?? ""));
}

// "all" is the only category that isn't stored on the modules themselves,
// so it is handled as a pass-through rather than a filter.
function modulesInCategory(categoryId) {
  const all = BOOK?.modules ?? [];
  const list = categoryId === ALL_CATEGORY.id ? [...all] : all.filter((m) => m.category === categoryId);
  return list.sort(byName);
}

// ---- Router ----

const SCREENS = ["menu", "category", "module"];

function currentRoute() {
  const [screen, param, from] = location.hash.replace(/^#\/?/, "").split("/");
  return { screen: SCREENS.includes(screen) ? screen : "menu", param, from };
}

function render(route) {
  for (const screen of SCREENS) {
    document.getElementById(`screen-${screen}`).hidden = screen !== route.screen;
  }
  // A renderer returns false when it rejected the param and re-routed to the
  // menu; a hashchange is already queued, so don't move focus into a dead screen.
  if (route.screen === "category" && !renderCategory(route.param)) return;
  if (route.screen === "module" && !renderModule(route.param, route.from)) return;
  focusScreen(route.screen);
}

function navigate(screen, param, from) {
  const parts = [screen];
  if (param) parts.push(encodeURIComponent(param));
  if (from) parts.push(encodeURIComponent(from));
  location.hash = `/${parts.join("/")}`;
}

// Move focus to the top of whatever screen just appeared, so keyboard and
// screen-reader users land on the new page instead of the old one.
function focusScreen(screen) {
  if (screen === "menu") document.querySelector("#menu-nav .menu__item")?.focus();
  if (screen === "category") document.getElementById("category-title")?.focus();
  if (screen === "module") document.querySelector("#module-content .module-name")?.focus();
}

window.addEventListener("hashchange", () => render(currentRoute()));

// Any element carrying data-route navigates (back links, module rows, link-less
// buttons). Menu items are excluded — the menu has its own handler below.
document.addEventListener("click", (e) => {
  const target = e.target.closest("[data-route]");
  if (target && !target.classList.contains("menu__item")) {
    navigate(target.dataset.route, target.dataset.param, target.dataset.from);
  }
});

// ---- Main menu ----

function menuItemHtml(category, index) {
  const key = index < 9 ? String(index + 1) : "";
  const keyHtml = key ? `<span class="menu__key">${key}</span> ` : "";
  const keyAttr = key ? ` data-key="${key}"` : "";
  return `
    <button class="menu__item" type="button" data-route="category" data-param="${escapeAttr(category.id)}"${keyAttr}>
      ${keyHtml}${escapeHtml(category.icon)} ${escapeHtml(category.name)}
    </button>
  `;
}

function renderMenu() {
  const nav = document.getElementById("menu-nav");
  const intro = document.getElementById("menu-intro");
  const list = menuCategories();

  intro.textContent = `${BOOK.modules.length} module(s) inside. Choose a chapter.`;
  nav.innerHTML = list.map(menuItemHtml).join("");
}

function menuItems() {
  return [...document.querySelectorAll("#menu-nav .menu__item")];
}

function handleMenuAction(btn) {
  if (btn?.dataset.route) navigate(btn.dataset.route, btn.dataset.param);
}

function setupMenu() {
  const nav = document.getElementById("menu-nav");

  nav.addEventListener("click", (e) => {
    const btn = e.target.closest(".menu__item");
    if (btn) handleMenuAction(btn);
  });

  nav.addEventListener("keydown", (e) => {
    const items = menuItems();
    const idx = items.indexOf(document.activeElement);
    if (e.key === "ArrowDown") {
      e.preventDefault();
      items[(idx + 1 + items.length) % items.length]?.focus();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      items[(idx - 1 + items.length) % items.length]?.focus();
    }
  });

  // Number-key shortcuts 1-7, only while the menu screen is showing.
  document.addEventListener("keydown", (e) => {
    if (currentRoute().screen !== "menu") return;
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    const match = menuItems().find((btn) => btn.dataset.key === e.key);
    if (match) handleMenuAction(match);
  });
}

// ---- Category screen ----

function moduleRowHtml(module, categoryId) {
  return `
    <button class="module-list__item" type="button" data-route="module" data-param="${escapeAttr(module.id)}" data-from="${escapeAttr(categoryId)}">
      <span class="module-name">${escapeHtml(module.icon)} ${escapeHtml(module.name)}</span>
      <span class="module-summary">${escapeHtml(module.summary)}</span>
    </button>
  `;
}

function renderCategory(categoryId) {
  const titleEl = document.getElementById("category-title");
  const blurbEl = document.getElementById("category-blurb");
  const listEl = document.getElementById("category-list");
  const category = findCategory(categoryId);

  // Unknown category id: bounce back to the menu rather than show an empty page.
  if (!category) {
    navigate("menu");
    return false;
  }

  titleEl.textContent = `${category.icon ?? ""} ${category.name}`.trim();
  blurbEl.textContent = category.blurb ?? "";

  const modules = modulesInCategory(category.id);
  listEl.innerHTML = modules.length
    ? modules.map((m) => moduleRowHtml(m, category.id)).join("")
    : '<p class="module-summary">This chapter is empty for now.</p>';
  return true;
}

// Arrow keys walk the module list the same way they walk the menu.
document.getElementById("category-list").addEventListener("keydown", (e) => {
  if (e.key !== "ArrowDown" && e.key !== "ArrowUp") return;
  const items = [...document.querySelectorAll("#category-list .module-list__item")];
  const idx = items.indexOf(document.activeElement);
  if (idx === -1) return;
  e.preventDefault();
  const step = e.key === "ArrowDown" ? 1 : -1;
  items[(idx + step + items.length) % items.length]?.focus();
});

// ---- Module screen ----

function linkButtonHtml(link) {
  const url = safeUrl(link?.url);
  if (!url) return "";
  const icon = link.icon ? `${escapeHtml(link.icon)} ` : "";
  return `
    <a class="link-btn" href="${escapeAttr(url)}" target="_blank" rel="noopener noreferrer">
      ${icon}${escapeHtml(link.label ?? url)}
    </a>
  `;
}

function renderModule(moduleId, fromCategoryId) {
  const content = document.getElementById("module-content");
  const backBtn = document.getElementById("module-back");
  const module = findModule(moduleId);

  // Unknown module id: bounce back to the menu rather than show an empty page.
  if (!module) {
    navigate("menu");
    return false;
  }

  // The back link points at whichever chapter the visitor actually came
  // from (e.g. "All modules"), falling back to the module's own chapter
  // for a direct/bookmarked link that never went through a category screen.
  const parent = findCategory(fromCategoryId) ?? findCategory(module.category);
  backBtn.dataset.route = parent ? "category" : "menu";
  if (parent) {
    backBtn.dataset.param = parent.id;
    backBtn.textContent = `← Back to ${parent.name}`;
  } else {
    delete backBtn.dataset.param;
    backBtn.textContent = "← Back to the Contents";
  }

  const useCases = Array.isArray(module.useCases) ? module.useCases : [];
  const useCasesHtml = useCases.length
    ? `<ul class="use-cases">${useCases.map((u) => `<li>${escapeHtml(u)}</li>`).join("")}</ul>`
    : "";

  const links = Array.isArray(module.links) ? module.links : [];
  const linksHtml = links.map(linkButtonHtml).join("");

  content.innerHTML = `
    <h2 class="module-name" tabindex="-1">${escapeHtml(module.icon)} ${escapeHtml(module.name)}</h2>
    <p class="module-summary">${escapeHtml(module.summary)}</p>
    ${useCasesHtml}
    ${linksHtml ? `<div class="link-buttons">${linksHtml}</div>` : ""}
  `;
  return true;
}

// ---- Boot ----

// Returns an error string if the data file is missing or the wrong shape, else null.
function dataProblem(data) {
  if (!data || typeof data !== "object") return "data/modules.js did not load, so window.BOOK_DATA is missing.";
  if (!Array.isArray(data.categories) || !data.categories.length) return "window.BOOK_DATA.categories is missing or empty.";
  if (!Array.isArray(data.modules) || !data.modules.length) return "window.BOOK_DATA.modules is missing or empty.";
  return null;
}

function showFatalError(message) {
  for (const screen of SCREENS) {
    document.getElementById(`screen-${screen}`).hidden = screen !== "menu";
  }
  document.getElementById("menu-intro").textContent = "";
  document.getElementById("menu-nav").innerHTML = `
    <div role="alert">
      <h2 class="screen-heading" tabindex="-1">The book is empty</h2>
      <p class="module-summary">${escapeHtml(message)}</p>
      <p class="module-summary">Check that <code>data/modules.js</code> sits next to <code>index.html</code> and assigns <code>window.BOOK_DATA</code>.</p>
    </div>
  `;
  document.querySelector("#menu-nav .screen-heading")?.focus();
}

function main() {
  const problem = dataProblem(window.BOOK_DATA);
  if (problem) {
    showFatalError(problem);
    return;
  }

  BOOK = window.BOOK_DATA;
  document.getElementById("book-count").textContent =
    `${BOOK.modules.length} modules across ${BOOK.categories.length} chapters`;

  setupMenu();
  renderMenu();
  render(currentRoute());
}

main();
