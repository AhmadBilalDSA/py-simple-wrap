import pytest

from py_simple_package.src.py_simple.easy_colors import (
    hex_to_rgb,
    is_valid_hex,
    rgb_to_hex,
    random_hex_color,
    is_light_color,
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


def test_random_hex_color():
    assert is_valid_hex(random_hex_color())


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
        ("#F0F0F0", True),
        ("#E0E0E0", True),
        ("#FFEEEE", True),
        ("#EEFFEE", True),
        ("#EEEEFF", True),
        ("#000000", False),
        ("#121212", False),
        ("#1A1A1A", False),
        ("#333333", False),
        ("#000080", False),
        ("#006400", False),
        ("#8B0000", False),
        ("#808080", True),
        ("#7F7F7F", True),
        ("#858585", True),
    ],
)
def test_is_light_color(hex_code, expected):
    assert is_light_color(hex_code) == expected


@pytest.mark.parametrize(
    "hex_code, threshold, expected",
    [
        ("#808080", 0.15, True),
        ("#808080", 0.20, True),
        ("#808080", 0.179, True),
        ("#FFFFFF", 0.5, True),
        ("#FFFFFF", 0.9, True),
        ("#000000", 0.01, False),
        ("#000000", 0.0, False),
        ("#333333", 0.05, False),
        ("#333333", 0.10, False),
    ],
)
def test_is_light_color_with_threshold(hex_code, threshold, expected):
    assert is_light_color(hex_code, threshold=threshold) == expected


def test_is_light_color_invalid_hex():
    with pytest.raises((ValueError, IndexError)):
        is_light_color("#GGGGGG")

    with pytest.raises((ValueError, IndexError)):
        is_light_color("#12345")

    with pytest.raises((ValueError, IndexError)):
        is_light_color("#1234567")


def test_is_light_color_edge_cases():
    assert is_light_color("#FFF") == is_light_color("#FFFFFF")
    assert is_light_color("#000") == is_light_color("#000000")
    assert is_light_color("#ABC") == is_light_color("#AABBCC")

    assert is_light_color("#AbCdEf") == is_light_color("#ABCDEF")

    assert is_light_color("#FF0000")
    assert is_light_color("#00FF00")
    assert not is_light_color("#0000FF")
