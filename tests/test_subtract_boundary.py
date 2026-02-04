import pytest
from app.calculator import subtract


def test_subtract_large_to_negative_boundary():
    assert subtract(-10**12, 10**12) == -(2 * 10**12)


def test_subtract_same_numbers_zero_boundary():
    assert subtract(10**9, 10**9) == 0


def test_subtract_float_precision_boundary():
    assert subtract(5.5, 2.2) == 3.3


def test_subtract_with_zero_boundary():
    assert subtract(0, 10**6) == -10**6


def test_subtract_minimal_difference_boundary():
    # Very small difference
    assert subtract(1.000000000001, 1.0) == 1e-12
