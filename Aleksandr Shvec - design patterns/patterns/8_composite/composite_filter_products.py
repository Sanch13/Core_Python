"""
## 📋 Техническое задание: Система фильтров для интернет-магазина

### 🎯 Цель:
Реализовать гибкую систему фильтрации товаров с возможностью комбинирования условий.
## 📦 Что нужно реализовать:

### 1. **Базовый класс `Filter` (Component)**
- Метод `apply(products: List[Product]) -> List[Product]` — фильтрует список товаров
### 2. **Простые фильтры (Leaf):**
**A) `PriceFilter`** — фильтрация по цене
- `min_price: float` — минимальная цена (включительно)
- `max_price: float` — максимальная цена (включительно)
**B) `CategoryFilter`** — фильтрация по категории
- `category: str` — название категории
**C) `BrandFilter`** — фильтрация по бренду
- `brands: List[str]` — список брендов (товар должен совпадать хотя бы с одним)
**D) `RatingFilter`** — фильтрация по рейтингу
- `min_rating: float` — минимальный рейтинг (от 0 до 5)

### 3. **Составные фильтры (Composite):**
**A) `AndFilter`** — логическое И (товар должен пройти ВСЕ фильтры)
- Может содержать список фильтров
- Методы: `add_filter()`, `remove_filter()`
**B) `OrFilter`** — логическое ИЛИ (товар должен пройти ХОТЯ БЫ ОДИН фильтр)
- Может содержать список фильтров
- Методы: `add_filter()`, `remove_filter()`

## 🏷️ Класс `Product`:
@dataclass
class Product:
    name: str
    price: float
    category: str
    brand: str
    rating: float  # от 0 до 5

## 📝 Примеры использования:

### Пример 1: Простой фильтр
```python
products = [
    Product("Nike Air Max", 8000, "Обувь", "Nike", 4.5),
    Product("Adidas Ultraboost", 12000, "Обувь", "Adidas", 4.8),
    Product("Puma T-Shirt", 2000, "Одежда", "Puma", 4.0),
]

# Фильтр: цена от 5000 до 10000
price_filter = PriceFilter(5000, 10000)
result = price_filter.apply(products)
# Результат: [Nike Air Max]
```

### Пример 2: Комбинация фильтров (И)
```python
# Фильтр: обувь И (Nike ИЛИ Adidas) И цена < 10000
and_filter = AndFilter()
and_filter.add_filter(CategoryFilter("Обувь"))
and_filter.add_filter(BrandFilter(["Nike", "Adidas"]))
and_filter.add_filter(PriceFilter(0, 10000))

result = and_filter.apply(products)
# Результат: [Nike Air Max]
```

### Пример 3: Вложенные фильтры
```python
# Фильтр: (Обувь И Nike) ИЛИ (рейтинг > 4.5)
or_filter = OrFilter()

shoes_nike = AndFilter()
shoes_nike.add_filter(CategoryFilter("Обувь"))
shoes_nike.add_filter(BrandFilter(["Nike"]))

or_filter.add_filter(shoes_nike)
or_filter.add_filter(RatingFilter(4.5))

result = or_filter.apply(products)
# Результат: [Nike Air Max, Adidas Ultraboost]
```

---

## ✅ Требования к коду:

1. **Использовать ABC и абстрактные методы**
2. **Type hints везде**
3. **Методы `add_filter()` и `remove_filter()` только в композитах**
4. **Чистый код**: хорошие имена, без дублирования
5. **Демонстрация работы** в `if __name__ == "__main__":`

---

## 🎁 Бонусное задание (опционально):

Добавь метод `describe()` в фильтры, который возвращает человекочитаемое описание:

```python
filter = AndFilter()
filter.add_filter(PriceFilter(1000, 5000))
filter.add_filter(BrandFilter(["Nike"]))

print(filter.describe())
# Вывод: "И: [Цена от 1000 до 5000 ₽, Бренд: Nike]"
```

## 🧪 Тестовые данные для проверки:
products = [
    Product("Nike Air Max", 8000, "Обувь", "Nike", 4.5),
    Product("Adidas Ultraboost", 12000, "Обувь", "Adidas", 4.8),
    Product("Puma T-Shirt", 2000, "Одежда", "Puma", 4.0),
    Product("Nike Hoodie", 6000, "Одежда", "Nike", 4.7),
    Product("Reebok Classic", 7000, "Обувь", "Reebok", 4.2),
    Product("Adidas Jacket", 9000, "Одежда", "Adidas", 4.6),
    Product("New Balance 574", 11000, "Обувь", "New Balance", 4.9),
]

Пиши код! После того как закончишь, я:
1. ✅ Проверю правильность реализации
2. 🧪 Протестирую на разных сценариях
3. 💡 Предложу улучшения
4. ❓ Задам вопросы для закрепления
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
	"""Class Product"""

	name: str
	price: float
	category: str
	brand: str
	rating: float  # от 0 до 5

	def __str__(self):
		return f"{self.category} {self.name}: {self.price:.2f} $"


class Filter(ABC):
	"""Base class Filter"""

	@abstractmethod
	def apply(self, products: list[Product]) -> list[Product]:
		"""Filter products"""
		pass

	@abstractmethod
	def describe(self) -> str:
		"""Show description"""
		pass


class PriceFilter(Filter):
	"""Class PriceFilter filter for price (leaf)"""

	def __init__(self, min_price: float, max_price: float) -> None:
		self.min_price = min_price
		self.max_price = max_price

	def apply(self, products: list[Product]) -> list[Product]:
		return list(
			filter(lambda product: self.min_price <= product.price <= self.max_price, products))

	def describe(self) -> str:
		return f"Price from {self.min_price} to {self.max_price} $"


class CategoryFilter(Filter):
	"""Class CategoryFilter filter for category (leaf)"""

	def __init__(self, category: str) -> None:
		self.category = category

	def apply(self, products: list[Product]) -> list[Product]:
		return list(filter(lambda product: product.category == self.category, products))

	def describe(self) -> str:
		return f"Category: {self.category}"


class BrandFilter(Filter):
	"""Class BrandFilter filter for brands (leaf)"""

	def __init__(self, brands: list[str]) -> None:
		self.brands = brands

	def apply(self, products: list[Product]) -> list[Product]:
		return list(filter(lambda product: product.brand in self.brands, products))

	def describe(self) -> str:
		return f"Brands {self.brands}"


class RatingFilter(Filter):
	"""Class RatingFilter filter for rating (leaf)"""

	def __init__(self, min_rating: float) -> None:
		self.min_rating = min_rating

	def apply(self, products: list[Product]) -> list[Product]:
		return list(filter(lambda product: product.rating >= self.min_rating, products))

	def describe(self) -> str:
		return f"Minimum ratings {self.min_rating}"


class AndFilter(Filter):
	"""Class AndFilter filter all filters (Composite)"""

	def __init__(self) -> None:
		self._filters = []

	def add_filter(self, filter: Filter) -> None:
		"""Add filter to _filters"""
		self._filters.append(filter)

	def remove_filter(self, filter: Filter) -> None:
		"""Remove filter from _filters"""
		self._filters.remove(filter)

	def apply(self, products: list[Product]) -> list[Product]:
		"""Filter in _filters all products"""
		if not self._filters:
			return products

		result = products
		for f in self._filters:
			result = f.apply(result)
		return result

	def describe(self) -> str:
		return f"AND: [{', '.join([f.describe() for f in self._filters])}]"


class OrFilter(Filter):
	"""Class OrFilter filter all filters (Composite)"""

	def __init__(self) -> None:
		self._filters = []

	def add_filter(self, filter: Filter) -> None:
		"""Add filter to _filters"""
		self._filters.append(filter)

	def remove_filter(self, filter: Filter) -> None:
		"""Remove filter from _filters"""
		self._filters.remove(filter)

	def apply(self, products: list[Product]) -> list[Product]:
		"""Filter in _filters all products"""
		if not self._filters:
			return products

		all_results = set()
		for f in self._filters:
			all_results.update(f.apply(products))

		return list(all_results)

	def describe(self) -> str:
		return f"OR: [{', '.join([f.describe() for f in self._filters])}]"


class NotFilter(Filter):
	"""Class NotFilter filter all filters (Composite)"""

	def __init__(self, filter: Filter) -> None:
		self._filter = filter

	def apply(self, products: list[Product]) -> list[Product]:
		"""Filter in _filters all products"""
		filtered = self._filter.apply(products)
		filtered_set = set(filtered)
		return list(p for p in products if p not in filtered_set)

	def describe(self) -> str:
		return f"NOT: [{self._filter.describe()}]"


if __name__ == "__main__":
	products = [
		Product("Nike Air Max", 8000, "Обувь", "Nike", 4.5),
		Product("Adidas Ultraboost", 12000, "Обувь", "Adidas", 4.8),
		Product("Puma T-Shirt", 2000, "Одежда", "Puma", 4.0),
		Product("Nike Hoodie", 6000, "Одежда", "Nike", 4.7),
		Product("Reebok Classic", 7000, "Обувь", "Reebok", 4.2),
		Product("Adidas Jacket", 9000, "Одежда", "Adidas", 4.6),
		Product("New Balance 574", 11000, "Обувь", "New Balance", 4.9),
	]

	print("=" * 80)
	print("ИСХОДНЫЕ ТОВАРЫ:")
	print("=" * 80)
	for p in products:
		print(f"  {p}")
	print()

	# ===== ПРИМЕР 1: Простой фильтр =====
	print("=" * 80)
	print("ПРИМЕР 1: Простой фильтр — Цена от 5000 до 10000 ₽")
	print("=" * 80)
	price_filter = PriceFilter(5000, 10000)
	result = price_filter.apply(products)
	print(f"Описание: {price_filter.describe()}")
	print(f"Найдено товаров: {len(result)}")
	for p in result:
		print(f"  ✓ {p}")
	print()

	# ===== ПРИМЕР 2: Фильтр AND =====
	print("=" * 80)
	print("ПРИМЕР 2: Комбинация AND — Обувь И (Nike ИЛИ Adidas) И цена < 10000")
	print("=" * 80)
	and_filter = AndFilter()
	and_filter.add_filter(CategoryFilter("Обувь"))
	and_filter.add_filter(BrandFilter(["Nike", "Adidas"]))
	and_filter.add_filter(PriceFilter(0, 10000))

	result = and_filter.apply(products)
	print(f"Описание: {and_filter.describe()}")
	print(f"Найдено товаров: {len(result)}")
	for p in result:
		print(f"  ✓ {p}")
	print()

	# ===== ПРИМЕР 3: Фильтр OR =====
	print("=" * 80)
	print("ПРИМЕР 3: Комбинация OR — Цена < 3000 ИЛИ Рейтинг ≥ 4.8")
	print("=" * 80)
	or_filter_simple = OrFilter()
	or_filter_simple.add_filter(PriceFilter(0, 3000))
	or_filter_simple.add_filter(RatingFilter(4.8))

	result = or_filter_simple.apply(products)
	print(f"Описание: {or_filter_simple.describe()}")
	print(f"Найдено товаров: {len(result)}")
	for p in result:
		print(f"  ✓ {p}")
	print()

	# ===== ПРИМЕР 4: Вложенная комбинация (AND внутри OR) =====
	print("=" * 80)
	print("ПРИМЕР 4: Сложная комбинация — (Обувь И Nike) ИЛИ (Рейтинг ≥ 4.7)")
	print("=" * 80)
	or_filter = OrFilter()

	# Ветка 1: Обувь И Nike
	shoes_nike = AndFilter()
	shoes_nike.add_filter(CategoryFilter("Обувь"))
	shoes_nike.add_filter(BrandFilter(["Nike"]))

	# Ветка 2: Рейтинг ≥ 4.7
	rating_filter = RatingFilter(4.7)

	# Объединяем ветки через OR
	or_filter.add_filter(shoes_nike)
	or_filter.add_filter(rating_filter)

	result = or_filter.apply(products)
	print(f"Описание: {or_filter.describe()}")
	print(f"Найдено товаров: {len(result)}")
	for p in result:
		print(f"  ✓ {p}")
	print()

	# ===== ПРИМЕР 5: Суперсложная комбинация =====
	print("=" * 80)
	print("ПРИМЕР 5: Суперсложная комбинация:")
	print("(Обувь И цена 7000-12000) ИЛИ (Одежда И Nike И рейтинг ≥ 4.5)")
	print("=" * 80)

	complex_filter = OrFilter()

	# Ветка 1: Обувь И цена 7000-12000
	branch1 = AndFilter()
	branch1.add_filter(CategoryFilter("Обувь"))
	branch1.add_filter(PriceFilter(7000, 12000))

	# Ветка 2: Одежда И Nike И рейтинг ≥ 4.5
	branch2 = AndFilter()
	branch2.add_filter(CategoryFilter("Одежда"))
	branch2.add_filter(BrandFilter(["Nike"]))
	branch2.add_filter(RatingFilter(4.5))

	complex_filter.add_filter(branch1)
	complex_filter.add_filter(branch2)

	result = complex_filter.apply(products)
	print(f"Описание: {complex_filter.describe()}")
	print(f"Найдено товаров: {len(result)}")
	for p in result:
		print(f"  ✓ {p}")
	print()


	not_nike = NotFilter(BrandFilter(["Nike"]))
	result = not_nike.apply(products)
	for p in result:
		print(f"  ✓ {p}")
	print()
	# Вернёт: [Adidas, Puma, Reebok, New Balance]


	# Пример 2: Все товары КРОМЕ дорогих (>10000)
	not_expensive = NotFilter(PriceFilter(10000, float('inf')))
	result = not_expensive.apply(products)
	for p in result:
		print(f"  ✓ {p}")
	print()
	# Вернёт: [все товары дешевле 10000]


	# Пример 3: Комбинация с AND
	# Обувь И НЕ (Nike ИЛИ Adidas)
	and_filter = AndFilter()
	and_filter.add_filter(CategoryFilter("Обувь"))

	brands_to_exclude = OrFilter()
	brands_to_exclude.add_filter(BrandFilter(["Nike"]))
	brands_to_exclude.add_filter(BrandFilter(["Adidas"]))

	and_filter.add_filter(NotFilter(brands_to_exclude))

	result = and_filter.apply(products)
	for p in result:
		print(f"  ✓ {p}")
	print()
	# Вернёт: [Reebok Classic, New Balance 574]
