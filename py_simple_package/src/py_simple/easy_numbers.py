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


def is_evenly_divides(number: int, divisor: int) -> bool:
    """
        Returns true if the number can be evenly divided by divisor.

        Arguments:
            number (int) -- number to check if evenly divided by divisor.
            divisor (int) -- divisor to check if number can be
             evenly divided by divisor.

        Example:
            is_evenly_divides(90, 9)
            (true)
            is_even(67, 2)
            (false)
        """
    return number % divisor == 0
