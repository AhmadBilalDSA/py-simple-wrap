from py_simple_package.src.py_simple.easy_numbers import (
    is_even,
    is_odd,
    is_evenly_divisible,
    is_positive,
    is_negative,
    average,
    is_prime,
    percentage_of,
)


# even


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



# odd


def test_is_odd_with_odd_number():
    assert is_odd(5) is True


def test_is_odd_with_even_number():
    assert is_odd(4) is False


def test_is_odd_with_zero():
    assert is_odd(0) is False


def test_is_odd_with_negative_odd():
    assert is_odd(-5) is True


def test_is_odd_with_negative_even():
    assert is_odd(-4) is False



# evenly_divisible


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


# positive


def test_is_positive_positive():
    assert is_positive(8) is True


def test_is_positive_negative():
    assert is_positive(-8) is False


def test_is_positive_zero():
    assert is_positive(0) is False



# negative


def test_is_negative_negative():
    assert is_negative(-8) is True


def test_is_negative_positive():
    assert is_negative(8) is False


def test_is_negative_zero():
    assert is_negative(0) is False


# average


def test_average_integers():
    assert average([2, 4, 6]) == 4.0


def test_average_floats():
    assert average([1.5, 2.5]) == 2.0


def test_average_single_number():
    assert average([5]) == 5.0


def test_average_negative_numbers():
    assert average([-2, -4]) == -3.0


def test_average_rounding():
    assert average([1, 2, 2]) == 1.67

# prime

def test_is_prime_two():
    assert is_prime(2) is True


def test_is_prime_three():
    assert is_prime(3) is True


def test_is_prime_composite():
    assert is_prime(9) is False


def test_is_prime_large_prime():
    assert is_prime(17) is True


def test_is_prime_one():
    assert is_prime(1) is False


def test_is_prime_zero():
    assert is_prime(0) is False




# percentage


def test_percentage_half():
    assert percentage_of(100, 0.5) == 50.0


def test_percentage_quarter():
    assert percentage_of(80, 0.25) == 20.0


def test_percentage_zero():
    assert percentage_of(100, 0) == 0.0


def test_percentage_decimal():
    assert percentage_of(19, 0.4) == 7.6