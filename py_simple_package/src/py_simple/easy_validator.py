"""
easy_validator is built to simplify validation.
"""
import re
from string import punctuation


def is_valid_email(email: str) -> bool:
    """
        Returns true if email is valid.

        Arguments:
            email (str): email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.

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
            username (str): username to validate.

        Returns:
            bool: True if the username is valid, False otherwise.

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
            zipcode (int): US zipcode to validate.

        Returns:
            bool: True if the zip code is valid, False otherwise.

        Example:
            is_valid_zipcode(12345)
            (True)
            is_valid_zipcode(1248721)
            (False)
        """
    pattern = r'^[0-9]{5}$'
    return bool(re.fullmatch(pattern, str(zipcode)))


def is_valid_url(url: str) -> bool:
    """
        Returns true if url is valid.

        Arguments:
            url (str): URL to validate.

        Returns:
            bool: True if the URL is valid, False otherwise.

        Example:
            is_valid_url("www.google.com")
            (True)
            is_valid_url("something.com")
            (False)
        """
    pattern = r'(https://|http://|www\.)[a-zA-Z0-9]+\.[a-zA-Z]+'
    return bool(re.fullmatch(pattern, url))


def is_password_secure(password: str) -> bool:
    """
        Returns true if password is valid.

        Validation checks:
            - minimum length of 8 characters
            - at least one special character
            - at least one upper case letter
            - at least two lowercase letters
            - at least two digits
            - no repeating characters

        Arguments:
            password (str): password to validate.

        Returns:
            bool: True if the password meets all checks, False otherwise.

        Example:
            is_password_secure("1andkrf!AG5")
            (True)
            is_password_secure("111mskagowd")
            (False)
        """
    min_length = 8
    upper_letters = 0
    lower_letters = 0
    digits = 0
    special_characters = 0
    last_char = ''

    if len(password) > min_length:
        for char in password:
            if char.isdigit():
                digits += 1
                if char == last_char:
                    return False
                else:
                    last_char = char
            elif char.isalpha():
                if char.upper() == char:
                    upper_letters += 1
                    if char == last_char:
                        return False
                    else:
                        last_char = char
                elif char.lower() == char:
                    lower_letters += 1
                    if char == last_char:
                        return False
                    else:
                        last_char = char
            elif char in punctuation:
                special_characters += 1
                if char == last_char:
                    return False
                else:
                    last_char = char
            else:
                pass
        if (upper_letters >= 1 and lower_letters >= 2 and digits >= 2 and
                special_characters >= 1):
            return True
        else:
            return False
    else:
        return False
