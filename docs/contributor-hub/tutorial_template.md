# Tutorial Template

Each module gets at least one tutorial page under `docs/tutorial/`, added to the `Tutorial` section of `mkdocs.yml`'s nav. This is the narrative, "here's why you'd use this" companion to the auto-generated `Reference` page — it's hand-written, not pulled from docstrings.

Modeled on `docs/tutorial/easy_date_formatter.md`, which is a good reference example to open side-by-side while writing a new one.

## Structure

Copy this whole block and fill in the placeholders:

`````markdown
# <Module Display Name>

One or two sentences: what everyday problem does this module solve, and
what stdlib module is it built on? (Mirror the module docstring here,
but written for a reader, not a code comment.)

## A small real-world example

A short paragraph setting up a realistic scenario — not "here's every
function," but "here's a task you'd actually have."

````python
from py_simple import function_one, function_two

result = function_one(...)
````

Example output:

````text
<what actually prints, for real — run it and paste the real output>
````

## What happened?

One short paragraph per function used above, explaining what it does
in plain language. Cross-reference other functions in the module even
if they weren't in the main example, so the page covers the whole
module, not just the one demo.

## Why use these helpers?

Closing paragraph: what would the reader have had to do without this
module (stdlib-only), and why is the wrapped version better for a
beginner? Keep it short — this echoes the "Traditional Way" contrast
from the docstrings, at the module level instead of function level.
`````

## Rules of thumb

- **Example output must be real.** Run the code and paste the actual output — don't hand-write a plausible-looking result. `easy_date_formatter.md` uses real dates for this reason.
- **Lead with a scenario, not a function list.** "Imagine you're creating a report and want to display today's date..." is more useful than "This module has 12 functions, here they are."
- **Don't duplicate the Reference page.** The tutorial explains *why* and walks through *one coherent example*; it doesn't need to demonstrate every single function exhaustively — that's what the auto-generated Reference page (from docstrings) is for.
- **Keep tone consistent** with the rest of the docs: plain language, beginner-friendly, no jargon introduced without explanation.

## Wiring it into the nav

After writing `docs/tutorial/easy_<name>.md`, add it to `mkdocs.yml` under the `Tutorial` → `Module Tutorials` list, alphabetically among the existing entries.
