from timeit import timeit


def make_list_1():
    result = []
    for i in range(10000):
        result.append(i)
    return result


def make_list_2():
    result = [i for i in range(10000)]
    return result


print(f"Function list_1 is : {timeit('make_list_1()', globals=globals(), number=1000):.5f} sec")
# Function list_1 is : 0.36816 sec
print(f"Function list_2 is : {timeit('make_list_2()', globals=globals(), number=1000):.5f} sec")
# Function list_2 is : 0.17744 sec

