import math
import pytest
from app.calculator import divide


def test_divide_small_nonzero_denominator_boundary():
    # Dividing by a very small non-zero value (precision stress)
    result = divide(1, 1e-12)
    assert math.isclose(result, 1e12, rel_tol=1e-9)


def test_divide_zero_numerator_boundary():
    assert divide(0, 5) == 0.0


def test_divide_negative_by_positive_boundary():
    assert divide(-10, 2) == -5.0


def test_divide_fraction_precision_boundary():
    assert math.isclose(divide(1, 3), 1/3, rel_tol=1e-12)


def test_divide_mixed_float_int_boundary():
    assert divide(3, 0.5) == 6.0
