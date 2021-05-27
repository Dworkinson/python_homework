from typing import Any


class NegativeIntegerException(Exception):
    pass


def factorial(index: int) -> int:
    def _validate(index: Any) -> int:
        return int(index)

    if (_validate(index)) < 0:
        raise NegativeIntegerException

    value = 1
    _next = 1

    while index >= 0:
        yield value
        value *= _next
        _next += 1
        index -= 1
