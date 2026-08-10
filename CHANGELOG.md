# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).
## [0.2.0] - 2026-08-10
### Added
- Added tests for `easy_flow` ([@thomsonl](https://github.com/thomsonl))
- Added all suggestions charts to `easy_data_visualization` ([@joaoprbrasil](https://github.com/joaoprbrasil))
- Added tests for `easy_game` helpers ([@averyquinnhq](https://github.com/averyquinnhq))
- Added tutorials for `easy_csv`, `easy_data_visualization`, `easy_date_formatter`, `easy_dict` ([@Onion0121](https://github.com/Onion0121))
- Added module-author badge/key to README ([@sara-czasak](https://github.com/sara-czasak))
### Changed
- Compressed emoji key into a dropdown menu in README ([@sara-czasak](https://github.com/sara-czasak))
- Alphabetized tutorials/references list ([@sara-czasak](https://github.com/sara-czasak))
### Fixed
- Fixed emoji menu rendering in README ([@sara-czasak](https://github.com/sara-czasak))

<details>
<summary>Day-by-day breakdown</summary>

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