import pytest
from app.calculator import divide


def test_divide_by_zero_int_raises_value_error():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_float_raises_value_error():
    with pytest.raises(ValueError):
        divide(10.0, 0.0)


def test_divide_non_numeric_numerator_type_error():
    with pytest.raises(TypeError):
        divide("10", 2)


def test_divide_non_numeric_denominator_type_error():
    with pytest.raises(TypeError):
        divide(10, "2")


def test_divide_none_inputs_type_error():
    with pytest.raises(TypeError):
        divide(None, 1)
