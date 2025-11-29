"""
Прототип — это порождающий паттерн проектирования, который позволяет копировать объекты,
не вдаваясь в подробности их реализации.
"""
import copy
from abc import ABC, abstractmethod


# Абстрактный прототип
class Enemy(ABC):
	def __init__(self, name: str, health: int, damage: int):
		self.name = name
		self.health = health
		self.damage = damage
		self.position = [0, 0]  # Изменяемый атрибут

	@abstractmethod
	def clone(self):
		"""Метод клонирования (обязательный для прототипа)"""
		pass

	def __str__(self):
		return (f"{self.name}: HP={self.health}, DMG={self.damage}, "
				f"Pos={self.position}")


# Конкретные прототипы
class Goblin(Enemy):
	def __init__(self):
		super().__init__("Goblin", health=50, damage=10)

	def clone(self):
		return copy.deepcopy(self)


class Dragon(Enemy):
	def __init__(self):
		super().__init__("Dragon", health=500, damage=100)
		self.can_fly = True  # Дополнительный атрибут

	def clone(self):
		return copy.deepcopy(self)


# Менеджер прототипов (опционально, но удобно)
class EnemyFactory:
	def __init__(self):
		self._prototypes = {}

	def register_prototype(self, key: str, prototype: Enemy):
		"""Регистрируем базовый прототип"""
		self._prototypes[key] = prototype

	def create(self, key: str) -> Enemy:
		"""Создаём врага клонированием"""
		if key not in self._prototypes:
			raise ValueError(f"Прототип '{key}' не найден")
		return self._prototypes[key].clone()


# Использование
if __name__ == "__main__":
	# Создаём фабрику и регистрируем прототипы
	factory = EnemyFactory()
	factory.register_prototype("goblin", Goblin())
	factory.register_prototype("dragon", Dragon())

	# Клонируем врагов
	enemy1 = factory.create("goblin")
	enemy2 = factory.create("goblin")
	enemy3 = factory.create("dragon")

	# Модифицируем клонов независимо
	enemy1.position = [10, 20]
	enemy2.position = [30, 40]
	enemy2.health = 30  # Ранен

	print(enemy1)  # Goblin: HP=50, DMG=10, Pos=[10, 20]
	print(enemy2)  # Goblin: HP=30, DMG=10, Pos=[30, 40]
	print(enemy3)  # Dragon: HP=500, DMG=100, Pos=[0, 0]

	# Проверяем, что это разные объекты
	print(f"enemy1 is enemy2: {enemy1 is enemy2}")  # False
