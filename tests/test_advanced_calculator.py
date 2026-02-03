import pytest
from app.calculator import add, subtract, multiply, divide


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_subtract_negative():
    assert subtract(-5, -3) == -2


def test_multiply_zero():
    assert multiply(5, 0) == 0


def test_divide_float():
    assert divide(7, 2) == 3.5
