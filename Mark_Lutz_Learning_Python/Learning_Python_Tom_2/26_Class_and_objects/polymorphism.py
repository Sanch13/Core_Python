class Employee:  # Универсальный суперкласс
    def __init__(self, name=""):
        self.name = name

    def compute_salary(self):
        ...  # Общие или стандартные линии поведения

    def give_raise(self):
        ...

    def promote(self):
        ...

    def retire(self):
        ...


class Engineer(Employee):  # Специализированный подкласс
    age = 22

    def compute_salary(self):
        """Из-за того, что версия computeSalary находится ниже в дереве классов, она заместит
        (переопределит) универсальную версию в Employee."""
        ...  # Что-то специальное


alex = Engineer()
print(type(Engineer), alex.__class__.__name__)
alex.__setattr__("name", "Alex")
print(alex.__dict__)
print(Employee.compute_salary(alex))
print(alex.age)
