import json
import os


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


def save_json_data(filepath: str, data: dict) -> None:
    """
    Saves a dictionary to a JSON file. Raises an error if the file
    already exists, so you don't accidentally overwrite something.

    Args:
        filepath (str): Path to the JSON file to create.
        data (dict): The data to save.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import save_json_data

            save_json_data("config.json", {"name": "Sara"})
            ```

        === "The Traditional Way"
            ```python
            import json
            import os

            filepath = "config.json"
            if os.path.exists(filepath):
                print(f"File {filepath} already exists.")
            else:
                with open(filepath, "w") as json_file:
                    json.dump({"name": "Sara"}, json_file, indent=4)
            ```
    """
    if os.path.exists(filepath):
        raise EasyJsonError(f"\n\n\nERROR: File {filepath} already exists.")

    try:
        with open(filepath, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        raise EasyJsonError(f"\n\n\nERROR: {e}") from None
