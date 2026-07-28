"""
easy_validator is built to simplify validation.
"""
import re


def is_valid_email(email: str) -> bool:
    """
        Returns true if email is valid.

        Arguments:
            email (str) -- email adress to validate.

        Example:
            is_valid_email("mymail@gmail.com")
            (True)
            is_valid_email("email.com")
            (False)
        """
    pattern = r'[a-zA-Z_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+'
    return bool(re.fullmatch(pattern, email))


def is_valid_username(username: str) -> bool:
    """
        Returns true if username is valid.

        Arguments:
            username (str) -- username to validate.

        Example:
            is_valid_username("user_name")
            (True)
            is_valid_username("user.name")
            (False)
        """
    pattern = r'^[a-zA-Z0-9_]+'
    return bool(re.fullmatch(pattern, username))


def is_valid_zipcode(zipcode: int) -> bool:
    """
        Returns true if US zip code is valid.

        Arguments:
            zipcode (int) -- US zipcode to validate.

        Example:
            is_valid_zipcode("12345")
            (True)
            is_valid_zipcode("1248721")
            (False)
        """
    pattern = r'^[0-9]{5}$'
    return bool(re.fullmatch(pattern, str(zipcode)))


