import pytest

from py_simple_package.src.py_simple.easy_strings import (
    count_words,
    is_alphanumeric,
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


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Something123", True),
        ("Python3", True),
        ("12345", True),
        ("abc", True),
        ("Hello World", False),
        ("hello!", False),
        ("user@email.com", False),
        ("", False),
    ],
)
def test_is_alphanumeric(text, expected):
    assert is_alphanumeric(text) is expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world! How are you?", 5),
        ("hello world", 2),
        ("one", 1),
        ("", 0),
        ("   ", 0),
        ("hello-world_again", 3),
        ("camelCaseText", 3),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected
