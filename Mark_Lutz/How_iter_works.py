l = [1, 2, 3, 4, 5]  # create new list (sequence)

object_iterable = iter(l)
# create iterable object of l,
# object_iterable = <list_iterator object at 0x0000027FB9B52860>

# print(object_iterable.__next__())
# print(next(object_iterable))
# object_iterable.__next__() or next(object_iterable)
# call method next() or obj.__next__() to move on the next obj


for x in l:
    print(x ** 2, end=' ')
    """Автоматическая итерация. Получает iter, вызывает __next__, перехватывает исключения"""

while True:
    try:
        x = next(object_iterable)
    except StopIteration:
        break
    print(x ** 2, end=' ')
    """Ручная итерация: то, что обычно делают циклы for. Оператор try перехватывает исключения 
    или вызов next(object_iterable)"""