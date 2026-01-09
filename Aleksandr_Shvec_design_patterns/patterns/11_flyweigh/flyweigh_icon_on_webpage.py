"""
Задание: Система иконок на веб-странице
Контекст задачи:
У тебя есть веб-приложение (например, социальная сеть или интернет-магазин). На странице сотни
иконок: лайки, корзины, уведомления, звёздочки рейтинга и т.д.
Что нужно реализовать:
Создай систему управления иконками используя паттерн Flyweight:

Класс IconType (легковес) — хранит общие данные иконки:
название (например, "heart", "cart", "bell")
SVG-код или emoji представление
размер по умолчанию
цвет по умолчанию


Класс IconFactory (фабрика) — управляет созданием и переиспользованием типов иконок
Класс Icon (контекст) — конкретная иконка на странице:
позиция (x, y)
ссылка на IconType
возможно tooltip (подсказка при наведении)


Класс WebPage (клиент) — веб-страница с иконками:
добавление иконок
рендеринг всех иконок
показ статистики



Минимальные требования:
Создай хотя бы 3 типа иконок (например: heart/лайк, cart/корзина, bell/уведомление)
Размести на странице минимум 10 иконок (несколько одинаковых типов)
Покажи, что типы переиспользуются через фабрику
Выведи статистику (сколько иконок, сколько уникальных типов)
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class IconType:
	"""Flyweight — stores shared icon data"""

	name: str
	svg: str
	size: tuple[int, int] = (20, 20)
	color: str = "black"

	def draw(self, x: int, y: int) -> None:
		"""Draw icon at specific position"""
		print(f"Draw {self.svg} [{self.name}] "
		      f"size={self.size}, color={self.color} at ({x}, {y})")



class IconFactory:
	"""Factory for managing and reusing IconType objects"""

	_icon_types: dict[tuple[str, str, tuple[int, int], str], IconType] = {}

	@classmethod
	def get_icon_type(
			cls,
			name: str,
			svg: str,
			size: tuple[int, int] = (20, 20),
			color: str = "black"
	) -> IconType:
		"""Returns existing IconType or creates new one if not exists"""

		key = (name, svg, size, color)

		if key not in  cls._icon_types:
			print(f"[Factory] Create new IconType: {name}")
			cls._icon_types[key] = IconType(name, svg, size, color)
		else:
			print(f"[Factory] Reuse exist IconType: {name}")

		return cls._icon_types[key]

	@classmethod
	def get_total_types(cls) -> int:
		"""Returns the number of unique icon types created"""
		return len(cls._icon_types)


class Icon:
	"""Context — represents a specific icon instance on the page with unique position"""

	def __init__(self, x: int, y: int, icon_type: IconType, tooltip: str = "" ):
		self.x = x
		self.y = y
		self.icon_type = icon_type
		self.tooltip = tooltip


	def draw(self) -> None:
		self.icon_type.draw(self.x, self.y)
		if self.tooltip:
			print(f"  └─ Tooltip: '{self.tooltip}'")


class WebPage:
	"""Client — manages icons on the web page"""

	def __init__(self):
		self.icons: list[Icon] = []

	def add_icon(
			self,
			x: int,
			y: int,
			name: str,
			svg: str,
			size: tuple[int, int] = (20, 20),
			color: str = "black",
			tooltip: str = ""
	):
		"""Add icon to list icons"""

		icon_type = IconFactory.get_icon_type(name, svg, size, color)
		icon = Icon(x, y, icon_type, tooltip)
		self.icons.append(icon)

	def render(self) -> None:
		"""Render all icons"""
		for icon in self.icons:
			icon.draw()

	def show_stats(self) -> None:
		"""Show statistics"""
		print(f"\n{'=' * 60}")
		print(f"All icons: {len(self.icons)}")
		print(f"All unique type icons: {IconFactory.get_total_types()}")
		print(f"All memory:  {len(self.icons)} objects of the IconTypes "
		      f"Only use {IconFactory.get_total_types()}")
		print(f"{'=' * 60}\n")


if __name__ == "__main__":
	page = WebPage()

	print("=" * 70)
	print("СОЗДАНИЕ ИКОНОК НА СТРАНИЦЕ")
	print("=" * 70 + "\n")

	# --- ХЕДЕР САЙТА ---
	print("📍 Добавляем иконки в хедер:\n")
	page.add_icon(10, 10, "bell", "🔔", size=(24, 24), color="red")
	page.add_icon(50, 10, "cart", "🛒", size=(24, 24), color="blue")
	page.add_icon(90, 10, "user", "👤", size=(24, 24), color="gray")

	# --- КАРТОЧКИ ТОВАРОВ (много одинаковых иконок) ---
	print("\n📍 Добавляем иконки в карточки товаров:\n")

	# Карточка 1
	page.add_icon(100, 100, "heart", "❤️", size=(20, 20), color="red")
	page.add_icon(130, 100, "cart", "🛒", size=(20, 20), color="blue")

	# Карточка 2
	page.add_icon(100, 150, "heart", "❤️", size=(20, 20), color="red")
	page.add_icon(130, 150, "cart", "🛒", size=(20, 20), color="blue")

	# Карточка 3
	page.add_icon(100, 200, "heart", "❤️", size=(20, 20), color="red")
	page.add_icon(130, 200, "cart", "🛒", size=(20, 20), color="blue")

	# Карточка 4
	page.add_icon(100, 250, "heart", "❤️", size=(20, 20), color="red")
	page.add_icon(130, 250, "cart", "🛒", size=(20, 20), color="blue")

	# --- РЕЙТИНГ (звёздочки) ---
	print("\n📍 Добавляем звёздочки рейтинга:\n")
	for i in range(5):
		page.add_icon(200 + i * 25, 300, "star", "⭐", size=(16, 16), color="gold")

	# --- ФУТЕР ---
	print("\n📍 Добавляем соцсети в футер:\n")
	page.add_icon(10, 500, "facebook", "📘", size=(32, 32), color="blue")
	page.add_icon(50, 500, "twitter", "🐦", size=(32, 32), color="lightblue")
	page.add_icon(90, 500, "instagram", "📷", size=(32, 32), color="purple")

	# --- РЕНДЕРИНГ И СТАТИСТИКА ---
	page.render()
	page.show_stats()