import unicodedata

"""Все текстовые примеры до сих пор имели формат ASCII (American Standard Code for Information 
Interchange). Этот формат был определен в 1960-х годах. Основной единицей хранения информации был
байт, который мог хранить 256 уникальных значений в своих 8 битах. Unicode — это действующий 
международный стандарт, определяющий символы всех языков мира плюс математические и другие символы.
Еще и эмодзи! Unicode предоставляет уникальный номер каждому символу, независимо от платформы, 
программыи языка."""
# print(ord("♥"), chr(9892))
# for char in range(1, 10000):
#     print(f"symbol-{char}--> {chr(char)}")

"""Модуль unicodedata содержит функции, которые преобразуют символы в обоих направлениях:
- lookup() принимает не зависящее от регистра имя и возвращает символ Unicode;
- name() принимает символ Unicode и возвращает его имя в верхнем регистре."""

def unicode_test(value):
    """Принимает символ Unicode, ищет его имя, а затем ищет символ, соответствующий полученному
имени (он должен совпасть с оригинальным)"""
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f"{value=}, {name=}, {value2=}, {ord(value)}")
    # print('value="%s", name="%s", value2="%s"' % (value, name, value2))
# unicode_test("♥")   # value='♥', name='BLACK HEART SUIT', value2='♥', 9829
# unicode_test('§')   # value='§', name='SECTION SIGN', value2='§', 167
# unicode_test("☃")   # value='☃', name='SNOWMAN', value2='☃', 9731

"""UTF-8 — это стандартная текстовая кодировка для Python, Linux и HTML. Она охватывает 
множество символов, работает быстро и хорошо. Гораздо удобнее работать с кодировкой UTF-8, 
чем постоянно переключаться с одной кодировки на другую.
UTF-8 — динамическую схему кодирования. 
Она использует для символа Unicode от 1 до 4 байт:
- 1 байт для ASCII;
- 2 байта для большинства языков, основанных на латинице (но не кириллице);
- 3 байта для других основных языков;
- 4 байта для остальных языков, включая некоторые азиатские языки и символы."""

"""Кодирование
Вы кодируете строку байтами. Первый аргумент строковой функции encode() — это имя кодировки.
"""
snowman = '\u2603'
ds = snowman.encode('utf-8')
"""Функция len() возвращает число байтов — 3, поскольку ds является переменной bytes."""
# print(ds, len(ds))  # b'\xe2\x98\x83' 3 # было использовано три байта
"""Декодирование
Мы декодируем байтовые строки в текстовые строки Unicode. Когда мы получаем текст
из какого-то внешнего источника (файлов, баз данных, сайтов, сетевых API и т. д.),
он закодирован в виде байтовой строки. Самое сложное — узнать, какая кодировка
была использована, чтобы можно было декодировать и получить строку Unicode.
Проблема в следующем: ничто в байтовой строке не говорит нам о том, какая
кодировка была использована.
"""
place = 'caf\u00e9'
# print(place, type(place)        # café <class 'str'>
"""Закодируем ее в формат UTF-8 с помощью переменной bytes, которая называется place_bytes"""
place_bytes = place.encode('utf-8')
# print(place_bytes, type(place_bytes), len(place_bytes))   # b'caf\xc3\xa9' <class 'bytes'> 5
"""Обратите внимание на то, что переменная place_bytes содержит 5 байт. Первые
три такие же, как в ASCII (преимущество UTF-8), а последние два кодируют символ
'é'. Теперь декодируем эту байтовую строку обратно в строку Unicode"""
place2 = place_bytes.decode('utf-8')
# print(place2)   # café
"""Это сработало, поскольку мы закодировали и декодировали строку с помощью кодировки UTF-8."""


"""Мораль этой истории: по возможности используйте кодировку UTF-8. Она работает и 
поддерживается везде, она способна выразить любой символ Unicode, и с ее
помощью можно быстро кодировать и декодировать."""

