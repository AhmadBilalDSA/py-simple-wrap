"""
easy_numbers is built to simplify different types of number operations.
"""


def is_even(number: int) -> bool:
    """
        Returns true if the number is even and false if it is odd.

        Arguments:
            number (int): number to check if odd or even.

        Example:
            is_even(90)
            (True)
            is_even(67)
            (False)
        """
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """
        Returns true if the number is odd and false if it is even.

        Arguments:
            number (int): number to check if odd or even.

        Example:
            is_odd(90)
            (False)
            is_odd(67)
            (True)
        """
    return number % 2 == 1


def is_evenly_divisible(number: int, divisor: int) -> bool:
    """
        Returns true if the number can be evenly divided by divisor.

        Arguments:
            number (int): number to check if evenly divided by divisor.
            divisor (int): divisor to check if number can be
             evenly divided by divisor.

        Example:
            is_evenly_divisible(90, 9)
            (True)
            is_evenly_divisible(67, 2)
            (False)
        """
    return number % divisor == 0


def is_positive(number: int) -> bool:
    """
        Returns true if the number is positive and false if it is
        negative.

        Arguments:
            number (int): number to check if positive.

        Example:
            is_positive(90)
            (True)
            is_positive(-10)
            (False)
        """
    return number > 0


def is_negative(number: int) -> bool:
    """
        Returns true if the number is negative and false if it is
        positive.

        Arguments:
            number (int): number to check if negative.

        Example:
            is_negative(90)
            (False)
            is_negative(-10)
            (True)
        """
    return number < 0


def average(nums: list[float]) -> float:
    """
        Returns the average of a list of numbers.

        Arguments:
            nums (list[float]): list of numbers to average.

        Example:
            average([1.5, 2, 3])
            (2.17)
            average([3, 5, 2.3, 6.24])
            (4.13)
        """
    return float(f"{(sum(nums) / len(nums)):.2f}")


def is_prime(number: int) -> bool:
    """
        Returns true if the number is prime and false if it is.

        Arguments:
            number (int): number to check if prime.

        Example:
            is_prime(2)
            (True)
            is_prime(15)
            (False)
        """
    if number > 0:
        limit = int((number ** 0.5) + 1)
    else:
        return False
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


def percentage_of(number: int, percentage: float) -> float:
    """
        Returns percentage of number as a float.

        Arguments:
            number (int): number to get percentage of.
            percentage (float): percentage to get.
            Must be between 0 and 1 (e.g. 0.5, 0.75)

        Example:
            percentage_of(100, 0.5)
            (50.0)
            percentage_of(19, 0.4)
            (7.6)
        """
    return float(f"{(number * percentage):.2f}")
