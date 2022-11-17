# x = 99
#
#
# def local():
#     x = 0
#
#
# def glob1():
#     global x
#     x += 1
#
#
# def glob2():
#     x = 0
#     import f1
#     f1.x += 1
#
#
# def glob3():
#     x = 0
#     import sys
#     glob = sys.modules['f1']
#     glob.x += 1
#
#
# def test():
#     print(x)
#     local(); glob1(); glob2(); glob3()
#     print(x)


# def f1():
#     x = 88
#
#     def f2():
#         print(x)
#     f2()
#
#
# f1()

# def f1():
#     x = 88
#
#     def f2():
#         return f"{x}"
#
#     return f2
#
#
# print(f1()())
# action = f1()
# print(action())
# print(type(f1()))

# def maker(n):
#     def action(x):
#         return x * n
#
#     return action
#
#
# print(maker(5)('hi '))
# f = maker(2)
# print(f)
# print(maker(5)('Bye '))

# def maker(n):
#     return lambda x: x ** n
#
# h = maker(3)
# x = 100
# def f1():
#     x = 99
#
#     def f2():
#         def f3():
#             print(x)
#         f3()
#
#     f2()
#
# f1()

# def tester(start):
#     state = start
#     def nested(label):
#         nonlocal state  # запоминает из объемлющей области видимости
#         print(label, state)
#         state += 1      # нелокальную переменную разрешено изменять
#     return nested


# def tester(start):
#     def nested(label):
#         print(label, nested.state)
#         nested.state += 1
#     nested.state = start
#     return nested

# l = [1,2,3,4,5]
# print(l)
#
# def f(l):
#     l += [0]
#
# f(l)
# print(l)

# l = [1,2]
# a = 1
#
# def f(a, l):
#     l = l[:]
#     a = 2
#     l[0] = 23
#     return a, l
#
#
# f(a, l)
# print(*f(a, l))
# print(a, l)

# def f(a, b=8, *args, c=True, **kwargs):
#     return a, b, args, c, kwargs
#
#
# print(f(3, 4, 5, 6, l=1, j=4))
# print(f(3, 123, 5, 6, l=1, j=4))
# # s = 'spam'
# print(f(*s))


# def func(a, b=2, c=3):
#     print(a,b, c)
#
# func(1)
# func(a=10)
# func(11, 88)
# func(1, c=0)


# def func(a=[]):
#     a.append('surprise')
#     return a
#
# print(func())
# print(func())
# print(func())

def f(a, *b, c=6, **d): return (a, b, c, d)
# print(f(1, 2, 3, x=4, y=5))
# print(f(1, 2, 3, x=4, y=5, c=7))
# print(f(1, 2, 3, c=7, x=4, y=5))
# print(f(1, c=7, *(2, 3,),  x=4, y=5))
# print(f(1, *(2, 3,),  x=4, y=5, c=7))



# def f(a, *b, c=6, **d): return (a, b, c, d)
# print(f(1, *(2, 3,), **dict(x=4, y=5)))
# print(f(1, *(2, 3,), **dict(x=4, y=5), c=7))
# print(f(1, *(2, 3,), c=7, **dict(x=4, y=5)))
# print(f(1, c=7, *(2, 3,),  **dict(x=4, y=5)))












