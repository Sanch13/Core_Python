import copy
from abc import ABC, abstractmethod


class Document(ABC):
	def __init__(self, title: str):
		self.title = title
		self.content = []
		self.metadata = {}

	@abstractmethod
	def clone(self):
		pass

	def add_section(self, text: str):
		self.content.append(text)

	def display(self):
		print(self)

	def __str__(self):
		return '\n'.join(f"{k}: {v}" for k, v in self.__dict__.items())


class Contract(Document):
	def __init__(self, title: str, amount: int = 0):
		super().__init__(title=title)
		self.parties = []
		self.amount = amount

	def clone(self):
		return copy.deepcopy(self)


class Invoice(Document):
	def __init__(self, title: str, invoice_number: int):
		super().__init__(title=title)
		self.invoice_number = invoice_number
		self.items = []
		self.total = 0

	def clone(self):
		return copy.deepcopy(self)


class TemplateManager:
	def __init__(self):
		self._prototypes = {}

	def register_template(self, name: str, prototype: Document):
		self._prototypes[name] = prototype.clone()

	def create_from_template(self, name: str) -> Document:
		if name not in self._prototypes:
			raise ValueError(f"Прототип '{name}' не зарегистрирован")

		return self._prototypes[name].clone()


if __name__ == '__main__':
	# Создаём шаблон договора
	contract_template = Contract(title="Договор поставки")
	contract_template.add_section("1. Предмет договора")
	contract_template.add_section("2. Обязанности сторон")

	# Регистрируем
	templates = TemplateManager()
	templates.register_template("supply_contract", contract_template)

	# Создаём реальные договоры из шаблона
	contract1 = templates.create_from_template("supply_contract")
	contract1.parties = ["ООО Рога", "ООО Копыта"]
	contract1.amount = 100000

	contract2 = templates.create_from_template("supply_contract")
	contract2.parties = ["ИП Иванов", "ЗАО Петров"]
	contract2.amount = 250000

	contract1.display()
	contract2.display()
