def fibonacci(index):
    first = 0
    second = 1

    while index > 0:
        value = first

        yield value
        first = second
        value += second
        second = value
        index -= 1
