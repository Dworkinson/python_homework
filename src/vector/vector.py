from __future__ import annotations

from math import hypot
from typing import Any


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._x = self._validate(x)
        self._y = self._validate(y)

    def _validate(self, value: Any) -> float:
        return float(value)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead.'
            )

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value: Any) -> None:
        self._x = self._validate(value)

    @y.setter
    def y(self, value: Any) -> None:
        self._y = self._validate(value)

    def __eq__(self, other: Vector) -> bool:
        self._check_type(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Vector) -> bool:
        return not self == other

    def __add__(self, other: Vector) -> Vector:
        self._check_type(other)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        self._check_type(other)
        return Vector(self.x - other.x, self.y - other.y)

    def __iadd__(self, other: Vector) -> Vector:
        self._check_type(other)
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other: Vector) -> Vector:
        self._check_type(other)
        self.x -= other.x
        self.y -= other.y
        return self

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def length(self) -> float:
        return hypot(self.x, self.y)
