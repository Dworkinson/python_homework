import pytest

from factorial.factorial import factorial
from factorial.factorial import NegativeIntegerException


def test_factorial():
    test_generator = factorial(5)
    expected_results = [1, 1, 2, 6, 24, 120]

    for result in expected_results:
        assert next(test_generator) == result

    with pytest.raises(StopIteration):
        next(test_generator)


def test_factorial_exception():
    impossible_factorial = factorial(-2)
    with pytest.raises(NegativeIntegerException):
        next(impossible_factorial)
