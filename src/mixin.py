class Number:
    validator = None

    def __init__(self, value=0):
        self._value = self.validator(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.validator(value)

    def __str__(self):
        return f'{self.validator.__name__}({self.value})'


class AbsoluteValueMixin:
    def abs(self):
        if self.value < 0:
            return self.value * -1
        return self.value


class Integer(Number):
    validator = int


class AbsInteger(Integer, AbsoluteValueMixin):
    pass


class Float(Number):
    validator = float


if __name__ == '__main__':
    i = AbsInteger(-1)
    print(i)
    print(i.abs())
