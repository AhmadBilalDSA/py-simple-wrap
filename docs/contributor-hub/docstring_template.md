# Docstring Template

Every public function in `py-simple-wrap` should have a docstring in this shape. It's Google-style (matching `mkdocs.yml`'s `docstring_style: google` setting for `mkdocstrings`), plus a "Py_simple Way vs. Traditional Way" example block that's specific to this project.

## Module-level docstring

Every module file starts with a short docstring explaining what it wraps and why:

```python
"""
easy_<name> is meant to simplify <what it does>.
Built on top of the <stdlib module> module — no more <the pain point>.
"""
```

See `easy_date_formatter.py:1-4` for a real example.

## Function-level docstring

Copy this whole block and fill in the placeholders:

````python
def function_name(arg_one: str, arg_two: int = 0) -> str:
    """
    One-line summary of what the function returns, written in the third
    person ("Returns the ...", "Calculates a ...").

    Args:
        arg_one (str): What this argument means.
        arg_two (int): What this argument means. Mention the default
            if it's not obvious from the signature.

    Returns:
        str: What the return value looks like, with a concrete example
            (e.g., 'Monday, July 20, 2026').

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import function_name

            result = function_name("hello", 7)
            ```

        === "The Traditional Way"
            ```python
            # Show the stdlib-only equivalent here, so readers see
            # exactly what py-simple-wrap is saving them from.
            ```
    """
````

## Rules of thumb

- **Args/Returns are required** if the function takes arguments or returns something — skip the section entirely if it doesn't apply (see `list_available_formats()` in `easy_date_formatter.py`, which has no `Args:` block).
- **Always include an Example block** with both tabs. This is non-negotiable per `CONTRIBUTING.md`'s coding style section ("Always include Docstrings with an example").
- **The "Traditional Way" tab should be honest** — show what a developer would actually have to write without this package (e.g., raw `strftime` codes), not a strawman.
- **Private helper functions** (prefixed `_`, like `_format_date`) can use a single-line docstring — they don't need the full Args/Returns/Example treatment since they're not part of the public API `mkdocstrings` renders.
- Keep examples runnable and consistent with what the function actually returns — copy-paste them into a REPL to check before submitting.

## Where this gets used

Docstrings written this way are what `mkdocstrings` (configured in `mkdocs.yml`) renders automatically into the `Reference` section of the docs site — there's no separate reference doc to hand-write. Writing a good docstring *is* writing the reference documentation.
