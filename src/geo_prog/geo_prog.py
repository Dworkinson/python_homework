from typing import Any


def geo_prog(start: int, size: int, multiplier: float):
    def _validate_int(value: Any) -> int:
        return int(value)

    def _validate_float(value: Any) -> float:
        return float(value)

    _validate_int(start)
    _validate_int(size)
    _validate_float(multiplier)

    i = 1
    while i <= size:
        yield start

        start *= multiplier
        i += 1
