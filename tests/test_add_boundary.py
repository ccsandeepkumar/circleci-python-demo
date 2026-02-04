import pytest
from app.calculator import add


def test_add_boundary_large_integers():
    assert add(10**15, 10**15) == 2 * (10**15)


def test_add_negative_and_positive_boundary():
    assert add(-10**12, 10**12) == 0


def test_add_float_precision_boundary():
    # Checks precision with floats near machine precision scale
    assert add(1e-12, 1.0) == 1.000000000001


def test_add_zero_identity_boundary():
    assert add(0, 999999999999) == 999999999999


def test_add_type_concat_strings_boundary():
    # Python behavior: "+" concatenates strings
    assert add("Edge", "Case") == "EdgeCase"
