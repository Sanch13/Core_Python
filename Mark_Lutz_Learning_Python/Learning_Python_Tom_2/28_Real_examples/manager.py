from person import Person


class Manager(Person):
    def __init__(self, name, job="Manager", pay=0):
        Person.__init__(self, name, job, pay)

    def give_raise(self, percent, bonus=10):
        # self.pay = int(self.pay * (1 + (percent + bonus) / 100))  # плохой способ
        Person.give_raise(self, percent=(percent + bonus))            # хороший способ


if __name__ == '__main__':
    alice = Manager(name="Alice", pay=100_000)
    alice.give_raise(percent=10)
    print(alice)  # Alice [120000 $]
