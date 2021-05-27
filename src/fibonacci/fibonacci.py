from typing import Any


def fibonacci(index: int) -> int:
    '''Generate a fibonacci sequence'''
    def _index_validate(index: Any) -> int:
        return int(index)
    _index_validate(index)

    def _is_positive(index: int) -> bool:
        return index > 0

    first = 0
    second = 1
    if _is_positive(index):
        while index >= 0:
            value = first

            yield value
            first = second
            value += second
            second = value
            index -= 1
    else:
        while index <= 0:
            value = first

            yield value
            first = second
            value -= second
            second = value
            index += 1
