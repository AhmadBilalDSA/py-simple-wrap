import re


def is_valid_email(email: str) -> bool:
    pattern = r'[a-zA-Z_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

