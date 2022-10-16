from timeit import repeat


print(repeat('num = 5; num *= 2', number=1, repeat=4))
# number=1 - number of starts, repeat=4 - number of repeats
# [1.33900175569579e-06, 3.219975042156875e-07, 2.169981598854065e-07, 1.770022208802402e-07]


