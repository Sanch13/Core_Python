"""From BOOK"""
"""Декоратор, размещенный ближе всего к функции (прямо над def), будет выполнен первым, а
затем выполнится тот, что находится сразу над ним."""


def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@square_it
@document_it
def add_ints(a, b):
    return a + b


print(add_ints(3, 5))


# @document_it
# @square_it
# def add_ints(a, b):
#     return a + b
#
# print(add_ints(3, 5))

###################################################################################################


count = iter(range(1, 10))


def decorate_1(func):
    def wrapper_1(*args, **kwargs):
        print(f'Do it {next(count)}, I am decorate_1')
        result = func(*args, **kwargs)
        print(f'Do it {next(count)}, decorate_1 have finished')
        return f'<dec_1>{result}</dec_1>'
    return wrapper_1


def decorate_2(func):
    def wrapper_2(*args, **kwargs):
        print(f'Do it {next(count)}, I am decorate_2')
        result = func(*args, **kwargs)
        print(f'Do it {next(count)}, decorate_2 have finished')
        return f'<dec_2>{result}</dec_2>'
    return wrapper_2


# @decorate_2
# @decorate_1
# def say_word_times(words, times):
#     return f'I say {words * times} .'
#
# print(say_word_times('Hi!', 2))

# Do it 1, I am decorate_2
# Do it 2, I am decorate_1
# Do it 3, decorate_1 have finished
# Do it 4, decorate_2 have finished
# <dec_2><dec_1>I say Hi!Hi! .</dec_1></dec_2>


# @decorate_1
# @decorate_2
# def say_word_times(words, times):
#     return f'I say {words * times} .'
#
# print(say_word_times('Hi!', 2))

# Do it 1, I am decorate_1
# Do it 2, I am decorate_2
# Do it 3, decorate_2 have finished
# Do it 4, decorate_1 have finished
# <dec_1><dec_2>I say Hi!Hi! .</dec_2></dec_1>

###################################################################################################

def decorate1(func):
    def wrapper1(*args, **kwargs):
        result = func(*args, **kwargs)
        result += ' I am decorate1 '
        return result
    return wrapper1


def decorate2(func):
    def wrapper2(*args, **kwargs):
        result = func(*args, **kwargs)
        result += ' I am decorate2 '
        return result
    return wrapper2

#
# @decorate2
# @decorate1
# def add_text(s1: str, s2: str):
#     return f"{s1} + {s2}"
#
#
# print(add_text('Sanch', "Ksenyia"))  # Sanch + Ksenyia I am decorate1  I am decorate2


# @decorate1
# @decorate2
# def add_text(s1: str, s2: str):
#     return f"{s1} + {s2}"
#
#
# print(add_text('Sanch', "Ksenyia"))  # Sanch + Ksenyia I am decorate2  I am decorate1