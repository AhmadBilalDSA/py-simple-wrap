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
        === "The Py_simple Way"
            ```python
            from py_simple import is_valid_email

            if is_valid_email("hello@world.com"):
                print("Looks good!")
            ```

        === "The Traditional Way"
            ```python
            import re

            pattern = r'[a-zA-Z_.%+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z]+'
            if re.fullmatch(pattern, "hello@world.com"):
                print("Looks good!")
            ```
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
        === "The Py_simple Way"
            ```python
            from py_simple import is_valid_username

            result = is_valid_username("user_name")  # -> True
            ```

        === "The Traditional Way"
            ```python
            import re

            pattern = r'^[a-zA-Z0-9_]+'
            result = bool(re.fullmatch(pattern, "user_name"))
            ```
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
        === "The Py_simple Way"
            ```python
            from py_simple import is_valid_zipcode

            result = is_valid_zipcode(12345)  # -> True
            ```

        === "The Traditional Way"
            ```python
            import re

            pattern = r'^[0-9]{5}$'
            result = bool(re.fullmatch(pattern, str(12345)))
            ```
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
        === "The Py_simple Way"
            ```python
            from py_simple import is_valid_url

            result = is_valid_url("www.google.com")  # -> True
            ```

        === "The Traditional Way"
            ```python
            import re

            pattern = (r'(?:https?://(?:www\.)?|www\.)[a-zA-Z0-9-]+\.
            (?:(?:[a-zA-Z0-9-]+\.)*)?[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?'
            r'(?:/\S*)?')
            result = bool(re.fullmatch(pattern, "www.google.com"))
            ```
    """
    pattern = (
        r'(?:https?://(?:www\.)?|www\.)[a-zA-Z0-9-]+\.(?:(?:[a-zA-Z0-9-]+\.)*)?[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?'
        r'(?:/\S*)?')
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
        === "The Py_simple Way"
            ```python
            from py_simple import is_password_secure

            result = is_password_secure("1andkrf!AG5")  # -> True
            ```

        === "The Traditional Way"
            ```python
            from string import punctuation

            password = "1andkrf!AG5"
            min_length = 8
            upper_letters = 0
            lower_letters = 0
            digits = 0
            special_characters = 0
            last_char = ''
            result = False

            if len(password) > min_length:
                for char in password:
                    if char.isdigit():
                        digits += 1
                        if char == last_char:
                            result = False
                            break
                        last_char = char
                    elif char.isalpha():
                        if char.upper() == char:
                            upper_letters += 1
                            if char == last_char:
                                result = False
                                break
                            last_char = char
                        elif char.lower() == char:
                            lower_letters += 1
                            if char == last_char:
                                result = False
                                break
                            last_char = char
                    elif char in punctuation:
                        special_characters += 1
                        if char == last_char:
                            result = False
                            break
                        last_char = char
                else:
                    result = (
                        upper_letters >= 1 and lower_letters >= 2 and
                        digits >= 2 and special_characters >= 1
                    )
            ```
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