import json


class EasyJsonError(Exception):
    """
    Raised when a JSON file can't be opened or parsed.

    Wraps the underlying error (missing file, bad permissions, invalid
    JSON syntax, etc.) so py_simple functions can fail with one
    consistent, easy-to-read exception instead of a random builtin one.

    Args:
        message (str): Human-readable description of what went wrong.

    Example:
        try:
            open_json("missing.json")
        except EasyJsonError as e:
            print(e)
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def open_json(filepath: str) -> dict | None:
    """
    Opens a JSON file and returns its contents as a dictionary.

    Args:
        filepath (str): Path to the JSON file to open.

    Returns:
        dict | None: The parsed JSON contents as a dictionary.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import open_json

            data = open_json("config.json")
            print(data["name"])
            ```

        === "The Traditional Way"
            ```python
            import json

            try:
                with open("config.json") as json_file:
                    data = json.load(json_file)
                print(data["name"])
            except Exception as e:
                print(f"Couldn't read the file: {e}")
            ```
    """
    try:
        with open(filepath) as json_file:
            return json.load(json_file)
    except Exception as e:
        raise EasyJsonError(f"\n\n\nERROR: {e}") from None
