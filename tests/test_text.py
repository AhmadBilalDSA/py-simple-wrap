import pytest

from py_simple_package.src.py_simple.easy_text import (
    capitalize_title,
    count_digits,
    count_letters,
    extract_hashtags,
    mask_part,
    pluralize,
    remove_punctuation,
    reverse_words,
    truncate,
    word_frequency,
)


@pytest.mark.parametrize(
    "text, length, expected",
    [
        ("Hello world!", 5, "Hello…"),
        ("Hi", 5, "Hi"),
        ("12345", 5, "12345"),
        ("abcdef", 3, "abc…"),
        ("", 3, ""),
    ],
)
def test_truncate(text, length, expected):
    assert truncate(text, length) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, world!", "Hello world"),
        ("No punctuation here", "No punctuation here"),
        ("don't stop", "dont stop"),
        ("", ""),
    ],
)
def test_remove_punctuation(text, expected):
    assert remove_punctuation(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello world", "world Hello"),
        ("one", "one"),
        ("a b c", "c b a"),
        ("", ""),
    ],
)
def test_reverse_words(text, expected):
    assert reverse_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("the great gatsby", "The Great Gatsby"),
        ("hello WORLD", "Hello World"),
        ("", ""),
    ],
)
def test_capitalize_title(text, expected):
    assert capitalize_title(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello 123!", 5),
        ("abc", 3),
        ("!!!", 0),
        ("", 0),
    ],
)
def test_count_letters(text, expected):
    assert count_letters(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello 123!", 3),
        ("abc", 0),
        ("007", 3),
        ("", 0),
    ],
)
def test_count_digits(text, expected):
    assert count_digits(text) == expected


@pytest.mark.parametrize(
    "text, visible, expected",
    [
        ("1234567890", 4, "1234 ******"),
        ("1234567890", 2, "12 ********"),
        ("1234", 4, "1234"),
        ("abc", 10, "abc"),
        ("", 0, ""),
    ],
)
def test_mask_part(text, visible, expected):
    assert mask_part(text, visible) == expected


def test_mask_part_default_visible():
    assert mask_part("1234567890") == "1234 ******"


@pytest.mark.parametrize(
    "word, count, expected",
    [
        ("cat", 1, "cat"),
        ("cat", 3, "cats"),
        ("dog", 0, "dogs"),
        ("bus", 2, "buses"),
        ("class", 2, "classes"),
    ],
)
def test_pluralize(word, count, expected):
    assert pluralize(word, count) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Loving #python and #coding!", ["python", "coding"]),
        ("no tags here", []),
        ("#one #two #one", ["one", "two", "one"]),
        ("", []),
    ],
)
def test_extract_hashtags(text, expected):
    assert extract_hashtags(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("the cat and the dog", {"the": 2, "cat": 1, "and": 1, "dog": 1}),
        ("Hello hello", {"hello": 2}),
        ("", {}),
    ],
)
def test_word_frequency(text, expected):
    assert word_frequency(text) == expected
