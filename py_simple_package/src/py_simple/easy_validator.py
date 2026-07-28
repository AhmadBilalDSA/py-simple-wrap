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
