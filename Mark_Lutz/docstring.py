"""Module documentation"""

# spam = 40
#
#
# def square(x):
#     """function documentation"""
#     return x**2
#
#
# class Employee:
#     """class documentation"""
#     pass
#
#
# print(square(4))
# print(square.__doc__)
#
# for i in range(50):
#     print('hello %d\n\a' % i)


l = [1, 2, 4, 8, 16, 32, 64]
x = 5
for i in l:
    if 2**x == i:
        print(f'at index', l.index(i))
        break

if 2**x in l:
    print(f'at index', l.index(2**x))

print(f'at index', *[l.index(i) for i in l if i == 2**x])

