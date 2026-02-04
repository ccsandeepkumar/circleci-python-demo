import pytest
from app.calculator import multiply


def test_multiply_large_values_boundary():
    # Big integer multiplication (Python handles arbitrary precision)
    assert multiply(10**8, 10**8) == 10**16


def test_multiply_by_zero_boundary():
    assert multiply(123456789, 0) == 0


def test_multiply_negative_and_positive_boundary():
    assert multiply(-10**6, 10**3) == -10**9


def test_multiply_float_boundary():
    assert multiply(2.5, 2) == 5.0


def test_multiply_string_repeat_boundary():
    # Python behavior: string * int repeats the string
    assert multiply("ab", 3) == "ababab"