"""Текстовые строки: регулярные выражения"""
"""Этот механизм поставляется в стандартном модуле re, который мы импортируем. Вы определяете
строковый шаблон, совпадения для которого вам нужно найти, и строку-источник, в которой
следует выполнить поиск."""
import re
"""Функция match() проверяет, начинается ли источник с шаблона."""
# result = re.match('You', 'Young Frankenstein')     # <re.Match object; span=(0, 3), match='You'>
"""Для более сложных проверок вам нужно скомпилировать шаблон, чтобы ускорить поиск"""
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')      # <re.Match object; span=(0, 3), match='You'>
"""Изменим шаблон и попробуем найти первое совпадение с помощью функции match()
.* - будут означать любое количество символов (даже ноль)"""
# if result_0 := re.match('.*Frank', 'Young Frankenstein'):
#     print(result_0.group())                   # Young Frank
"""Поскольку в Python с этим часто приходится иметь дело, напомню еще раз: функция match() ищет
строку-шаблон только в начале строки-источника, а функция search() ищет шаблон в любом
 месте источника. Функция match() — не единственный способ сравнить шаблон и источник."""
# if result_1 := re.match('You', 'Young Frankenstein'):
#     print(result_1.group())                   # You
"""- search() возвращает первое совпадение, если таковое имеется. используйте функцию search(),
чтобы найти шаблон в любом месте строки-источника, не прибегая к использованию символа подстановки.*
"""
# if result_1 := re.search('Frank', 'Young Frankenstein'):
#     print(result_1.group())                   # Frank
"""- findall() возвращает список всех непересекающихся совпадений, если таковые имеются"""
m = re.findall('n', 'Young Frankenstein')       # ['n', 'n', 'n', 'n']
# print('Found', len(m), 'matches')             # Found 4 matches
"""А что насчет строки 'n', за которой следует любой символ?"""
m_1 = re.findall('n.', 'Young Frankenstein')    # ['ng', 'nk', 'ns']
# print('Found', len(m_1), 'matches')           # Found 3 matches
"""- split() разбивает источник на совпадения с шаблоном и возвращает список всех фрагментов строки;
- sub() принимает аргумент для замены и заменяет все части источника, совпавшие с шаблоном, 
на значение этого аргумента."""
m_2 = re.split('n', 'Young Frankenstein')       # ['You', 'g Fra', 'ke', 'stei', '']
m_3 = re.sub('n', '>', 'Young Frankenstein')    # You>g Fra>ke>stei>
import string
printable = string.printable
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
"""Какие символы строки printable являются цифрами?"""
# re.findall('\d', printable)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
"""Какие символы являются цифрами, буквами и нижним подчеркиванием?"""
# ''.join(re.findall('\w', printable))
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_
"""Шаблоны: использование спецификаторов"""
# \b	Граница слова
source = '''I wish I may, I wish I might. Have a dish of fish tonight.'''
"""Начнем с поиска символов w или f, за которыми следует буквосочетание ish:"""
re.findall('[wsh]+', source)    # ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']
"""Найдем одно или несколько сочетаний символов w, s и h:"""
re.findall('[wf]ish', source)   # ['wish', 'wish', 'fish']
"""Найдем символ I, за которым следует сочетание wish:"""
re.findall('I (?=wish)', source)    # ['I ', 'I ']
"""Python использует специальные escape-последовательности для строк. Избегайте случайного 
применения escape последовательностей, используя неформатированные строки Python, когда 
определяете строку регулярного выражения. Всегда размещайте символ r перед строкой шаблона 
регулярного выражения, и escape-последовательности Python будут отключены, как показано здесь"""
re.findall(r'\bfish', source)   # ['fish']
"""Если вы заключите шаблон в круглые скобки, совпадения будут сохранены в отдельную группу,
 а кортеж, состоящий из них, окажется доступен благодаря вызову m.groups()"""
re.search(r'(. dish\b).*(\bfish)', source).groups()      # ('a dish', 'fish')

