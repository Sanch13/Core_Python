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

def tester(start):
    state = start
    def nested(label):
        nonlocal state  # запоминает из объемлющей области видимости
        print(label, state)
        state += 1      # нелокальную переменную разрешено изменять
    return nested











