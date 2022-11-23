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
# import sys


# def f(a, *b, c=6, **d): return (a, b, c, d)
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

# l = [1,2,3,3,4,5,6,7,3,3,8,9,0,2,4,5]
# p = (3,5,6,7,8)
# m = [4,3,6]
# def intersect(*args):
#     res = []
#     for x in args[0]:
#         if x in res: continue
#         for other in args[1:]:
#             if x not in other: break
#         else:
#             res.append(x)
#     return res
#
# print(intersect(l, p, m))


# def print3(*args, sep=' ', end='\n', file=sys.stdout):
#     output = ''
#     first = True
#     for arg in args:
#         output += ('' if first else sep) + str(arg)
#         first = False
#     file.write(output + end)
#
#
# print3('sad', 'bad', 'cat', end='')
# print('sad', 'bad', 'cat')
import sys
from timeit import timeit

# l = list(range(990))
#
#
# def mysum(l):
#     if not l:
#         return 0
#     else:
#         return l[0] + mysum(l[1:])
#
#
# def mysum2(l):
#     return 0 if not l else l[0] + mysum2(l[1:])
#
#
# def mysum3(l):
#     sum = 0
#     for x in l:
#         sum += x
#     return sum

# print(round(timeit('mysum(l)', globals=globals(), number=1000), 5))   # 2.73014
# print(round(timeit('mysum2(l)', globals=globals(), number=1000), 5))    # 2.72523
# print(round(timeit('mysum3(l)', globals=globals(), number=1000), 5))    # 0.03165
# print(round(timeit('sum(l)', globals=globals(), number=1000), 5))    # 0.00389

# l = [[1,2], [[[[2,3], 5, 6]], 7,], [3, [5,6, [0,7,6]]]]
#
# def sumtree(l):
#     total = 0
#     for x in l:
#         if not isinstance(x, list):
#             total += x
#         else:
#             total += sumtree(x)
#         # total += x if not isinstance(x, list) else sumtree(x)
#     return total

# print(sumtree(l))
# print(round(timeit('sumtree(l)', globals=globals(), number=1000), 5))   # 0.00223


# def sumtree2(l):
#     total = 0
#     items = list(l)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             total += front
#         else:
#             items.extend(front)
#     return total


# print(sumtree2(l))
# print(round(timeit('sumtree2(l)', globals=globals(), number=1000), 5))   # 0.00341


# def sumtree3(l):
#     total = 0
#     items = list(l)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):
#             total += front
#         else:
#             items[:0] = front
#     return total
#
#
# # print(sumtree3(l))
# print(round(timeit('sumtree3(l)', globals=globals(), number=1000), 5))   # 0.00467

# import sys
# from tkinter import Button, mainloop
# butt = Button()
# butt = Button(text='Press me', command=(lambda :sys.stdout.write('Spam\n')))
# butt.pack()
# mainloop()


# seq = 'abc'


# def permute2(seq):
#     if not seq:
#         yield seq
#     else:
#         for i in range(len(seq)):
#             rest = seq[:i] + seq[i+1:]
#             for x in permute2(rest):
#                 yield seq[i:i+1] + x
#
#
# print(list(permute2(seq)))

# l1 = 'sadm'
# l2 = '9827'
# l3 = '!@#$'
#
#
# def myzip(*seq):
#     all_list = []
#     for i in seq:
#         all_list.append(list(i))
#     out_list = []
#     while all(all_list):
#         rest = ()
#         for c in all_list:
#             rest += tuple(c.pop(0))
#         out_list.append(rest)
#     return out_list

# def myzip(*seq):
#     """generator"""
#     all_list = []
#     for i in seq:
#         all_list.append(list(i))
#     while all(all_list):
#         rest = ()
#         for c in all_list:
#             rest += tuple(c.pop(0))
#         yield tuple(rest)


# def myzip_short(*seqs):
#     seqs_list = [list(s) for s in seqs]
#     while all(seqs_list):
#         yield tuple(i.pop(0) for i in seqs_list)
#
#
# def myzip_very_short(*seq):
#     min_length = min(len(l) for l in seq)
#     return [tuple(s[i] for s in seq) for i in range(min_length)]
#
#
# answer = list(myzip(l1, l2, l3))
# answer2 = list(myzip_short(l1, l2, l3))
# answer3 = myzip_very_short(l1, l2, l3)
#
#
# print(answer)
# print(answer2)
# print(answer3)

import time










