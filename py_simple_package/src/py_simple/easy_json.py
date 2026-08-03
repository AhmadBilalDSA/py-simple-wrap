"""
easy_json is built to simplify working with json files
"""

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


def pretty_json(data: dict = None, filepath: str = None) -> str | None:
    """
    Returns a pretty-printed, indented JSON string from a dictionary or
    a JSON file. Provide exactly one of `data` or `filepath` — not both.

    Args:
        data (dict): A dictionary to format as pretty-printed JSON.
        filepath (str): Path to a JSON file to load and format as
            pretty-printed JSON.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import pretty_json

            print(pretty_json(data={"name": "Sara"}))
            ```

        === "The Traditional Way"
            ```python
            import json

            print(json.dumps({"name": "Sara"}, indent=2))
            ```
    """
    if data is None and filepath is None:
        raise EasyJsonError("\n\n\nERROR: Either data or filepath "
                            "must be provided.") from None
    if data is not None and filepath is not None:
        raise EasyJsonError(f"\n\n\nERROR: Please provide data OR "
                            f"filepath.") from None
    elif data:
        return json.dumps(data, indent=2)
    else:
        try:
            d = open_json(filepath)
            return json.dumps(d, indent=2)
        except Exception as e:
            raise EasyJsonError(f"\n\n\nERROR: {e}") from None


def update_json(filepath: str, new_data: dict) -> None:
    """
    Updates a JSON file with new data, merging it into what's already
    there. Existing top-level keys in `new_data` overwrite matching keys
    in the file; anything else in the file is left untouched.

    Args:
        filepath (str): Path to the JSON file to update.
        new_data (dict): The data to merge into the existing file.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import update_json

            update_json("config.json", {"name": "Sara"})
            ```

        === "The Traditional Way"
            ```python
            import json

            with open("config.json") as json_file:
                data = json.load(json_file)

            data.update({"name": "Sara"})

            with open("config.json", "w") as json_file:
                json.dump(data, json_file, indent=4)
            ```
    """
    try:
        old_data = open_json(filepath)
        old_data.update(new_data)
        with open(filepath, "w") as json_file:
            json.dump(old_data, json_file, indent=4)
    except Exception as e:
        raise EasyJsonError(f"\n\n\nERROR: {e}") from None


def is_json_file(filepath: str) -> bool:
    """
    Checks whether a filepath points to an existing file with a `.json`
    extension.

    Args:
        filepath (str): Path to check.

    Returns:
        bool: True if the file exists and ends in `.json`, False otherwise.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import is_json_file

            if is_json_file("config.json"):
                print("Looks good!")
            ```

        === "The Traditional Way"
            ```python
            import os

            filepath = "config.json"
            if os.path.isfile(filepath) and filepath.split(".")[-1] == "json":
                print("Looks good!")
            ```
    """
    is_file = os.path.isfile(filepath)
    if is_file:
        if filepath.split(".")[-1] == "json":
            return True
        else:
            return False
    else:
        return False
