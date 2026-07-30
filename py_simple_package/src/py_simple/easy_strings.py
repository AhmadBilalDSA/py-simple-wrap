"""Beginner-friendly helpers for common string operations."""

import re


def remove_extra_spaces(text: str) -> str:
    """
    Removes leading, trailing, and repeated spaces from text.

    Example:
        remove_extra_spaces("  hello   world  ")
        "hello world"
    """
    return " ".join(text.split())


def to_snake_case(text: str) -> str:
    """
    Converts text to snake_case.

    Example:
        to_snake_case("Hello World")
        "hello_world"
    """
    cleaned_text = _separate_words(text)
    return cleaned_text.lower().replace(" ", "_")


def to_kebab_case(text: str) -> str:
    """
    Converts text to kebab-case.

    Example:
        to_kebab_case("Hello World")
        "hello-world"
    """
    cleaned_text = _separate_words(text)
    return cleaned_text.lower().replace(" ", "-")


def is_palindrome(text: str) -> bool:
    """
    Returns True when text reads the same forwards and backwards.

    Spaces, punctuation, and letter casing are ignored.

    Example:
        is_palindrome("Never odd or even")
        True
    """
    cleaned_text = "".join(
        character.lower() for character in text if character.isalnum()
    )
    return cleaned_text == cleaned_text[::-1]


def _separate_words(text: str) -> str:
    """Normalizes common word separators and separates camel-case words."""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    text = re.sub(r"[_\-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    return remove_extra_spaces(text)
