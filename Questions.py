"""Декоратор, размещенный ближе всего к функции (прямо над def), будет выполнен первым, а
затем выполнится тот, что находится сразу над ним."""

count = iter(range(1, 10))


def decorate_1(func):
    def wrapper_1(*args, **kwargs):
        print(f'Do it {next(count)}, I am decorate_1')
        result = func(*args, **kwargs)
        print(f'Do it {next(count)}, decorate_1 have finished')
        return result
    return wrapper_1


def decorate_2(func):
    def wrapper_2(*args, **kwargs):
        print(f'Do it {next(count)}, I am decorate_2')
        result = func(*args, **kwargs)
        print(f'Do it {next(count)}, decorate_2 have finished')
        return result
    return wrapper_2


@decorate_2
@decorate_1
def say_word_times(words, times):
    print(f'I say {words * times}')

say_word_times('Hey', 3)

# Do it 1, I am decorate_2
# Do it 2, I am decorate_1
# I say HeyHeyHey
# Do it 3, decorate_1 have finished
# Do it 4, decorate_2 have finished


# @decorate_1
# @decorate_2
# def say_word_times(words, times):
#     print(f'I say {words * times}')
#
# say_word_times('Hey', 3)

# Do it 1, I am decorate_1
# Do it 2, I am decorate_2
# I say HeyHeyHey
# Do it 3, decorate_2 have finished
# Do it 4, decorate_1 have finished





