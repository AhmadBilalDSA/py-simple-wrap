# Build a Signup Validation Check

When people create an account, a program needs to check their details before
accepting them. This small command-line example combines the email, username,
and password helpers from `py_simple` into one clear signup check.

## What we are building

Imagine a community site where a new member enters an email address, a public
username, and a password. We will keep the checks together, then tell the
member whether their details can be accepted.

```python
from py_simple import is_password_secure, is_valid_email, is_valid_username


applicant = {
    "email": "maya@example.com",
    "username": "maya_dev",
    "password": "River!27Map",
}

checks = {
    "email": is_valid_email(applicant["email"]),
    "username": is_valid_username(applicant["username"]),
    "password": is_password_secure(applicant["password"]),
}

if all(checks.values()):
    print("Account details accepted")
else:
    for field, accepted in checks.items():
        if not accepted:
            print(f"Please update the {field}.")
```

Example output:

```text
Account details accepted
```

## Try an invalid detail

Changing a detail shows which part needs attention. Here the username contains
a hyphen, while `is_valid_username()` accepts letters, numbers, and
underscores.

```python
applicant["username"] = "maya-dev"

checks["username"] = is_valid_username(applicant["username"])

for field, accepted in checks.items():
    if not accepted:
        print(f"Please update the {field}.")
```

Example output:

```text
Please update the username.
```

## How the checks work

`is_valid_email()` confirms that the email has the expected address format.
`is_valid_username()` keeps usernames simple and predictable by allowing
letters, numbers, and underscores. `is_password_secure()` checks that a
password is long enough and includes uppercase letters, lowercase letters,
digits, and a special character without repeating adjacent characters.

Putting the results in a dictionary lets `all()` decide whether every check
passed, while the final loop can point to the exact detail that needs changing.
This keeps a beginner-friendly program readable without writing regular
expressions or password-counting logic by hand.
