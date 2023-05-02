class WhoAmI:

    def __init__(self, res: int = 0, step: int = 1):
        self.res = res
        self.step = step

    def increase(self) -> int:
        self.res += self.step
        return self.res

    def __str__(self) -> str:
        return str(self.res)


c = WhoAmI()
print(c.__dict__)
c.increase()
c.increase()
c.increase()
c.increase()
print(c.increase())
b = WhoAmI()
b.increase()
b.increase()
b.increase()
print(b.res)
ten = id(b)
sixteen = hex(id(b))
print(ten, sixteen, int(sixteen, 16))
# print(b, type(b), id(b), hex(id(b)))
print(c)
