"""
easy_generator helps generate things faster.
"""

import string
import random


def generate_password(pass_length: int = 12, uppercase_chars: int = 2,
                      digit_chars: int = 2, special_chars: int = 2) -> str:

    lowercase_chars = (pass_length -
                       (special_chars + digit_chars + uppercase_chars))
    lower_chars = [random.choice(string.ascii_lowercase) for _ in range(lowercase_chars)]
    upper_chars = [random.choice(string.ascii_uppercase) for _ in range(uppercase_chars)]
    digit_chars = [random.choice(string.digits) for _ in range(digit_chars)]
    special_chars = [random.choice(string.punctuation) for _ in range(special_chars)]

    pass_chars = [i for i in lower_chars + upper_chars + digit_chars + special_chars]

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


print(generate_password())
