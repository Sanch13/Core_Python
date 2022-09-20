"""Декоратор, размещенный ближе всего к функции (прямо над def), будет выполнен первым, а
затем выполнится тот, что находится сразу над ним."""


def document_it(func):
    def function_1(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return function_1


def square_it(func):
    def function_2(*args, **kwargs):
        result = func(*args, **kwargs)
        print('I am working')
        return f"This is a result two decorate {result ** 2}"
    return function_2


"""The first way"""


@document_it
@square_it
def add_ints(a, b):
    return a + b


add_ints(3, 5)


# Running function: function_2
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: This is two decorate 64
# This is two decorate 64


"""The second way"""

# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b
#
#
# print(add_ints(3, 5))
#
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# This is two decorate 64