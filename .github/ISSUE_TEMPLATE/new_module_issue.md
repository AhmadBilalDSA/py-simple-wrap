---
name: 🖋️ Want to add a module to py-simple-wrap?
about: New module idea
title: 🖋️ Want to add a module to py-simple-wrap?
labels: good first issue, help wanted, good-first-issue
---
`py-simple-wrap` is a collection of beginner-friendly Python wrappers that make common tasks easier — things like `easy_file_manager` and `unit_converter`.
 
If you've got an idea for a module (or want to extend an existing one with a new function), go ahead and open a PR! I'll review it and merge if it's a good fit.
 
### A few guidelines to keep things consistent
 
- **Keep it beginner-friendly.** The whole point of py-simple-wrap is that someone new to Python can use it without fighting boilerplate.
- **API style:** separate, clearly named functions first (e.g. `miles_to_km()`, not a generic `convert()` dispatcher). Dispatcher patterns can come later if it makes sense.
- **Import style:** modules should work as `from py_simple.your_module import your_function`.
- **Docstrings:** a short description of what the function does and an example if it's not obvious, here is a [GUIDE](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/docstring_template/) with docstring templates.

-  Make sure to read [CONTRIBUTING.md](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md) before you start!
- Not sure if your idea fits? Open a PR anyway or start a discussion here — happy to talk it through.

Looking forward to seeing what people come up with!

**Links:**
- Contributing tutorials [(docstrings, templates, exceptions)](https://sara-czasak.github.io/py-simple-wrap/docs/contributor-hub/)
- Where it goes: [`README.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/README.md), under `## 🛠️ Module Menu`
- Contributing guide: [`CONTRIBUTING.md`](https://github.com/sara-czasak/py-simple-wrap/blob/main/CONTRIBUTING.md)
