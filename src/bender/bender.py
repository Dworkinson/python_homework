from functools import reduce


class InvalidParameter(Exception):
    pass


def max5():
    values = input().strip().split(' ')
    if len(values) != 5:
        raise InvalidParameter()

    return max(map(int, values))


def factorial_recursion(n):
    if n < 0:
        raise InvalidParameter()

    if n <= 1:
        return 1

    return factorial_recursion(n - 1) * n


def factorial(n):
    if n < 0:
        raise InvalidParameter()

    if n <= 1:
        print(1)

    result = 2
    for i in range(3, n+1):
        result *= i
    print(result)


def factorial2(n):
    if n < 0:
        raise InvalidParameter()

    if n <= 1:
        print(1)

    print(reduce(lambda x, y: x * y, range(2, n+1)))


def array_abs(array):
    return [abs(elem) for elem in array]


def array_sum(array):
    return sum(array)
