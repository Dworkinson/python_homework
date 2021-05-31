from functools import reduce


def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def sequence_handler(func, array):
    result = array[0]

    for elem in array[1:]:
        result = func(result, elem)
    return result


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]

    print(sequence_handler(add, array))
    print(sequence_handler(mult, array))
    print()

    print(sequence_handler(lambda x, y: x + y, array))
    print(sequence_handler(lambda x, y: x * y, array))
    print()

    print(reduce(lambda x, y: x + y, array))
    print(reduce(lambda x, y: x * y, array))
    print()
