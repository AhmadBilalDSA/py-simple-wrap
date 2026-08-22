---
name: 📔 [Documentation] Add a README module menu entry for {{MODULE_NAME}}
about: A module changed in a merged PR has no entry in the README's Module Menu
title: 📔 [Documentation] Add a README module menu entry for {{MODULE_NAME}}
labels: documentation, good first issue, help wanted, good-first-issue
---
`{{MODULE_NAME}}` doesn't have an entry in the README's Module Menu yet.

**What's needed:**

1. Pick a short, on-theme emoji for the module (see existing entries for examples).

2. Add a new section to `README.md` under `## 🛠️ Module Menu`, matching the structure
   of the other entries:
   - A `### <emoji> Easy X` heading
   - A collapsible `<details>` block with a one-line `<summary>` describing what the module does
   - A Markdown table listing each public function, what it does, and a short usage example
Use an existing entry as your template — e.g. the "Easy Flow" section is a good compact
one to copy the structure from.
   - 
Please read [CONTRIBUTING.md](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
before you start, and feel free to ask questions here!

**Links:**
- Module: [`{{MODULE_NAME}}.py`](https://github.com/sara-czasak/py-simple-wrap/blob/main/py_simple_package/src/py_simple/{{MODULE_NAME}}.py)
- Where it goes: [`README.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/README.md), under `## 🛠️ Module Menu`
- Contributing guide: [`CONTRIBUTING.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
