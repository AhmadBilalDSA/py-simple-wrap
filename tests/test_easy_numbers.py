import pytest
from py_simple_package.src.py_simple.easy_numbers import (
is_even,
is_evenly_divides
)
import random

def test_is_even():
    """ Should return True if the number is even and False otherwise. """
    random_number = random.randint(1, 100)
    assert is_even(random_number), \
        f'Number: {random_number}'


def test_is_evenly_divides():
    """ Should return True if the number is evenly divided by divisor """
    random_number = random.randint(1, 100)
    random_divisor = random.randint(1, 10)
    assert is_evenly_divides(random_number, random_divisor), \
        f"Number: {random_number}, Divisor: {random_divisor}"