import pytest

from py_simple_package.src.py_simple.easy_colors import (
    hex_to_rgb,
    is_valid_hex,
    rgb_to_hex,
)


@pytest.mark.parametrize(
    "hex_code, expected",
    [
        ("#FFFFFF", True),
        ("#ffffff", True),
        ("FFFFFF", True),
        ("ffffff", True),
        ("#FFF", True),
        ("#fff", True),
        ("FFF", True),
        ("fff", True),
        ("#000000", True),
        ("#123456", True),
        ("#abcDEF", True),
        ("123456", True),
        ("#GGGGGG", False),
        ("#12345", False),
        ("#1234567", False),
        ("xyz", False),
        ("", False),
        (None, False),
        (123456, False),
    ],
)
def test_is_valid_hex(hex_code, expected):
    assert is_valid_hex(hex_code) is expected


@pytest.mark.parametrize(
    "hex_code, expected",
    [
        ("#FFFFFF", (255, 255, 255)),
        ("#ffffff", (255, 255, 255)),
        ("FFFFFF", (255, 255, 255)),
        ("#000000", (0, 0, 0)),
        ("#00ff00", (0, 255, 0)),
        ("#123456", (18, 52, 86)),
        ("#FFF", (255, 255, 255)),
        ("fff", (255, 255, 255)),
        ("#000", (0, 0, 0)),
        ("f0a", (255, 0, 170)),
    ],
)
def test_hex_to_rgb_valid(hex_code, expected):
    assert hex_to_rgb(hex_code) == expected


@pytest.mark.parametrize(
    "invalid_hex",
    [
        "#GGGGGG",
        "#12345",
        "#1234567",
        "invalid",
        "",
        "1234567",
    ],
)
def test_hex_to_rgb_invalid(invalid_hex):
    with pytest.raises(ValueError):
        hex_to_rgb(invalid_hex)


@pytest.mark.parametrize(
    "r, g, b, expected",
    [
        (255, 255, 255, "#FFFFFF"),
        (0, 0, 0, "#000000"),
        (0, 255, 0, "#00FF00"),
        (18, 52, 86, "#123456"),
        (255, 0, 170, "#FF00AA"),
    ],
)
def test_rgb_to_hex_valid(r, g, b, expected):
    assert rgb_to_hex(r, g, b) == expected


@pytest.mark.parametrize(
    "r, g, b",
    [
        (-1, 0, 0),
        (0, 256, 0),
        (0, 0, 300),
        (-255, 0, 0),
    ],
)
def test_rgb_to_hex_out_of_range(r, g, b):
    with pytest.raises(ValueError):
        rgb_to_hex(r, g, b)


@pytest.mark.parametrize(
    "r, g, b",
    [
        ("255", 255, 255),
        (255, 255.0, 255),
        (True, 255, 255),
        (255, None, 255),
    ],
)
def test_rgb_to_hex_invalid_types(r, g, b):
    with pytest.raises(TypeError):
        rgb_to_hex(r, g, b)
