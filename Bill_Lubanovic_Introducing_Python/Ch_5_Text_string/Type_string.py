from Bill_Lubanovic_Introducing_Python.Ch_2_Data_Types.Python_types import replace_sep_in_sting
import string

replace_sep_in_sting("""
""")

"""В Python вы можете объединить строки или строковые переменные с помощью
оператора +. Строки (не переменные) можно объединять, просто расположив их одну за
другой: "My word! " "A gentleman caller!"""

print("My word! " "A gentleman caller!")

"""Кроме отсутствия аргумента (когда подразумевается, что нужно найти пробелы)
или отдельного символа, возможна и ситуация, когда функция strip() удалит все
символы из последовательности"""
blurt = "What the...!!?"
print(blurt.strip('.?!'))
# string.whitespace 	#  \t\n\r\x0b\x0c
# string.punctuation  # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
ex = '   #$ What in tarnation .. {}[]*('
print(ex.strip(string.punctuation + string.whitespace))

setup = 'a duck goes into a bar...'
"""Строка выравнивается в пределах указанного общего количества пробелов"""
print(setup.center(100))	# for center
print(setup.ljust(100))		# in the left
print(setup.rjust(100))		# in the right
"""Старый стиль: %
Старый стиль форматирования строк имеет форму строка % данные . Внутри строки
находятся интерполяционные последовательности. Самая простая последовательность — это 
символ % и буква. Буква указывает на тип данных, которые должны быть отформатированы. Вы можете 
использовать последовательность %s для любого типа данных — Python отформатирует их как строку 
без дополнительных пробелов. Рассмотрим несколько примеров. Сначала целое число:
'%s' -> '42', '%d' -> '42', '%x' -> '2a', '%o' -> '52' """
# %s Строка
# %d Целое число в десятичной системе счисления
# %x Целое число в шестнадцатеричной системе счисления
# %o Целое число в восьмеричной системе счисления
# %f Число с плавающей точкой в десятичной системе счисления
# %e Число с плавающей точкой в шестнадцатеричной системе счисления
# %g Число с плавающей точкой в восьмеричной системе счисления
# %% Символ %

"""Новый стиль форматирования имеет вид <строка.format(данные)>.
Аргументы функции format() должны идти в том порядке, в котором расставлены заполнители {}
 в строке формата."""
# thing = 'woodchuck', place = 'lake'
# 'The {} is in the {}.'.format(thing, place)

"""В новом стиле форматирования вы также можете указать позицию аргументов
следующим образом: Значение 0 относится к первому аргументу place , а 1 — к thing ."""
# 'The {1} is in the {0}.'.format(place, thing)   # 'The woodchuck is in the lake.'

"""Аргументы функции format() могут быть именованными:"""
# 'The {thing} is in the {place}'.format(thing='duck', place='bathtub')
# 'The duck is in the bathtub'

"""Они также могут быть словарями: 
В следующем примере {0} — это первый аргумент функции format() (словарь d ):"""
# d = {'thing': '5', 'place': 'bathtub'}
# 'The {0[thing]:.02} is in the {0[place]}.'.format(d)
# 'The duck is in the bathtub.'

thing = 'wereduck'
place = 5

print(f'The {thing:>20} is in the {place:.^20}')
print(f'The {thing:>.4} is in the {place:03}')


#            Tasks                   Tasks                   Tasks               #
"""Напишите с заглавной буквы слово, которое начинается с буквы m:"""
song = """When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!"""
print(*(word.capitalize() for word in song.strip(string.punctuation).split() if word[0] in 'm'))
###################################################################################################
"""Выведите на экран все вопросы из списка, а также правильные ответы в таком 
виде:
Q: вопрос
A: ответ
"""
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]
for i in range(len(questions)):
    print(f'Q: {questions[i]}', f'\nA: {answers[i]}')
###################################################################################################
"""Выведите на экран следующее стихотворение, используя старый стиль форматирования.
Подставьте в него такие строки: 'roast beef', 'ham', 'head' и 'clam':"""
# My kitty cat likes %s,
# My kitty cat likes %s,
# My kitty cat fell on his %s
# And now thinks he's a %s.
print('My kitty cat likes %s,' % 'roast beef', 'My kitty cat likes %s,' % 'ham', sep='\n')
print('My kitty cat fell on his %s' % 'head', "And now thinks he's a %s." % 'clam', sep='\n')
###################################################################################################
"""Напишите письмо с использованием нового стиля форматирования. Сохраните 
предложенную строку в переменной letter (она понадобится вам в упражнении 
ниже):"""
salutation = 'Hey'
name = "Sanch"
product = "phone"
verbed = "sold"
room = "bathroom"
animals = "Cats"
percent = 100
spokesman = "Artur"
job_title = "Chief"
amount = 20
letter = f"""Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals} 
Send us your receipt and {amount} for shipping and handling 
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed} 
Thank you for your support 
Sincerely,
{spokesman}
{job_title}.
My word! A gentleman caller!
What the
What in tarnation"""
print(letter)
###################################################################################################
"""После проведения публичных опросов с целью выбора имени появились: английская подводная лодка 
Boaty McBoatface, австралийская беговая лошадь Horsey McHorseface и шведский поезд 
Trainy McTrainface. Используйте форматирование с символом % для того, чтобы вывести 
на экран победившие имена для утки, тыквы и шпица 
5 7.  Сделайте то же самое с помощью функции format() 
5 8.  А теперь еще раз с использованием f-строк."""
print("Победившие имена %s, %s и %s" % ('Boaty McBoatface', 'Horsey McHorseface', 'Trainy McTrainface'))
print("Победившие имена {}, {} и {}".format('Boaty McBoatface', 'Horsey McHorseface', 'Trainy McTrainface'))
print(f"Победившие имена {'Boaty McBoatface'}, {'Horsey McHorseface'} и {'Trainy McTrainface'}")




