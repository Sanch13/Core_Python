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

generator = (x ** 2 for x in (1, 2, 3, 4, 5))  # <generator object <genexpr> at 0x000001CD1EB58040>
"""
Генератор - итератор, элементы которого можно итерировать только один раз !!!
Генераторные функции и генераторные выражения сами представляют собой итераторы и потому 
поддерживают только одну активную итерацию. Итератором генератора является сам генератор.
map(), filter(), zip(), sum(), sorted() and other.
"""

L = [1, 2, 3, 4, 5]     # L - итерируемый объект
It = iter(L)            # It - Итератор   <list_iterator object at 0x0000025249E63EB0>
"""
Итерируемый объект - объект, который предоставляет возможность обойти поочередно свои 
элементы. Может быть преобразован к итератору.
It - Итератор - объект, который поддерживает функцию next(). Помнит о том, какой элемент будет 
браться следующий.
"""



