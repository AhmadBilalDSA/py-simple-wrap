import pytest

from py_simple_package.src.py_simple.easy_regex import (
    extract_emails,
    extract_urls,
    extract_number_sequences,
    extract_numbers)

class TestEasyRegex:

    @pytest.mark.parametrize(
        "email,expected",
        [
            ("Hello john@gmail.com", ["john@gmail.com"]),
            ("john@gmail.com alice@yahoo.com", ["john@gmail.com", "alice@yahoo.com"]),
            ("Hello Everyone", []),
            ("", []),
            ("john.smith+work@gmail.com", ["john.smith+work@gmail.com"]),
            ("USER@EXAMPLE.COM", ["USER@EXAMPLE.COM"]),
            ("Duplicate a@test.com a@test.com", ["a@test.com", "a@test.com"]),
        ]
    )

    def test_extract_emails(self, email, expected):
        assert extract_emails(email) == expected

    @pytest.mark.parametrize(
        "urls,expected",
        [
            ("Visit https://www.example.com", ["https://www.example.com"]),
            ("Visit http://example.com", ["http://example.com"]),
            ("Visit www.example.org today", ["www.example.org"]),
            (
                "Go to https://google.com and www.github.com",
                ["https://google.com", "www.github.com"],
            ),
            ("", []),
            ("No links here", []),
            (
                "https://docs.python.org/3/library/re.html",
                ["https://docs.python.org/3/library/re.html"],
            ),
        ]
    )

    def test_extract_urls(self, urls, expected):
        assert extract_urls(urls) == expected

    @pytest.mark.parametrize(
        "number_sequence,expected",
        [
            ("IP: 192.168.1.1", ["192.168.1.1"]),
            ("Today is 04-08-2026", ["04-08-2026"]),
            ("Time: 14:32", ["14:32"]),
            ("Version v1.2.3", ["1.2.3"]),
            ("ID 123_456_789", ["123_456_789"]),
            (
                "Server 192.168.1.1 at 14:32 on 04-08-2026",
                ["192.168.1.1", "14:32", "04-08-2026"],
            ),
            ("Just number 123", ["123"]),
            ("", []),
            ("No sequences", []),
        ]
        )

    def test_extract_number_sequences(self, number_sequence, expected):
        assert extract_number_sequences(number_sequence) == expected

    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ("I have 3 cats and 12 fish", ["3", "12"]),
            ("12345", ["12345"]),
            ("Room42", ["42"]),
            ("Version 1.2.3", ["1", "2", "3"]),
            ("IP 192.168.1.1", ["192", "168", "1", "1"]),
            ("04-08-2026", ["04", "08", "2026"]),
            ("", []),
            ("No numbers here", []),
            ]
        )

    def test_extract_numbers(self, numbers, expected):
        assert extract_numbers(numbers) == expected
