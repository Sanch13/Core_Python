"""
Меню ресторана (блюда и комплексные обеды)

"""
from abc import ABC, abstractmethod
from typing import List


class Dish(ABC):
	"""Basic interface for a dish"""

	def __init__(self, name: str, category: str) -> None:
		self.name = name
		self.category = category

	@abstractmethod
	def get_price(self) -> float:
		"""Get the cost of the dish"""
		pass

	@abstractmethod
	def show_details_dish(self) -> None:
		"""Show dish information"""
		pass


class Salad(Dish):
	"""Salad is a simple element"""

	def __init__(self, name: str, price: float) -> None:
		super().__init__(name, "Салат")
		self.price = price

	def get_price(self) -> float:
		return self.price

	def show_details_dish(self) -> None:
		print(f"Категория: {self.category} | Название: {self.name} "
			  f"Стоимость: {self.price} $")


class Soup(Dish):
	"""Суп - простой элемент"""

	def __init__(self, name: str, price: float, volume: int) -> None:
		super().__init__(name, "Soup")
		self.price = price
		self.volume = volume

	def get_price(self) -> float:
		return self.price

	def show_details_dish(self) -> None:
		print(f"Категория: {self.category} | Название: {self.name} "
			  f"Объем: {self.volume} "
			  f"Стоимость: {self.price} $")


class MainCourse(Dish):
	"""The main dish is a simple element"""
	def __init__(self, name: str, price: float, weight: int) -> None:
		super().__init__(name, "Main dish")
		self.price = price
		self.weight = weight

	def get_price(self) -> float:
		return self.price

	def show_details_dish(self) -> None:
		print(f"Категория: {self.category} | Название: {self.name} "
			  f"Вес: {self.weight} "
			  f"Стоимость: {self.price} $")


class Lunch(Dish):
	"""Complex lunch is a component (Composite)"""

	def __init__(self, name: str) -> None:
		super().__init__(name, "Complex lunch")
		self._dishes: List[Dish] = []

	def add_dish(self, dish: Dish) -> None:
		"""Add a dish to a specific set meal"""
		self._dishes.append(dish)

	def remove_dish(self, dish: Dish) -> None:
		"""Remove a dish from a set meal"""
		self._dishes.remove(dish)

	def get_price(self) -> float:
		"""Get the total cost of a set meal"""
		return sum(p.get_price() for p in self._dishes)

	def show_details_dish(self) -> None:
		"""Show the structure of set meals"""
		print(f"Комплексный обед: {self.name} ")
		print(f"Общая стоимость: {self.get_price()} $")
		for dish in self._dishes:
			dish.show_details_dish()
		print()


class Menu(Dish):
	"""Main menu"""
	def __init__(self, name: str) -> None:
		super().__init__(name, "Main menu")
		self._items: List[Dish] = []

	def add_item(self, dish: Dish) -> None:
		"""Add item to menu"""
		self._items.append(dish)

	def remove_item(self, dish: Dish) -> None:
		"""Remove item from menu"""
		self._items.remove(dish)

	def get_price(self) -> float:
		"""Get the total cost of all menu items"""
		return sum(item.get_price() for item in self._items)

	def show_details_dish(self) -> None:
		print(f"📋 {self.name}")
		print(f"  Всего позиций: {len(self._items)}")
		print(f"  Общая стоимость: {self.get_price():.2f} $")

		for item in self._items:
			item.show_details_dish()
			print()


if __name__ == "__main__":
	salad_1 = Salad("Salad Caprese", 130)
	salad_2 = Salad("Ceaser Salad",  150)
	salad_3 = Salad("Waldorf Salad", 160)

	soup_1 = Soup("Heartiest", price=100.99, volume=250)
	soup_2 = Soup("Mushroom Soup with Tofu", price=250.99, volume=250)
	soup_3 = Soup("Matzo Ball Soup", price=175.99, volume=250)

	main_1 = MainCourse("Стейк Рибай", 450.0, 300)
	main_2 = MainCourse("Лосось на гриле", 380.0, 250)

	lunch_1 = Lunch("Haute Horizon")
	lunch_1.add_dish(soup_1)
	lunch_1.add_dish(salad_1)
	lunch_1.add_dish(main_1)

	lunch_2 = Lunch("Royale Blossom")
	lunch_2.add_dish(soup_2)
	lunch_2.add_dish(salad_3)
	lunch_2.add_dish(main_2)

	menu = Menu("Обеденное меню ресторана")
	menu.add_item(lunch_1)
	menu.add_item(lunch_2)
	menu.add_item(salad_2)

	menu.show_details_dish()















