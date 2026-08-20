import pytest

from py_simple_package.src.py_simple.easy_validator import (
    is_valid_email,
    is_valid_username,
    is_valid_zipcode,
    is_valid_url,
    is_password_secure)

class TestEasyValidator:

    @pytest.mark.parametrize(
    "email,expected",
    [
        ("mymail@gmail.com", True),
        ("email.com", False),
        ("", False),
        ("user@test.co", True),
        ("@gmail.com", False),
    ],
    )

    def test_email_validation(self, email, expected):
        assert is_valid_email(email) is expected

    @pytest.mark.parametrize(
        "username,expected",
        [
            ("user_name", True),
            ("user.name", False),
            ("user123", True),
            ("", False),
            ("user-name", False),
        ],
    )

    def test_username_validation(self, username, expected):
        assert is_valid_username(username) is expected

    @pytest.mark.parametrize(
            "zipcode,expected",
            [
                (12345, True),
                (1248721, False),
                (1234, False),
                (99999, True),
                ("01234", True),
            ],
        )

    def test_zipcode_validation(self, zipcode, expected):
        assert is_valid_zipcode(zipcode) is expected

    @pytest.mark.parametrize(
        "url, expected",
        [
            ("www.google.com", True),
            ("something.com", False),
            ("http://google.com", True),
            ("https://google.com", True),
            ("", False),
        ],
    )

    def test_url_validation(self, url, expected):
        assert is_valid_url(url) is expected

    @pytest.mark.parametrize(
        "password, expected",
        [
            ("1andkrf!AG5", True),
            ("111mskagowd", False),
            ("Ab1!cd", False),
            ("abcd12!ef", False),
            ("Abcdef!g1", False),
            ("Abcd12!!Ef", False),
            ("AAbcdef1!2", False),
            ("Abbcdef1!2", False),
            ("Abcdef11!2", False),
            (" 1andkrf!AG5", True),
            ("Abcde12!", False),
            ("", False),
        ],
    )

    def test_password_validation(self, password, expected):
        assert is_password_secure(password) is expected