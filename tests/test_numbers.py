from py_simple_package.src.py_simple.easy_numbers import (
    is_even,
    is_evenly_divisible,
)


def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(5) is False


def test_is_even_with_zero():
    assert is_even(0) is True


def test_is_even_with_negative_even():
    assert is_even(-8) is True


def test_is_even_with_negative_odd():
    assert is_even(-7) is False


def test_is_evenly_divisible_true():
    assert is_evenly_divisible(10, 5) is True


def test_is_evenly_divisible_false():
    assert is_evenly_divisible(10, 3) is False


def test_is_evenly_divisible_by_one():
    assert is_evenly_divisible(99, 1) is True


def test_is_evenly_divisible_equal_numbers():
    assert is_evenly_divisible(8, 8) is True


def test_is_evenly_divisible_negative_number():
    assert is_evenly_divisible(-10, 5) is True


def test_is_evenly_divisible_negative_divisor():
    assert is_evenly_divisible(10, -5) is True


def test_is_evenly_divisible_both_negative():
    assert is_evenly_divisible(-10, -5) is True