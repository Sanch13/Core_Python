class Cat:
    def __init__(self, name):
        self.name = name


furball = Cat('Grumpy')  # furball.name --> Grumpy

"""Не обязательно иметь метод __init__() в описании каждого класса — он используется для 
того, чтобы различать объекты одного класса. Это не то, что в некоторых
других языках называется конструктором. Python уже создал объект для вас. Метод
__init__() следует рассматривать скорее как средство инициализации. Если класс Cat уже определен, 
как мы сделали в этой главе, то второй такой класс создать не получится. """

class Car:
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

"""Проверить, унаследован ли класс от другого класса, можно с помощью функции
issubclass()"""
issubclass(Yugo, Car)  # True

give_me_a_car = Car()
give_me_a_yugo = Yugo()
"""Если говорить в терминах объектно-ориентированных языков, Yugo является Car. Объект с 
именем give_me_a_yugo — это экземпляр класса Yugo, но он также наследует все то, 
что может делать класс Car."""
# give_me_a_car.exclaim()      # I'm a Car!
# give_me_a_yugo.exclaim()     # I'm a Car!

"""Многолетний опыт работы в объектно-ориентированном программировании показал, 
что чрезмерное увлечение наследованием может затруднить управление программами. 
Вместо этого рекомендуется сделать акцент на использовании других приемов, таких 
как агрегирование и композиция. """

"""Класс Yugo должен как-то отличаться от класса Car, иначе зачем вообще создавать новый класс.
Изменим способ работы метода exclaim() для класса Yugo_1"""
class Yugo_1(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car_1 = Car()
give_me_a_yugo_1 = Yugo_1()
# give_me_a_car_1.exclaim()   # I'm a Car!
# give_me_a_yugo_1.exclaim()  # I'm a Yugo! Much like a Car, but more Yugo-ish.

"""В этих примерах мы переопределили метод exclaim(). Переопределять можно любые методы,
включая __init__(). В производный класс можно добавить и метод, которого не было в родительском
классе."""

"""Получаем помощь от своего родителя с использованием метода super(). Мы видели, как 
производный класс может добавить или переопределить метод родительского класса. 
Но что, если нужно будет вызвать этот родительский метод?"""

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

"""Когда вы определяете метод __init__() для своего класса, вы заменяете метод __init__()
родительского класса, который больше не вызывается автоматически. В результате вам
нужно вызывать его явно. 
- Метод super() получает определение родительского класса Person
- метод __init__() вызывает метод Person.__init__(). Последний заботится о том, чтобы передать 
аргумент self суперклассу, поэтому вам нужно просто дать ему любые необязательные аргументы. 
В нашем случае единственным аргументом класса Person() будет name"""

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
# bob.name    # 'Bob Frapples'
# bob.email   # 'bob@frapples.com'

"""Мы могли бы определить новый класс так у родителя, но тогда потеряли бы возможность 
применять наследование. Мы использовали метод super(), чтобы заставить Person делать свою работу
так же, как это делает обычный объект класса Person. Есть и другое преимущество:
если определение класса Person в будущем изменится, с помощью метода super()
мы сможем гарантировать, что атрибуты и методы, которые класс EmailPerson наследует от класса 
Person, отреагируют на изменения. Используйте метод super(), когда потомок делает что-то 
по-своему, но все еще нуждается в помощи родителя (как и в реальной жизни)."""



"""Множественное наследование. Объекты могут наследовать и от нескольких родительских классов.
Если ваш класс ссылается на метод или атрибут, которого у него нет, Python будет искать его в 
родительском классе. Что, если у нескольких классов будут атрибуты с одинаковыми именами?
 Кто победит? Наследование в Python зависит от порядка разрешения методов. Каждый класс Python 
 имеет особый метод mro(), возвращающий список классов, в которых будет выполнен поиск метода 
 или атрибута для объекта этого класса. Похожий атрибут с именем __mro__ представляет собой 
 кортеж, содержащий имена этих классов. Побеждает первый."""


class Animal:
    def says(self):
        return 'I speak!'

class Horse(Animal):
    def says(self):
        return 'Neigh!'

class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

"""Если нам понадобится метод или атрибут класса Mule, Python будет искать его в следующих классах
по порядку.
1. Сам объект (типа Mule).
2. Класс объекта (Mule).
3. Первый родительский класс этого класса (Donkey).
4. Второй родительский класс этого класса (Horse).
5. Прародительский класс этого класса (Animal)."""

Mule.mro()
# [
# <class '__main__.Mule'>,
# <class '__main__.Donkey'>,
# <class '__main__.Horse'>,
# <class '__main__.Animal'>,
# <class 'object'>
# ]

mule = Mule()
hinny = Hinny()
mule.says()      # 'Hee-haw!'
hinny.says()     # 'Neigh!'

"""Если бы у классов Horse и Donkey не было метода says(), классы Mule и Hinny использовали 
бы метод says() прародительского класса Animal и возвратили бы значение 'I speak!'."""


# class A():
#     count = 0
#
#     def __init__(self):
#         A.count += 1
#
#     def exclaim(self):
#         print("I'm an A!")
#
#     @classmethod
#     def kids(cls):
#         print("A has", cls.count, "little objects.")
#
#     @staticmethod
#     def commercial():
#         print('This CoyoteWeapon has been brought to you by Acme')
#
# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
# A.kids()
# A.commercial()
# breezy_a.kids()
# breezy_a.commercial()

"""Агрегирование и композиция. Наследование может сослужить хорошую службу, когда вы хотите, 
чтобы класспотомок большую часть времени вел себя как родительский класс (потомок является
родителем). Возможность создавать иерархии наследования довольно заманчива, но иногда композиция
или агрегирование имеет больше смысла. В чем разница? При композиции один объект является 
частью другого. Утка является птицей (наследование), но имеет хвост (композиция). 
Хвост не похож на утку — он является частью утки. В следующем примере создадим объекты 
bill и tail и предоставим их новому объекту duck:"""

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')


а_tail = Tail('long')
а_bill = Bill('wide orange')
duck = Duck(а_bill, а_tail)
# duck.about()    # This duck has a wide orange bill and a long tail
"""Агрегирование выражает более свободные отношения между объектами: один из них использует 
другой, но оба они существуют независимо друг от друга. Утка использует озеро, 
но не является его частью"""


"""Именованные кортежи"""
from collections import namedtuple
"""Именованный кортеж — это подкласс кортежей, с помощью которых вы можете получить доступ к 
значениям по имени (используя конструкцию .имя) и позиции (используя конструкцию [смещение]).
Преобразуем класс Duck в именованный кортеж, сохранив bill и tail как простые строковые аргументы.
Функцию namedtuple можно вызвать, передав ей два аргумента:
- имя нового подкласса именованного кортежа;
- строку, содержащую имена полей, разделенные пробелами."""

Duck = namedtuple('Duck', 'bill tail')  # Создает новый подкласс кортежа с именованными полями
duckk = Duck('wide orange', 'long')     # Duck(bill='wide orange', tail='long')
PP = namedtuple('PP', 'name old')
pp = PP('Sanch', 37)                    # PP(name='Sanch', old=37)
# pp[1]                                   # 37
# pp.name = 'God'                         # AttributeError: can't set attribute
"""Мы могли бы определить pp как словарь dd"""
dd = pp._asdict()                       # {'name': 'Sanch', 'old': 37}
"""Вы можете добавить поля в словарь и изменить значения других поелй"""
dd['old'] = 100                         # 'old': 100
dd['name'] = 'God'                      #'name': 'God'
# dd['skills'] = 'fine'                   # 'skills': 'fine'
pp = PP(**dd)                           # PP(name='Sanch', old=100)
"""Именованные кортежи неизменяемы, но вы можете заменить одно или несколько
полей и вернуть другой именованный кортеж"""
tt = pp._replace(name='Yo', old=88)    # tt = PP(name='Yo', old=88)

"""Именованный кортеж можно сделать также из словаря"""

Duck = namedtuple('Duck', 'bill tail')
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)       # Duck(bill='wide orange', tail='long')
"""Обратите внимание на конструкцию **parts. Это аргумент — ключевое слово. Он извлекает 
ключи и значения словаря parts и передает их в качестве аргументов"""

"""Классы данных dataclass"""

"""Перед вами простой старый объект, имеющий один атрибут name:"""
class TeenyClass():
    def __init__(self, name):
        self.name = name

teeny = TeenyClass('itsy')  # teeny.name --> itsy

"""Реализация той же функциональности с помощью классов данных будет выглядеть несколько иначе"""

from dataclasses import dataclass
@dataclass
class TeenyDataClass:
    name: str

teeny1 = TeenyDataClass('bitsy')    # teeny1.name --> bitsy

"""Помимо декоратора @dataclass, вам нужно определить атрибуты класса с помощью
аннотаций переменных. Это выглядит как 
имя: тип    или    имя: тип = значение
например color: str    или    color: str = "red".
Типом может быть любой тип объектов в Python, включая созданные вами классы, а не только 
встроенные, такие как str или int. Когда вы создаете объект класса данных, вы предоставляете 
аргументы в том порядке, в котором они указаны в классе, или используете именованные аргументы,
передавая их в любом порядке:"""

from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
# AnimalClass(name='yeti', habitat='Himalayas', teeth=46)
duck01 = AnimalClass(habitat='lake', name='duck')
# AnimalClass(name='duck', habitat='lake', teeth=0)
"""Вы можете обращаться к атрибутам этого объекта точно так же, как и к атрибутам
других объектов"""
# snowman.teeth       # 46
# duck01.habitat      # lake

"""По множеству причин рекомендуется использовать сторонний пакет attrs (https://oreil.ly/Rdwlx),
который позволяет меньше набирать, меньше проверять данные и т. д. Взгляните сами и решите для 
себя, что вам больше нравится — эта библиотека или встроенные решения."""

# TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS   TASKS

"""10.1. Создайте класс Thing, не имеющий содержимого, и выведите его на экран. Затем создайте
объект example этого класса и также выведите его. Совпадают ли выведенные значения? - No"""
class Thing:
    pass
# print(Thing)      # <class '__main__.Thing'>
example = Thing()   # <__main__.Thing object at 0x000001E869C12A60>
###################################################################################################
"""10.2. Создайте новый класс с именем Thing2 и присвойте переменной letters значение 'abc'. 
Выведите на экран значение letters."""
class Thing2:
    letters = 'abc'
# Thing2.letters  # abc
###################################################################################################
"""10.3. Создайте еще один класс, который, конечно же, называется Thing3. В этот раз присвойте 
значение 'xyz' атрибуту объекта letters. Выведите на экран значение атрибута letters. 
Понадобилось ли вам создавать объект класса, чтобы сделать это? - yes"""
class Thing3:
    def __init__(self):
        self. letters = 'xyz'
# objj = Thing3()
# objj.letters    # xyz
###################################################################################################
"""10.4. Создайте класс Element, имеющий атрибуты объекта name, symbol и number.
Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1."""
# class Element:
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#     def dump(self):
#         print(f"name = {self.name}, symbol = {self.symbol}, number = {self.number}")
#
#     def __str__(self):
#         return f"name = {self.name}, symbol = {self.symbol}, number = {self.number}"

# obj = Element('Hydrogen', 'H', 1)
###################################################################################################
"""10.5. Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen', 'symbol': 'H',
'number': 1. Далее создайте объект с именем hydrogen класса Element с помощью этого словаря."""
d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = Element(d['name'], d['symbol'], d['number'])   # from Aleksandr Shvec - design patterns
# hydrogen = Element(**d)
###################################################################################################
"""10.6. Для класса Element определите метод с именем dump(), который выводит на экран 
значения атрибутов объекта (name, symbol и number). Создайте объект hydrogen из этого нового 
определения и используйте метод dump(), чтобы вывести на экран его атрибуты."""
# hydrogen.dump()     # name = Hydrogen, symbol = H, number = 1
###################################################################################################
"""10.7. Вызовите функцию print(hydrogen). В определении класса Element измените имя метода 
dump на __str__, создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen)."""
# print(hydrogen)                       # <__main__.Element object at 0x0000026AA0F16AF0>
# hydrogen = Element('Yooo', 'Q', 4)
# print(hydrogen)                       # name = Yooo, symbol = Q, number = 4
###################################################################################################
"""10.8. Модифицируйте класс Element, сделав атрибуты name, symbol и number приватными. 
Определите свойство получателя для каждого атрибута, возвращающее его значение."""
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number
###################################################################################################
"""10.9. Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них определите
всего один метод — eats(). Он должен возвращать значения 'berries' (для Bear), 'clover' 
(для Rabbit) или 'campers' (для Octothorpe). Создайте по одному объекту каждого класса 
и выведите на экран то, что ест указанное животное."""
class Bear:
    def eats(self):
        return f'berries'

class Rabbit:
    def eats(self):
        return f'clover'

class Octothorpe:
    def eats(self):
        return f'campers'

bear = Bear()
bear.eats()                 # berries
rabbit = Rabbit()
rabbit.eats()               # clover
octothorpe = Octothorpe()
octothorpe.eats()           # campers
###################################################################################################
"""10.10. Определите три класса: Laser, Claw и SmartPhone. Каждый из них имеет только один 
метод — does(). Он возвращает значения 'disintegrate' (для Laser), 'crush' (для Claw) или 
'ring' (для SmartPhone). Далее определите класс Robot, который содержит по одному объекту 
каждого из этих классов. Определите метод does() для класса Robot, который выводит на 
экран все, что делают его компоненты."""
class Laser:
    def does(self):
        return f'disintegrate'

class Claw:
    def does(self):
        return f'crush'

class SmartPhone:
    def does(self):
        return f'ring'

laser = Laser()
claw = Claw()
smarphone = SmartPhone()

class Robot:
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        print(f'laser says {self.laser.does()},\n'
              f'claw says {self.claw.does()},\n'
              f'smatphone says {self.smartphone.does()}')

verter = Robot(laser, claw, smarphone)
verter.does()

###################################################################################################
#                                   VERSION FROM BOOK
# class Robot:
#     def __init__(self):
#         self.laser = Laser()
#         self.claw = Claw()
#         self.smartphone = SmartPhone()
#
#
#     def does(self):
#         print(f'laser says {self.laser.does()},\n'
#               f'claw says {self.claw.does()},\n'
#               f'smatphone says {self.smartphone.does()}')
#
# r = Robot()
# r.does()
###################################################################################################

