from py_simple_package.src.py_simple.easy_validator import (
    is_valid_email,
    is_valid_username,
    is_valid_zipcode,
    is_valid_url,
    is_password_secure)

def test_valid_email():
    assert is_valid_email("mymail@gmail.com")

def test_not_valid_email():
    assert not is_valid_email("email.com")

def test_email_empty():
    assert not is_valid_email("")

def test_email_with_subdomain():
    assert is_valid_email("user@test.co")

def test_email_missing_username():
    assert not is_valid_email("@gmail.com")

def test_valid_username():
    assert is_valid_username("user_name")

def test_not_valid_username():
    assert not is_valid_username("user.name")

def test_username_numbers():
    assert is_valid_username("user123")

def test_username_empty():
    assert not is_valid_username("")

def test_username_dash():
    assert not is_valid_username("user-name")

def test_valid_zipcode():
    assert is_valid_zipcode(12345)

def test_not_valid_zipcode():
    assert not is_valid_zipcode(1248721)

def test_zipcode_too_short():
    assert not is_valid_zipcode(1234)

def test_zipcode_exact_five_digits():
    assert is_valid_zipcode(99999)

def test_zipcode_with_leading_zero():
    assert is_valid_zipcode("01234")

def test_valid_url():
    assert is_valid_url("www.google.com")

def test_not_valid_url():
    assert not is_valid_url("something.com")

def test_url_http():
    assert is_valid_url("http://google.com")

def test_url_https():
    assert is_valid_url("https://google.com")

def test_url_empty():
    assert not is_valid_url("")

def test_password_secure():
    assert is_password_secure("1andkrf!AG5")

def test_not_password_secure():
    assert not is_password_secure("111mskagowd")

def test_password_too_short():
    assert not is_password_secure("Ab1!cd")

def test_password_no_uppercase():
    assert not is_password_secure("abcd12!ef")

def test_password_no_special_character():
    assert not is_password_secure("Abcd1234ef")

def test_password_not_enough_digits():
    assert not is_password_secure("Abcdef!g1")

def test_password_repeated_characters():
    assert not is_password_secure("Abcd12!!Ef")