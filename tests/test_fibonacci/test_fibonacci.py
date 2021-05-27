import pytest

from fibonacci.fibonacci import fibonacci


@pytest.mark.parametrize('index, expected_values', [
    (5, [0, 1, 1, 2, 3, 5]), (-5, [0, 1, -1, 2, -3, 5]), (0, [0])
])
def test_positive_fibonacci_sequence(index, expected_values):
    test_generator = fibonacci(index)
    test_values = []

    for value in test_generator:
        test_values.append(value)

    assert test_values == expected_values

    with pytest.raises(StopIteration):
        next(test_generator)
