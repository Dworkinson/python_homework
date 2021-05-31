from functools import reduce


class InvalidParameter(Exception):
    pass


def max5() -> int:
    values = input().strip().split(' ')
    if len(values) != 5:
        raise InvalidParameter()

    return max(map(int, values))


def factorial_recursion(n: int) -> int:
    if int(n) < 0:
        raise InvalidParameter()

    if n <= 1:
        return 1

    return factorial_recursion(n - 1) * n


def factorial(n: int) -> None:
    if int(n) < 0:
        raise InvalidParameter()

    if n <= 1:
        print(1)

    result = 2
    for i in range(3, n + 1):
        result *= i
    print(result)


def factorial2(n: int) -> None:
    if int(n) < 0:
        raise InvalidParameter()

    if n <= 1:
        print(1)
        return

    print(reduce(lambda x, y: x * y, range(2, n + 1)))


def array_abs(array) -> list:
    return [abs(elem) for elem in array]


def array_sum(array) -> int or float:
    return sum(array)
