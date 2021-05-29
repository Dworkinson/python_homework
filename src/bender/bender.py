def max_5():
    values = []
    values.append(float(input('Enter a number\n')))
    values.append(float(input('Enter another number\n')))
    values.append(float(input('Enter another number\n')))
    values.append(float(input('Enter another number\n')))
    values.append(float(input('Enter another number\n')))
    print(max(values))


class WrongValue(Exception):
    pass


def factorial(value):
    if int(value) <= 1:
        if value < 0:
            raise WrongValue
        return 1
    return factorial(value - 1) * value


def array_abs(array):
    abs_array = []
    for i in array:
        abs_array.append(abs(i))
    return abs_array


def array_sum(array):
    return sum(array)


class Zero(Exception):
    pass


def abcz3():
    def _is_not_zero(value):
        if value == 0:
            raise Zero
        return value

    a = _is_not_zero(int(input()))
    b = _is_not_zero(int(input()))
    c = _is_not_zero(int(input()))

    if a + b > c:
        print('alpha')
    elif (b - c) < a:
        print('bravo')
    elif (b % c) == 0:
        print('charlie')
    else:
        print('zulu')
