---
name: 📝 [Documentation] Add a tutorial page for {{MODULE_NAME}}
about: A module changed in a merged PR has no matching tutorial file
title: 📝 [Documentation] Add a tutorial page for {{MODULE_NAME}}
labels: documentation, good first issue, help wanted, good-first-issue
---
`{{MODULE_NAME}}` doesn't have a tutorial page yet.

Please add a short tutorial page demonstrating 2-3 functions used together in a realistic
mini-example.

Match the tone and structure of the existing tutorials in [`docs/tutorial/`](https://github.com/sara-czasak/py-simple-wrap/tree/main/docs/tutorial) (e.g.
[`easy_colors.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/docs/tutorial/easy_colors.md)) — a short intro, a small real-world example, a "What happened?"
breakdown, and a "Why use these helpers?" closer. Here is a guide on how to write module tutorials: [Contributor Hub](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/tutorial_template/)

Once it's written, also add a line for it in [`mkdocs.yml`](https://github.com/sara-czasak/py-simple-wrap/blob/main/mkdocs.yml)
under `Tutorial: > Module Tutorials:`, following the same format as the existing
entries — e.g. `- Easy Colors: tutorial/easy_colors.md`.

Please read [CONTRIBUTING.md](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md) before you start, and feel free to ask questions here!

**Links:**
- Module to document: [`{{MODULE_NAME}}.py`](https://github.com/sara-czasak/py-simple-wrap/blob/main/py_simple_package/src/py_simple/{{MODULE_NAME}}.py)
- Where the tutorial goes: [`docs/tutorial/`](https://github.com/sara-czasak/py-simple-wrap/tree/main/docs/tutorial)
- Contributing guide: [`CONTRIBUTING.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
- Tutorials for contributors: [`docs/contributor-hub`](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/)