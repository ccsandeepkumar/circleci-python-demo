"""
This file controls which test cases should run in CircleCI.
Edit this list and commit — CircleCI will automatically
execute ONLY these tests.
"""

SELECTED_TESTS = [
    "tests/test_calculator.py",
    # "tests/test_advanced_calculator.py",
    # "tests/test_login.py::test_valid_user",   # example (commented)
]


def get_tests():
    return SELECTED_TESTS


if __name__ == "__main__":
    for test in SELECTED_TESTS:
        print(test)

