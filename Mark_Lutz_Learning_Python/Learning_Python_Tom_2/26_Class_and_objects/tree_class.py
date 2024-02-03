class C2:
    ...


class C3:
    ...


class C1(C2, C3):
    def __init__(self, name: str):
        self.name = name

    def set_name(self, name):
        self.name = name


# I1 = C1()
# I2 = C1()
# I1.set_name('bob')
# I2.set_name('sue')
# print(I1.name)
I1 = C1('alex')
I2 = C1('alice')
print(I1.name)

I3 = C3()
print(I3.__dir__())
print("__init__" in dir(I3))
I3.name = "QWERTY"
print(I3.name, I3.__dict__)
