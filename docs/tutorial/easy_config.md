# Easy Config

GitHub Actions workflow files are easy to start and just as easy to leave
unfinished. `easy_config` creates a commented starter workflow file, so you
can focus on choosing when it runs and what jobs your project needs.

## A small real-world example

Imagine you have started a Python project and want a place to add automated
checks later. From your project root, create a workflow called `checks`:

```python
from pathlib import Path

from py_simple import gh_workflow_config

workflow = Path(".github/workflows/checks.yml")

gh_workflow_config("checks")

print(workflow.exists())
print("name: checks" in workflow.read_text(encoding="utf-8"))
```

Example output:

```text
True
True
```

## What happened?

`gh_workflow_config()` created the `.github/workflows` folder when it was
missing, copied the built-in starter template into `checks.yml`, and replaced
the template's workflow name with `checks`.

`Path()` points to the file that will be created. `exists()` confirms that the
file is there, and `read_text()` lets the example check that the workflow has
the expected name. If `checks.yml` already exists, `gh_workflow_config()`
leaves it unchanged.

## Working from a subfolder

If you run a setup script from a subfolder instead of the project root, pass
`at_root=False`. The helper finds the Git repository root and creates the
workflow there:

```python
from py_simple import gh_workflow_config

gh_workflow_config("checks", at_root=False)
```

## Why use these helpers?

Without this helper, you would need to create the `.github/workflows` folders,
copy a workflow skeleton, and remember the basic YAML structure yourself.
`gh_workflow_config()` gives you a commented starting point while still
leaving the trigger, permissions, and commands under your control.
