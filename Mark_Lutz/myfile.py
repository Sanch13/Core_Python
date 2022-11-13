from timeit import timeit


# title = "The meaning of life"
# a = "dead"
# b = "parrot"
# c = "sketch"
# print(a, b, c)


# def list_comp():
#     squares = [x ** 2 for x in range(1000)]
#     return squares
#
#
# def ffor():
#     squares = []
#     for x in range(1000):
#         squares.append(x**2)
#     return squares
#
#
# def concotinate():
#     squares = []
#     for x in tuple(range(1000)):
#         squares += [x]
#     return squares


# print(timeit("list_comp()", globals=globals(), number=10000))
# print(timeit("ffor()", globals=globals(), number=10000))
# print(timeit("concotinate()", globals=globals(), number=10000))

# def just_open():
#     l = []
#     for line in open('Questions.txt', encoding='utf8'):
#         l.append(line)
#
#
# def open_readlines():
#     l = []
#     for line in open('Questions.txt', encoding='utf8').readlines():
#         l.append(line)

# def open_while():
#     f = open("Questions.txt", encoding='utf8')
#     l = []
#     while 1:
#         line = f.readline()
#         if not line: break
#         l.append(line)


# result1 = [round(timeit("just_open()", globals=globals(), number=10000), 5) for _ in range(5)]
# print(f'{sum(result1) / 5:.7}')      # 1.207828, 1.198302, 1.209996
# result2 = [round(timeit("open_readlines()", globals=globals(), number=10000), 5) for _ in range(5)]
# print(f'{sum(result2) / 5:.7}')      # 1.212836, 1.225576, 1.213552
# result3 = [round(timeit("open_while()", globals=globals(), number=10000), 5) for _ in range(5)]
# print(f'{sum(result3) / 5:.7}')  # 1.275006, 1.281348, 1.262974
# print(f'{timeit("just_open()", globals=globals(), number=10000):.4}')  # 0.6661
# print(f'{timeit("open_readlines()", globals=globals(), number=10000):.4}')  # 0.7496
