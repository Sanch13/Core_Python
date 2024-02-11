class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent / 100))

    def __repr__(self):
        return f"{self.name} [{self.pay} $]"


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100_000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(10)
    print(sue.name, sue.pay)
    print(bob)
    print(sue)
