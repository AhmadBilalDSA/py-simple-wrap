"""
easy_generator helps generate things faster.
"""

import string
import random
import qrcode
import os


class EasyGeneratorError(Exception):
    """
    Raised when a value can't be generated.

    Wraps whatever the underlying operation raises internally (bad
    length/character counts, missing data, qrcode/PIL errors, etc.)
    so py_simple functions can fail with one consistent,
    easy-to-read exception instead of a random builtin or
    library-specific one.

    Args:
        message (str): Human-readable description of what went wrong.
        """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def generate_password(pass_length: int = 12, uppercase_chars: int = 2,
                      digit_chars: int = 2, special_chars: int = 2) -> str:
    """
    Generates a randomized password of a given length in one call,
    handling the character-pool selection, shuffling, and
    repeated-character checks every password generator needs, instead
    of writing that logic by hand each time.

    Args:
        pass_length (int, optional): Total number of characters in the
            generated password. Defaults to `12`.
        uppercase_chars (int, optional): Number of uppercase letters to
            include. Defaults to `2`.
        digit_chars (int, optional): Number of digits to include.
            Defaults to `2`.
        special_chars (int, optional): Number of punctuation characters
            to include. Defaults to `2`.

    Returns:
        str: The generated password, made up of lowercase letters,
            uppercase letters, digits, and special characters shuffled
            together, with no two identical characters placed next to
            each other. The number of lowercase letters is calculated
            as `pass_length - (uppercase_chars + digit_chars + special_chars)`.

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import generate_password

            password = generate_password(16, uppercase_chars=3, digit_chars=3, special_chars=3)
            ```

        === "The Traditional Way"
            ```python
            import string
            import random

            length = 16
            uppercase_chars = 3
            digit_chars = 3
            special_chars = 3
            lowercase_chars = length - (uppercase_chars + digit_chars + special_chars)

            chars = (
                [random.choice(string.ascii_lowercase) for _ in range(lowercase_chars)]
                + [random.choice(string.ascii_uppercase) for _ in range(uppercase_chars)]
                + [random.choice(string.digits) for _ in range(digit_chars)]
                + [random.choice(string.punctuation) for _ in range(special_chars)]
            )
            random.shuffle(chars)
            password = ''.join(chars)
            ```
    """
    lowercase_chars = (pass_length -
                       (special_chars + digit_chars + uppercase_chars))
    lower_chars = [random.choice(string.ascii_lowercase)
                   for _ in range(lowercase_chars)]
    upper_chars = [random.choice(string.ascii_uppercase)
                   for _ in range(uppercase_chars)]
    digit_chars = [random.choice(string.digits)
                   for _ in range(digit_chars)]
    special_chars = [random.choice(string.punctuation)
                     for _ in range(special_chars)]

    pass_chars = [i for i in lower_chars + upper_chars +
                  digit_chars + special_chars]

    all_clear = False
    last_char = None
    while not all_clear:
        random.shuffle(pass_chars)
        for char in pass_chars:
            if char == last_char:
                break
            else:
                last_char = char
        all_clear = True

    return ''.join(pass_chars)


def generate_qr_code(data_to_encode: str) -> None:
    """
    Generates a QR code image from the given data and saves it to disk
    in one call, handling the qrcode image creation and non-overwriting
    filename selection every QR code generator needs.

    Args:
        data_to_encode (str): The text or data to encode in the QR
            code (e.g. a URL, message, or other string).

    Returns:
        None: The QR code is saved directly to disk as
            `qrcode{num}.png`, where `num` is the smallest
            non-negative integer that does not collide with an
            existing file in the current directory.

    Raises:
        EasyGeneratorError: If `data_to_encode` is empty, or if the
            QR code image can't be created or saved (e.g. an
            underlying qrcode/PIL error).

    Example:
        === "The Py_simple Way"
            ```python
            from py_simple import generate_qr_code

            generate_qr_code("https://example.com")
            ```

        === "The Traditional Way"
            ```python
            import qrcode
            import os

            data = "https://example.com"
            img = qrcode.make(data)

            num = 0
            while os.path.exists(f'qrcode{num}.png'):
                num += 1
            img.save(f'qrcode{num}.png')
            ```
    """
    if not data_to_encode:
        raise EasyGeneratorError("You need to provide some data to encode")
    try:
        img = qrcode.make(data_to_encode)

        num = 0
        good_filename = False
        while not good_filename:
            if os.path.exists(f'qrcode{num}.png'):
                num += 1
            else:
                good_filename = True
        img.save(f'qrcode{num}.png')
    except Exception as e:
        raise EasyGeneratorError(f"\n\n\nERROR: {e}")
