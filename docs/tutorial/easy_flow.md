# Easy Flow

Running Python files from other scripts can be useful when building tools, automation scripts, or simple workflows. The `easy_flow` module provides a simple helper that lets you execute Python files while handling errors in a clean and readable way.

## A small real-world example

Imagine you have a small automation project with different Python scripts. Instead of opening each file manually, you want to run them from a main program.

```python
from py_simple import run_py_file

run_py_file("backup.py")
```

Example output:

```text
RUNNING: backup.py
Backup completed successfully!
```

## What happened?

`run_py_file()` runs a Python file as if it was executed directly from the command line, making it easy to launch scripts from another program.

If something goes wrong while running the file, `easy_flow` catches the error and raises an `EasyFlowError` with a clear message instead of exposing different types of Python exceptions.

For example:

```python
from py_simple import run_py_file

run_py_file("broken_script.py")
```

Output:

```text
RUNNING: broken_script.py


ERROR: Something went wrong inside the script
```

## Why use these helpers?

Instead of writing the same execution logic and error handling every time, you can simply use:

```python
run_py_file("script.py")
```

This keeps your workflow automation simple, readable, and beginner-friendly while providing consistent error handling when running Python files.