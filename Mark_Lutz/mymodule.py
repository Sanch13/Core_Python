# def adder(**kwargs):
#     values = list(kwargs.values())
#     total = values[0]
#     for v in values[1:]:
#         total += v
#     return total


# print(adder(a=1, b=10, c=19))
# print(adder(a='as', b='usual', c='john'))


# print(adder())
# print(adder(23))
# print(adder(23, 45))
# print(adder(23, 45, 67))
# print(adder(23, 45, 67, 45, 67, 87, 9))
# print(adder(['Sanch', 'Prog'], ['Ksenya', 'Mng']))
# print(adder(0.234, 0.9436))


# def adder(*args):  # f(1,5,7), f([1,2,3], [5,6,7]), f('sad', 'bed'), f(0.1, 0.6)
#     items = args[0]
#     for item in args[1:]:
#         items += item
#     return items
#
#
# print(adder(1,5,7))
# print(adder([1,2,3], [5,6,7]))
# print(adder([1,2,3], (5,6,7)))
# print(adder('sad', 'bed'))
# print(adder(0.1, 0.6))


# def copy_dict(d):
#     d_copy = d.copy()
#     return d_copy


# d1 = {1: 1, 2: 2}
# d2 = {3: 3, 4: 4}
# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
#
#
# def add_dict(dict1, dict2):
#     if isinstance(dict1, dict):
#         dict1.update(dict2)
#     elif isinstance(dict1, list):
#         dict1.extend(dict2)
#     return dict1
#
#
# print(add_dict(d1, d2))
# print(add_dict(l1, l2))


# def is_prime(y: int):
#     if y <= 1:
#         return f'{y} not prime'
#     length = list(range(2, int(y)))
#     for x in length:
#         if y % x == 0:
#             return f'{y} has factor {x}'
#     else:
#         return f'{y} is prime'
#
#
# print(is_prime(10))


# import math
#
# l = [2, 4, 9, 16, 25]
#
#
# def is_for(l):
#     out = []
#     for x in l:
#         out.append(math.sqrt(x))
#     return out
#
#
# def is_map(l):
#     return list(map(math.sqrt, l))
#
#
# def is_comp(l):
#     return [math.sqrt(x) for x in l]
#
#
# def is_gen(l):
#     return list(math.sqrt(x) for x in l)
#
#
# print(is_for(l), is_map(l), is_comp(l), is_gen(l), sep='\n')


# def countdown(n):
#     if n != 0:
#         print(n, end=' ')
#         return countdown(n - 1)
#     else:
#         return f'stop'
#
#
# print(countdown(20))
import math
from timeit import timeit


# def my_fact1(n):
#     return n if n == 1 else n * my_fact1(n - 1)
#
#
# def my_fact3(n):
#     res = 1
#     length_fact = list(range(2, n + 1))
#     for x in length_fact:
#         res *= x
#     return res
#
#
# def my_fact4(n):
#     return math.factorial(n)
#
#
# print(timeit("my_fact1(6)", globals=globals(), number=10000))
# print(timeit("my_fact3(6)", globals=globals(), number=10000))
# print(timeit("my_fact4(6)", globals=globals(), number=10000))





