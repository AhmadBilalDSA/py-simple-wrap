from py_simple_package.src.py_simple.easy_regex import (
    extract_emails,
    extract_urls,
    extract_number_sequences,
    extract_numbers
)

import pytest

@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("this is my address, ginny@gmail.com", True)
    ]
)