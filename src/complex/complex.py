from __future__ import annotations

from math import hypot
from typing import Any


class Complex:
    def __init__(self, real: float = 0.0, imaginary: float = 0.0) -> None:
        self._real = self._validate(real)
        self._imaginary = self._validate(imaginary)

    def _validate(self, value: Any) -> float:
        return float(value)

    def _check_type(self, obj: Any) -> None:
        if not isinstance(obj, self.__class__):
            raise TypeError(
                f'arg should be of type {self.__class__.__name__}, got {obj.__class__.__name__} instead'
            )

    @property
    def real(self) -> float:
        return self._real

    @property
    def imaginary(self) -> float:
        return self._imaginary

    def __eq__(self, other: Complex) -> bool:
        self._check_type(other)
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other: Complex) -> bool:
        self._check_type(other)
        return not self == other

    def __add__(self, other: Complex) -> Complex:
        self._check_type(other)
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other: Complex) -> Complex:
        self._check_type(other)
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other: Complex) -> Complex:
        self._check_type(other)
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __iadd__(self, other: Complex) -> Complex:
        self._check_type(other)
        return self.__add__(other)

    def __isub__(self, other: Complex) -> Complex:
        self._check_type(other)
        return self.__sub__(other)

    def __imul__(self, other: Complex) -> Complex:
        self._check_type(other)
        return self.__mul__(other)

    def __abs__(self) -> float:
        return hypot(self.real, self.imaginary)

    def __str__(self) -> str:
        if self.imaginary < 0:
            return f'{self.real}{self.imaginary}i'
        else:
            return f'{self.real}+{self.imaginary}i'
