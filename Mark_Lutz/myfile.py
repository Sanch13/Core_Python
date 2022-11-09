from timeit import timeit

# title = "The meaning of life"
# a = "dead"
# b = "parrot"
# c = "sketch"
# print(a, b, c)


def list_comp():
    squares = [x ** 2 for x in range(1000)]
    return squares


def ffor():
    squares = []
    for x in range(1000):
        squares.append(x**2)
    return squares


def concotinate():
    squares = []
    for x in tuple(range(1000)):
        squares += [x]
    return squares


# print(timeit("list_comp()", globals=globals(), number=10000))
# print(timeit("ffor()", globals=globals(), number=10000))
# print(timeit("concotinate()", globals=globals(), number=10000))
