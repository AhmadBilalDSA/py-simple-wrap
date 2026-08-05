"""Beginner-friendly helpers for hex and RGB color handling."""

import re


def is_valid_hex(hex_code: str) -> bool:
    """
    Checks whether a string is a valid hex color code.

    Supports 3-digit and 6-digit hex color formats, with or without
    a leading '#' prefix.

    Args:
        hex_code (str): Color string to check.

    Returns:
        bool: True if hex_code is a valid hex color, False otherwise.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import is_valid_hex

            is_valid_hex("#FFFFFF")  # -> True
            is_valid_hex("fff")  # -> True
            is_valid_hex("invalid")  # -> False
            ```

        === "The Traditional Way"
            ```python
            import re

            hex_code = "#FFFFFF"
            cleaned = hex_code.lstrip("#")
            is_valid = len(cleaned) in (3, 6) and all(
                c in "0123456789abcdefABCDEF" for c in cleaned
            )
            ```
    """
    if not isinstance(hex_code, str):
        return False

    cleaned = hex_code.lstrip("#")
    if len(cleaned) not in (3, 6):
        return False

    return bool(re.fullmatch(r"[0-9a-fA-F]+", cleaned))


def hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
    """
    Converts a hex color code string to an (R, G, B) integer tuple.

    Supports 3-digit and 6-digit hex color codes with or without '#'.

    Args:
        hex_code (str): Hex color string to convert (e.g., "#FFFFFF" or "fff").

    Returns:
        tuple[int, int, int]: RGB values as (r, g, b) integers in range 0-255.

    Raises:
        ValueError: If hex_code is not a valid hex color.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import hex_to_rgb

            hex_to_rgb("#FFFFFF")  # -> (255, 255, 255)
            hex_to_rgb("00ff00")  # -> (0, 255, 0)
            ```

        === "The Traditional Way"
            ```python
            hex_code = "#FFFFFF".lstrip("#")
            if len(hex_code) == 3:
                hex_code = "".join(c * 2 for c in hex_code)
            r, g, b = tuple(int(hex_code[i : i + 2], 16) for i in (0, 2, 4))
            ```
    """
    if not is_valid_hex(hex_code):
        raise ValueError(f"Invalid hex color code: '{hex_code}'")

    cleaned = hex_code.lstrip("#")
    if len(cleaned) == 3:
        cleaned = "".join(character * 2 for character in cleaned)

    r = int(cleaned[0:2], 16)
    g = int(cleaned[2:4], 16)
    b = int(cleaned[4:6], 16)

    return r, g, b


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Converts (R, G, B) color values to a hex color string.

    Args:
        r (int): Red channel value (0 to 255).
        g (int): Green channel value (0 to 255).
        b (int): Blue channel value (0 to 255).

    Returns:
        str: Uppercase hex color string (e.g., "#FFFFFF").

    Raises:
        ValueError: If any channel is outside the 0-255 range.
        TypeError: If any channel is not an integer.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import rgb_to_hex

            rgb_to_hex(255, 255, 255)  # -> "#FFFFFF"
            rgb_to_hex(0, 128, 64)  # -> "#008040"
            ```

        === "The Traditional Way"
            ```python
            r, g, b = 255, 255, 255
            hex_code = f"#{r:02X}{g:02X}{b:02X}"
            ```
    """
    for name, val in [("r", r), ("g", g), ("b", b)]:
        if not isinstance(val, int) or isinstance(val, bool):
            raise TypeError(f"Color channel '{name}' must be an integer.")
        if not (0 <= val <= 255):
            raise ValueError(
                f"Color channel '{name}' must be between 0 and 255, got {val}."
            )

    return f"#{r:02X}{g:02X}{b:02X}"
