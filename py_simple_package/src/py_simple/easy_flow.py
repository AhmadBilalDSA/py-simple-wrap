"""
easy_flow is built to simplify work flows
"""

import runpy


class EasyFlowError(Exception):
    """
    Raised when a Python file can't be run.

    Wraps the underlying error (missing file, bad permissions, an
    exception raised inside the file being run, etc.) so py_simple
    functions can fail with one consistent, easy-to-read exception
    instead of a random builtin one.

    Args:
        message (str): Human-readable description of what went wrong.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def run_py_file(filename: str):
    """
    Runs a Python file as if it were called directly from the command
    line (i.e. as `__main__`), using the current process.

    Args:
        filename (str): Path to the `.py` file to run.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import run_py_file

            run_py_file("script.py")
            ```

        === "The Traditional Way"
            ```python
            import runpy

            print("RUNNING: script.py")
            try:
                runpy.run_path("script.py")
            except Exception as e:
                print(f"Couldn't run the file: {e}")
            ```
    """
    print(f"RUNNING: {filename}")
    try:
        runpy.run_path(filename)
    except Exception as e:
        raise EasyFlowError(f"\n\n\nERROR: {e}") from None