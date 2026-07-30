import pytest

from py_simple.easy_strings import (
    is_palindrome,
    remove_extra_spaces,
    to_kebab_case,
    to_snake_case,
)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("  hello   world  ", "hello world"),
        ("hello world", "hello world"),
        ("", ""),
        ("   ", ""),
        ("hello\tworld\nagain", "hello world again"),
    ],
)
def test_remove_extra_spaces(text, expected):
    assert remove_extra_spaces(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello_world"),
        ("hello-world", "hello_world"),
        ("hello_world", "hello_world"),
        ("helloWorld", "hello_world"),
        ("  Multiple   Spaces  ", "multiple_spaces"),
        ("Python 3 Basics", "python_3_basics"),
    ],
)
def test_to_snake_case(text, expected):
    assert to_snake_case(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello-world"),
        ("hello_world", "hello-world"),
        ("hello-world", "hello-world"),
        ("helloWorld", "hello-world"),
        ("  Multiple   Spaces  ", "multiple-spaces"),
        ("Python 3 Basics", "python-3-basics"),
    ],
)
def test_to_kebab_case(text, expected):
    assert to_kebab_case(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("RaceCar", True),
        ("Never odd or even", True),
        ("A man, a plan, a canal: Panama!", True),
        ("hello", False),
        ("", True),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected
