class FirstClass:
    def __init__(self, value):
        self.data = value

    def display(self):
        return self.data


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s”' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "[ThirdClass: %s]" % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass("abc")
a.display()  # Вызывается унаследованный метод
print(a)  # __str__ : возвращает отображаемую строку
b = a + "xyz"  # __add__ : создает новый экземпляр
b.display()  # b имеет все методы класса ThirdClass
print(b)
a.mul(3)  # mul: изменяет экземпляр на месте
print(a)
print(ThirdClass.__bases__)
