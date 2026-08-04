"""
easy_async is built to simplify asynchronous code execution.
"""

from concurrent.futures import ThreadPoolExecutor


class EasyAsyncError(Exception):
    """
    Raised when a py_simple async function fails to complete.

    Wraps the underlying error (an exception raised inside one of the
    functions being run, a thread pool failure, etc.) so py_simple
    functions can fail with one consistent, easy-to-read exception
    instead of a random builtin one.

    Args:
        message (str): Human-readable description of what went wrong.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def run_at_the_same_time(functions: list) -> list:
    """
    Runs multiple zero-argument functions at the same time and returns
    their results.

    Raises EasyAsyncError if any function raises an exception while
    running.

    Args:
        functions (list): Functions to run, each taking no arguments.

    Returns:
        list: A list of (name, result) tuples, one per function.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import run_at_the_same_time

            def add():
                return 1 + 1

            def sub():
                return 4 - 2

            run_at_the_same_time([add, sub])  # -> [("add", 2), ("sub", 2)]
            ```

        === "The Traditional Way"
            ```python
            from concurrent.futures import ThreadPoolExecutor

            def add():
                return 1 + 1

            def sub():
                return 4 - 2

            functions = [add, sub]
            results = []
            with ThreadPoolExecutor() as executor:
                tickets = [
                    (f.__name__, executor.submit(f)) for f in functions
                ]
                for name, ticket in tickets:
                    results.append((name, ticket.result()))
            ```
    """
    tickets = []
    results = []
    try:
        with ThreadPoolExecutor() as executor:
            for function in functions:
                ticket = executor.submit(function)
                tickets.append((function.__name__, ticket))
            for ticket in tickets:
                results.append((ticket[0], ticket[1].result()))
        return results
    except Exception as e:
        raise EasyAsyncError(f"\n\n\nERROR: {e}") from None