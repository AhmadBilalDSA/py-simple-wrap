# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.3.3] - 2026-08-17
### Added
- Added a Contributor Hub overview page (`docs/contributor-hub/index.md`) that helps beginners find the right template based on what they're stuck on, instead of landing on the first template page by default ([@sara-czasak](https://github.com/sara-czasak))
- Added a Custom Exception Template to the Contributor Hub, covering the codebase's `<Module>Error` pattern with a worked example ([@sara-czasak](https://github.com/sara-czasak))


## [0.3.2] - 2026-08-17
### Added
- Added `.github/dependabot.yml` to automate dependency updates for pip, npm, and GitHub Actions, with a 7-day cooldown on routine updates (security-alert-driven fixes bypass the cooldown) ([@sara-czasak](https://github.com/sara-czasak))
### Changed
- Bumped GitHub Actions in `pages.yml`/`publish.yml`: `actions/checkout` 4→7, `actions/setup-python` 4→7, `actions/upload-artifact` 4→7, `actions/download-artifact` 4→8, `actions/deploy-pages` 4→5 (Dependabot)
- Bumped `typescript` 5.9.3→7.0.2 and `@types/node` 22.20.1→26.2.0 in the Quest generator's `package.json` (Dependabot)
### Fixed
- Fixed a broken `Documentation` project URL in `pyproject.toml` — pointed at a malformed GitHub folder link that 404'd; now points at the live docs site (`https://sara-czasak.github.io/py-simple-wrap/docs/`) ([@sara-czasak](https://github.com/sara-czasak))
 

## [0.3.1] - 2026-08-17
### Added
- Re-included `easy_data_visualization` (`plot_data`) in the public API now that unit tests exist ([@HeaTTap](https://github.com/HeaTTap))
- Added a "Contributor Hub" docs section with copy-paste Docstring and Tutorial templates ([@sara-czasak](https://github.com/sara-czasak))
- Added a standalone landing page at the GitHub Pages root, linking out to Docs, Contributor Hub, and Contributors Quest ([@sara-czasak](https://github.com/sara-czasak))
- Added the `publish.yml` GitHub Actions workflow for manual PyPI releases ([@sara-czasak](https://github.com/sara-czasak))
### Changed
- Moved the docs site from the GitHub Pages root to `/docs/` to make room for the new landing page; updated `site_url` and internal README/CONTRIBUTING links accordingly ([@sara-czasak](https://github.com/sara-czasak))
- Reorganized README badges into two rows (explore vs. project status) and added Home/Contributor Hub/Contributors badges ([@sara-czasak](https://github.com/sara-czasak))
- Added a Contributor Hub callout to CONTRIBUTING.md pointing new contributors at the docstring/tutorial templates ([@sara-czasak](https://github.com/sara-czasak))

## [0.3.0] - 2026-08-16
### Added
- Contributor "quest" gamification system: guilds, badges, XP and achievement tracking ([@sara-czasak](https://github.com/sara-czasak))
- Added tutorials for `easy_validator`, `easy_regex`, `easy_numbers`, `easy_math`, `easy_lists`, `easy_json`, `easy_images`, `easy_stats` ([@Onion0121](https://github.com/Onion0121), [@Venkat4real](https://github.com/Venkat4real), killmeheaven, Boyeong24 — last two not currently listed in `.all-contributorsrc`)
-- Added `easy_numbers2.md`, `easy_math2.md`, `easy_json2.md` tutorial files ([@Onion0121](https://github.com/Onion0121)); renamed to resolve filename conflicts with other contributors' tutorials ([@sara-czasak](https://github.com/sara-czasak))
- Added Python 3.13/3.14 classifiers and CI matrix entries ([@jbsilva](https://github.com/jbsilva))
### Changed
- Replaced `pygame` with `pygame-ce` as the `easy_game` dependency for Python 3.14 wheel support ([@jbsilva](https://github.com/jbsilva))
- Restructured CONTRIBUTORS.md and added a contributor round table ([@sara-czasak](https://github.com/sara-czasak))
- Added new contributors (E4x7k, jbsilva, Venkat4real) to README/CONTRIBUTORS.md ([@sara-czasak](https://github.com/sara-czasak))
- Excluded `easy_data_visualization` (`plot_data`) from the public API and removed the `matplotlib` dependency until unit tests exist for it ([@sara-czasak](https://github.com/sara-czasak))
### Fixed
- Fixed typo in the Easy Json tutorial path in `mkdocs.yml` ([@sara-czasak](https://github.com/sara-czasak))
- Bug-fixing and optimization passes on the contributor-quest scripts/site ([@sara-czasak](https://github.com/sara-czasak))
- Added missing permissions to the pylint/tests CI workflows ([@sara-czasak](https://github.com/sara-czasak))

<details>
<summary>Day-by-day breakdown</summary>

#### 2026-08-14 – 2026-08-16
**📦 Released v0.3.0 (PYPI)**
- Continued quest-system development: achievement tracking, badge fixes, guild-name fixes, and several bug-fix passes across the generator script and site ([@sara-czasak](https://github.com/sara-czasak))
- Replaced `pygame` with `pygame-ce` for Python 3.14 support; added 3.13/3.14 classifiers and CI matrix entries ([@jbsilva](https://github.com/jbsilva))
- Added jbsilva as a contributor ([@sara-czasak](https://github.com/sara-czasak))
- Optimized quest scripts/site and updated the `contributor-quest` dependency lockfile ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-08-12
- Added `easy_numbers2.md`, `easy_math2.md`, `easy_json2.md` tutorial files; fixed a typo in the Easy Json tutorial path ([@sara-czasak](https://github.com/sara-czasak))
- Added easy_math tutorial (killmeheaven — not currently listed in `.all-contributorsrc`)
- Added easy_json tutorial (Boyeong24 — not currently listed in `.all-contributorsrc`)
- Added E4x7k as a contributor ([@sara-czasak](https://github.com/sara-czasak))
- Docs edit to `mkdocs.yml` ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-08-11
- Started a contributor "quest" gamification system: workflow, generator script, guilds/badges/XP libraries, and a companion site ([@sara-czasak](https://github.com/sara-czasak))
- Added tutorials for `easy_validator`, `easy_regex`, `easy_numbers`, `easy_math`, `easy_lists`, `easy_json`, `easy_images` ([@Onion0121](https://github.com/Onion0121))
- Added `easy_stats` and `easy_numbers` tutorials ([@Venkat4real](https://github.com/Venkat4real))
- Added `.github/scripts/update_contributors.py` and an update-contributors workflow, with follow-up bug fixes ([@sara-czasak](https://github.com/sara-czasak))
- Restructured CONTRIBUTORS.md and added a contributor round table ([@sara-czasak](https://github.com/sara-czasak))
- Added Venkat4real as a contributor ([@sara-czasak](https://github.com/sara-czasak))
- Added permissions to the pylint/tests CI workflows ([@sara-czasak](https://github.com/sara-czasak))
- Several README/`.all-contributorsrc` fixes ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-08-10
- Added tutorials for `easy_generator`, `easy_game`, `easy_file_manager`, `easy_dict`, `easy_date_formatter`, `easy_data_visualization`, `easy_csv`; alphabetized the tutorials/references list ([@Onion0121](https://github.com/Onion0121), [@sara-czasak](https://github.com/sara-czasak))
- Added tests for `easy_game` helpers ([@averyquinnhq](https://github.com/averyquinnhq))
- Added all suggested charts to `easy_data_visualization` ([@joaoprbrasil](https://github.com/joaoprbrasil))
- Compressed the emoji key into a dropdown menu in README, fixed emoji menu rendering, and added a module-author badge/key ([@sara-czasak](https://github.com/sara-czasak))
- Added João Pedro Brasil and thomsonl as contributors ([@sara-czasak](https://github.com/sara-czasak))
- Started CHANGELOG.md and labeled PyPI releases in it ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-08-04 – 2026-08-09
**📦 Released v0.2.0 (PYPI)**
- Added JSON flattening function and tests (`is_nested_json`, `flatten_json`) to `easy_json` ([@sara-czasak](https://github.com/sara-czasak), [@atiqur-rahman-pro](https://github.com/atiqur-rahman-pro))
- Added `easy_regex` module; tests added ([@sara-czasak](https://github.com/sara-czasak), [@Mlandvo](https://github.com/Mlandvo), [@gaoharimran29-glitch](https://github.com/gaoharimran29-glitch))
- Added `easy_lists` (11 helpers) and `easy_text` (10 helpers) modules, with tests and docs ([@ghostfix-pm](https://github.com/ghostfix-pm))
- Added `easy_csv` module with CSV helpers ([@qotique](https://github.com/qotique))
- Added `easy_colors` functions: `random_hex_color`/`is_light_color` ([@smirnov-danil](https://github.com/smirnov-danil)), `rgb_to_hsl`/`hsl_to_rgb` ([@SemTiOne](https://github.com/SemTiOne)), `hex_to_rgba`/`contrast_ratio` ([@gaoharimran29-glitch](https://github.com/gaoharimran29-glitch))
- Added `run_py_file_safe`, `time_it`, and `retry` to `easy_flow` ([@AureSerua](https://github.com/AureSerua)); added tests ([@thomsonl](https://github.com/thomsonl))
- Added `easy_images` module ([@vjymisal0](https://github.com/vjymisal0))
- Started `easy_game` module, added `check_if_quit` and mouse-press detection ([@sara-czasak](https://github.com/sara-czasak))
- Added `easy_dict`, `easy_math`, and `easy_stats` modules ([@SemTiOne](https://github.com/SemTiOne))
- Added `easy_generator` module and 3 new helper functions ([@sara-czasak](https://github.com/sara-czasak))
- Added initial `easy_data_visualization` module and did a modularization pass ([@joaoprbrasil](https://github.com/joaoprbrasil))
- Renamed `prime_factors` → `prime_factorization` (and its tests) ([@sara-czasak](https://github.com/sara-czasak))
- Added tutorials for `easy_flow`, `easy_async`, `easy_colors`, `easy_converter`, `easy_web` ([@Onion0121](https://github.com/Onion0121))
- Added async test scaffolding ([@AashiSrivastava411](https://github.com/AashiSrivastava411))
- Multiple bug-fixing passes across `easy_generator` and other modules ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-08-01 – 2026-08-03
- Added `count_words` function to `easy_strings` (Killbill584 — not currently listed in `.all-contributorsrc`)
- Added unit tests for `easy_strings` (`is_alphanumeric`, `count_words`, fixes #42) ([@atiqur-rahman-pro](https://github.com/atiqur-rahman-pro))
- Added `easy_colors` module for hex/RGB handling (#40) ([@HeaTTap](https://github.com/HeaTTap))
- Added `easy_json` module: `open_json`, `save_json_data`, `pretty_json`; tests added ([@sara-czasak](https://github.com/sara-czasak), [@atiqur-rahman-pro](https://github.com/atiqur-rahman-pro), [@matheusfrta](https://github.com/matheusfrta))
- Added `get_all_headers`, `get_meta_description`, custom exception to `easy_web`; tests added ([@sara-czasak](https://github.com/sara-czasak), [@atiqur-rahman-pro](https://github.com/atiqur-rahman-pro))
- Added `count_tags`, `get_tag_list`, `print_allowed_tags` to `easy_web`; README polish ([@ghostfix-pm](https://github.com/ghostfix-pm))
- Added `round_to_nearest`, `greatest_common_divisor`, `clamp` helpers; tests added ([@gaoharimran29-glitch](https://github.com/gaoharimran29-glitch), [@ghostfix-pm](https://github.com/ghostfix-pm))
- Started `easy_flow` module ([@sara-czasak](https://github.com/sara-czasak))
- Added `easy_strings` tutorial ([@Onion0121](https://github.com/Onion0121))
- Revised Code of Conduct and SECURITY.md for clarity ([@sara-czasak](https://github.com/sara-czasak))
- README overhaul: badges, consistency fixes, all-contributors bot setup ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-07-31
**📦 Released v0.1.1, v0.1.2, v0.1.3, v0.1.4 (PYPI)**
- Added unit tests for `easy_web` module (closes #15) ([@HeaTTap](https://github.com/HeaTTap))
- Added `get_page_title` and other new functions to `easy_web`, added unit test workflow ([@sara-czasak](https://github.com/sara-czasak))
- Refactored docs, started building the docs page, added GitHub Pages deployment workflow ([@sara-czasak](https://github.com/sara-czasak))
- Docstring/docs improvements and typo fixes across modules ([@sara-czasak](https://github.com/sara-czasak))
- Various bug fixes and mkdocs config fixes ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-07-23 – 2026-07-30
**📦 Released v0.1.0 (PYPI)**
- Started and expanded `easy_numbers` module (is_prime, percentage_of, fixed negative-number prime bug); tests added ([@sara-czasak](https://github.com/sara-czasak), [@jagjitkaur0000](https://github.com/jagjitkaur0000))
- Added fluid oz/ml conversions and other features to `easy_converter`; tests added ([@sara-czasak](https://github.com/sara-czasak), [@averyquinnhq](https://github.com/averyquinnhq))
- Started and expanded `easy_validator` module; tests added ([@sara-czasak](https://github.com/sara-czasak), [@gaoharimran29-glitch](https://github.com/gaoharimran29-glitch))
- Added `easy_strings` module ([@shivams786](https://github.com/shivams786))
- Added speed converters to `easy_converter` (closes #17) ([@sol4nki](https://github.com/sol4nki))
- Started `easy_web` module, added docstrings and request timeout ([@sara-czasak](https://github.com/sara-czasak))
- pyproject.toml expansion, comprehensive tests, and new utility functions ([@ghostfix-pm](https://github.com/ghostfix-pm))
- Enhanced Pylint CI workflow, added `.pylintrc` ([@sara-czasak](https://github.com/sara-czasak))
- Various README/CONTRIBUTORS.md updates ([@sara-czasak](https://github.com/sara-czasak))

#### 2026-07-21 – 2026-07-22
**📦 Initial version (v0.0.1) PYPI**
- Project scaffolding: initial commit, README, LICENSE, CONTRIBUTING.md, pyproject.toml ([@sara-czasak](https://github.com/sara-czasak))
- Added `easy_file_manager` functionality: read-to-list, remove file, rename file ([@sara-czasak](https://github.com/sara-czasak))
- Added `easy_date_formatter` module, made helper functions private ([@sara-czasak](https://github.com/sara-czasak))
- README formatting passes (headers, readability) ([@sara-czasak](https://github.com/sara-czasak))
- Prepared files for test coverage ([@sara-czasak](https://github.com/sara-czasak))

</details>

<br>