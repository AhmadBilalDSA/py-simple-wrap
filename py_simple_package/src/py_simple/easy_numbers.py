"""
easy_numbers is built to simplify different types of number operations.
"""


def is_even(number: int) -> bool:
    """
        Returns true if the number is even and false if it is odd.

        Arguments:
            number (int) -- number to check if odd or even.

        Example:
            is_even(90)
            (true)
            is_even(67)
            (false)
        """
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """
        Returns true if the number is odd and false if it is even.

        Arguments:
            number (int) -- number to check if odd or even.

        Example:
            is_odd(90)
            (false)
            is_odd(67)
            (true)
        """
    return number % 2 == 1


def is_evenly_divisible(number: int, divisor: int) -> bool:
    """
        Returns true if the number can be evenly divided by divisor.

        Arguments:
            number (int) -- number to check if evenly divided by divisor.
            divisor (int) -- divisor to check if number can be
             evenly divided by divisor.

        Example:
            is_evenly_divisible(90, 9)
            (true)
            is_evenly_divisible(67, 2)
            (false)
        """
    return number % divisor == 0


def is_positive(number: int) -> bool:
    """
        Returns true if the number is positive and false if it is
        negative.

        Arguments:
            number (int) -- number to check if positive.

        Example:
            is_positive(90)
            (true)
            is_positive(-10)
            (false)
        """
    return number > 0


def is_negative(number: int) -> bool:
    """
        Returns true if the number is negative and false if it is
        positive.

        Arguments:
            number (int) -- number to check if negative.

        Example:
            is_negative(90)
            (false)
            is_negative(-10)
            (true)
        """
    return number < 0


def average(nums: list[float]) -> float:
    """
        Returns the average of a list of numbers.

        Arguments:
            nums (list[float]) -- list of numbers to average.

        Example:
            average([1.5, 2, 3])
            (2.17)
            average([3, 5, 2.3, 6.24])
            (4.13)
        """
    return float(f"{(sum(nums) / len(nums)):.2f}")


def is_prime(number: int) -> bool:
    limit = int((number ** 0.5) + 1)
    prime = True
    if number < 2:
        return False
    elif number == 2:
        return True
    elif is_even(number):
        return False
    else:
        for i in range(3, limit, 2):
            if is_evenly_divisible(number, i):
                return False
    return True