# print(0b0000_0000_0000_0000_0000_0000_1001_1010)            # 154
# print(0x9a)                                                 # 154
# print(0b0000_0000_0000_0000_0000_0000_1001_1010 == 0x9a)    # True
# print(2 ** 32)                                              # 4294967296
# print(0xffffffff)                                           # 154

# TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS

"""12.1. Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9'.
Выведите на экран значение строки mystery. Выведите на экран значение 
переменной mystery и ее имя Unicode."""
mystery = '\U0001f4a9'
# print(mystery, unicodedata.name(mystery))  # 💩 PILE OF POO
###################################################################################################
"""12.2. Закодируйте строку mystery, на этот раз с использованием кодировки UTF-8, в переменную
типа bytes с именем pop_bytes. Выведите на экран значение переменной pop_bytes."""
pop_bytes = mystery.encode('utf-8')
# print(pop_bytes)      # b'\xf0\x9f\x92\xa9'
###################################################################################################
"""12.3. Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку pop_string. 
Выведите на экран значение переменной pop_string. Равно ли оно значению переменной mystery?"""
pop_string = pop_bytes.decode('utf-8')
# print(pop_string, pop_string == mystery)       # 💩 True
###################################################################################################
"""12.4. При работе с текстом могут пригодиться регулярные выражения. 
Назовите следующую строку mammoth:"""
mammoth = """We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""
###################################################################################################
"""12.5. Импортируйте модуль re, чтобы использовать функции регулярных выражений в Python.
Примените функцию re.findall() для вывода на экран всех слов, начинающихся с буквы с."""
# print(re.findall(r'\bc\w*', mammoth))
# ['cheese', 'city', 'cheese', 'cheek', 'could', 'cheese', 'cast', 'crush']
###################################################################################################
"""12.6. Найдите все четырехбуквенные слова, которые начинаются с буквы c."""
# print(re.findall(r'\bc\w{3}\b', mammoth))   # ['city', 'cast']
###################################################################################################
"""12.7. Найдите все слова, которые заканчиваются на букву r."""
re.findall(r'\w*r\b', mammoth)       # my version
# ['your', 'fair', 'Or', 'scar', 'Mr', 'far', 'For', 'your', 'or']
re.findall(r'\b\w*r\b', mammoth)     # the version from Aleksandr Shvec - design patterns
###################################################################################################
"""12.8. Найдите все слова, которые содержат три гласные подряд."""
re.findall(r'\b[a-zA-Z]*[eioau]{3}[a-zA-Z]*\b', mammoth)            # my version
# ['queen', 'quietly', 'beau', 'queen', 'squeeze', 'queen']
re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth)             # the version from Aleksandr Shvec - design patterns
###################################################################################################
"""12.9. Используйте метод unhexlify для того, чтобы преобразовать шестнадцатеричную строку,
созданную путем объединения двух строк для размещения на странице, в переменную типа bytes 
с именем gif:
'47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b' """
import binascii
import struct
str_1 = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(str_1)
# len(gif)    # 42
# b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04
# \x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
###################################################################################################
"""12.10. Байты, содержащиеся в переменной gif, определяют однопиксельный прозрачный GIF-файл.
Этот формат является одним из самых распространенных. Корректный файл формата GIF начинается
со строки GIF89a. Корректен ли этот файл? - Yes"""
# print(gif[:6] == b'GIF89a')
###################################################################################################
"""12.11. Ширина GIF-файла в пикселах является шестнадцатибитным целым числом
с обратным порядком байтов, которое начинается со смещения 6 байт. Высота
имеет такой же размер и начинается со смещения 8 байт. Извлеките и выведите
на экран эти значения для переменной gif. Равны ли они 1? YES
"""
# print(struct.unpack('<hh', gif[6:10]))            # (1, 1) my version
# width, height = struct.unpack('<HH', gif[6:10])   # (1, 1)    from Aleksandr Shvec - design patterns
###################################################################################################






