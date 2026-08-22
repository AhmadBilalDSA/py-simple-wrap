---
name: 🪄 [2-Minute Task] Add a reference page for {{MODULE_NAME}}
about: A module changed in a merged PR has no matching reference file
title: 🪄 [2-Minute Task] Add a reference page for {{MODULE_NAME}}
labels: documentation, good first issue, help wanted, good-first-issue, 5-minute-task, fast-task
---
`{{MODULE_NAME}}` doesn't have a reference page yet — and despite how this sounds,
it's genuinely one of the easiest issues in this whole project. Don't let the title scare you off!

**All you need to do:**

1. Create a new file at `docs/reference/{{MODULE_NAME}}.md`

2. Paste in this single line:
    ``` md 
    ::: py_simple.{{MODULE_NAME}}
    ```
   
3. That's it. [mkdocstrings](https://mkdocstrings.github.io/) automatically pulls in the
module's docstrings and builds the full page for you — no writing required.

4. Add a line for it in [`mkdocs.yml`](https://github.com/sara-czasak/py-simple-wrap/blob/main/mkdocs.yml)
   under the `Reference:` section, following the same format as the existing
   entries — e.g. `- Easy Colors: reference/easy_colors.md`.

Please read [CONTRIBUTING.md](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
before you start, and feel free to ask questions here!

**Links:**
- Module: [`{{MODULE_NAME}}.py`](https://github.com/sara-czasak/py-simple-wrap/blob/main/py_simple_package/src/py_simple/{{MODULE_NAME}}.py)
- Where it goes: [`docs/reference/`](https://github.com/sara-czasak/py-simple-wrap/tree/main/docs/reference)
- Example of an existing one: [`easy_colors.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/docs/reference/easy_colors.md)
- Contributing guide: [`CONTRIBUTING.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
- Tutorials for contributors: [`docs/contributor-hub`](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/)
