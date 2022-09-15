# Имя                       Тип       Изменяемый? Примеры
# Булево.значение           bool       Нет        True, False
# Целое.число               int        Нет        47, 25000, 25_000
# Число.с.плавающей точкой  float      Нет        3.14, 2.7e5
# Комплексное число         complex    Нет        3j,5 + 9j
# Текстовая строка          str        Нет        'alas',"alack",'''a verse attack'''
# Кортеж                    tuple      Нет         (2,4, 8)
# Байты                     bytes      Нет         b'ab\xff'
# Фиксированное множество   frozenset  Нет         frozenset(['Elsa','Otto'])
# Словарь                   dict       Да          {'game':'bingo','dog':'dingo','drummer':'Ringo'}
# Список                    list       Да          ['Winken','Blinken','Nod']
# Массив байтов             bytearray  Да          bytearray(…)
# Множество                 set        Да          set([3, 5, 7])

s = ""


def replace_sep_in_sting(string):
    print(' '.join(string.split('.')))


replace_sep_in_sting(s)

"""Python является строго типизированным языком, а это означает, что тип объекта не изменяется,
даже если его значение изменяемо"""
a = 5
print(f'a = {a}', type(a))
b = str(a)
print(f'b = {b}', type(b))
