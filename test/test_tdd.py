import re
import pytest
from hypothesis import given, strategies as st
from src.tdd import *

def test_fizzbuzz():
    fizzbuzz(5) == 'Buzz'
    fizzbuzz(3) == 'Fizz'
    fizzbuzz(15) == 'FizzBuzz'
    fizzbuzz('lol') == 'You should give me an integer'
    fizzbuzz(7) == '7'


valid_password_strategy = st.from_regex(
    r'^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?])(?=.*\d.*\d)[A-Za-z\d!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]{8,}$',
    fullmatch=True
)

# Test valid passwords
@given(password=valid_password_strategy)
def test_valid_passwords(password):
    result = validate_password(password)
    assert result["is_valid"] is True, f"Password '{password}' should be valid but got errors: {result.get('errors', [])}"
    assert len(result.get("errors", [])) == 0


# Test property: Passwords shorter than 8 characters are invalid
@given(password=st.text(max_size=7))
def test_short_passwords_are_invalid(password):
    result = validate_password(password)
    assert result["is_valid"] is False
    assert "Password must be at least 8 characters" in result["errors"]


# Test property: Passwords without 2 numbers are invalid
@given(password=st.from_regex(r'^[A-Za-z!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]{8,}$|^[A-Za-z!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*\d[A-Za-z!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]*$', fullmatch=True))
def test_passwords_without_two_numbers_are_invalid(password):
    # Count digits to ensure we're actually testing passwords with less than 2 digits
    digit_count = sum(c.isdigit() for c in password)
    if digit_count < 2 and len(password) >= 8:  # Only check this requirement if password is long enough
        result = validate_password(password)
        assert result["is_valid"] is False
        assert "The password must contain at least 2 numbers" in result["errors"]


# Test property: Passwords without capital letters are invalid
@given(password=st.from_regex(r'^[a-z0-9!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]{8,}$', fullmatch=True))
def test_passwords_without_capital_letters_are_invalid(password):
    result = validate_password(password)
    assert result["is_valid"] is False
    assert "Password must contain at least one capital letter" in result["errors"]


# Test property: Passwords without special characters are invalid
@given(password=st.from_regex(r'^[A-Za-z0-9]{8,}$', fullmatch=True))
def test_passwords_without_special_characters_are_invalid(password):
    result = validate_password(password)
    assert result["is_valid"] is False
    assert "Password must contain at least one special character" in result["errors"]
