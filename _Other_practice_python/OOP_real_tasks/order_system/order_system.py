"""
Теперь давай я придумаю задачу, которая:
1. Реалистична для прода
2. Требует архитектурного мышления
3. Легко масштабируется
4. Без многопоточности

---

## **Задача: Система обработки заказов интернет-магазина**

### **Контекст бизнеса:**
Ты разрабатываешь часть системы для интернет-магазина. Нужно реализовать **обработчик заказов**,
который принимает заказы и применяет к ним различные правила:
- Скидки (процентные, фиксированные, промокоды)
- Расчет налогов (могут отличаться по регионам)
- Расчет стоимости доставки (зависит от веса, региона, типа доставки)
- Валидация заказа (проверка наличия товара, минимальной суммы и т.д.)

**Важно:** В будущем компания планирует:
- Добавлять новые типы скидок
- Интегрироваться с внешними сервисами (проверка адреса, платежные системы)
- Поддерживать разные страны с разными правилами налогов
- Логировать все операции для аудита

---

### **Декомпозиция на подзадачи:**

Я разобью задачу на **5 подзадач**. Мы будем двигаться пошагово:

1. **Подзадача 1: Проектирование структуры данных**
   - Создай модели для Order (заказ), OrderItem (товар в заказе), Customer (клиент)
   - Подумай, какие атрибуты нужны каждой сущности

2. **Подзадача 2: Паттерн Strategy для скидок**
   - Реализуй систему применения скидок через паттерн Strategy
   - Создай интерфейс/абстрактный класс для скидок
   - Реализуй минимум 2 типа скидок

3. **Подзадача 3: Паттерн Chain of Responsibility для валидации**
   - Создай цепочку валидаторов
   - Каждый валидатор проверяет одно правило

4. **Подзадача 4: Главный процессор заказов**
   - Собери все компоненты в единый OrderProcessor
   - Реализуй метод `process_order()`, который применяет все операции

5. **Подзадача 5: Dependency Injection и тестируемость**
   - Сделай систему гибкой через внедрение зависимостей
   - Подготовь код к тестированию

---

### **Начнем с Подзадачи 1: Проектирование структуры данных**

**Твоя задача:**
Подумай и опиши (пока без кода), какие **классы/dataclasses** тебе понадобятся и какие **атрибуты** должны быть у каждого класса.

**Подсказки для размышления:**
- Что описывает заказ? (номер, клиент, список товаров, итоговая сумма?)
- Что нужно знать о товаре в заказе? (название, цена, количество?)
- Что нужно знать о клиенте? (имя, адрес, регион?)

**Важно:** Подумай о том, что в будущем может измениться. Например, может добавиться поле "способ оплаты" или "тип доставки".

Опиши своими словами структуру, и я дам фидбек перед тем, как ты начнешь писать код.
"""
from __future__ import annotations
from enum import StrEnum
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class Address:
	city: str
	street: str
	index: int


@dataclass(frozen=True)
class Customer:
	id: int
	email: str
	address: Address


@dataclass(frozen=True)
class OrderItem:
	name: str
	product_id: int
	quantity: int
	price: int
	weight: int

	@property
	def subtotal(self) -> int:
		return self.price * self.quantity


class OrderStatus(StrEnum):
	NEW = "new"
	HANDLED = "handled"
	CANCELED = "canceled"


class DiscountStrategy(ABC):

	@abstractmethod
	def calculate_discount(self, order: Order) -> int:
		pass


class Validator(ABC):

	def __init__(self):
		self._next_validator: Validator | None = None

	def validate(self, order: Order) -> bool:
		self._check(order)

		if self._next_validator:
			return self._next_validator.validate(order)

		return True

	def set_next(self, validator: Validator) -> Validator:
		self._next_validator = validator
		return validator

	@abstractmethod
	def _check(self, order: Order):
		pass


class TaxCalculator(ABC):
	@abstractmethod
	def calculate_tax(self, order: Order) -> int:
		"""Рассчитывает налог для заказа"""
		pass


class ShippingCalculator(ABC):
	@abstractmethod
	def calculate_shipping(self, order: Order) -> int:
		"""Рассчитывает стоимость доставки"""
		pass


@dataclass
class Order:
	id: int
	customer: Customer
	orders: list[OrderItem]
	discount_amount: int = 0
	tax_amount: int = 0
	shipping_cost: int = 0
	status: OrderStatus = OrderStatus.NEW

	@property
	def items_total_price(self) -> int:
		return sum(item.subtotal for item in self.orders) if self.orders else 0

	@property
	def final_total(self) -> int:
		return self.items_total_price - self.discount_amount + self.tax_amount + self.shipping_cost

	@property
	def total_weight(self) -> int:
		return sum(item.weight * item.quantity for item in self.orders)


class WeightBasedShipping(ShippingCalculator):
	def __init__(self, base_cost: int = 100, cost_per_kg: int = 10):
		self.base_cost = base_cost
		self.cost_per_kg = cost_per_kg

	def calculate_shipping(self, order: Order) -> int:
		weight_kg = order.total_weight // 1000
		return self.base_cost + (self.cost_per_kg * weight_kg)


class FreeShippingAboveAmount(ShippingCalculator):
	def __init__(self, threshold: int, fallback_calculator: ShippingCalculator):
		self.threshold = threshold
		self.fallback_calculator = fallback_calculator

	def calculate_shipping(self, order: Order) -> int:
		if order.items_total_price >= self.threshold:
			return 0
		else:
			return self.fallback_calculator.calculate_shipping(order)


class RegionalTaxCalculator(TaxCalculator):
	def __init__(self, tax_rates: dict[str, int]):
		self.tax_rates = tax_rates

	def calculate_tax(self, order: Order) -> int:
		city = order.customer.address.city
		tax_rate = self.tax_rates.get(city, 20)
		total_price_with_discount = order.items_total_price - order.discount_amount
		return total_price_with_discount * tax_rate // 100


class FlatTaxCalculator(TaxCalculator):
	def __init__(self, tax_rate: int):
		self.tax_rate = tax_rate

	def calculate_tax(self, order: Order) -> int:
		total_price_with_discount = order.items_total_price - order.discount_amount
		return total_price_with_discount * self.tax_rate // 100


class ItemsExistValidator(Validator):
	def _check(self, order: Order):
		if not order.orders:
			raise ValueError("В заказе нет товаров")


class MinimumOrderValidator(Validator):

	def __init__(self, min_amount: int):
		super().__init__()
		self.min_amount = min_amount

	def _check(self, order: Order):
		if order.items_total_price <= self.min_amount:
			raise ValueError(f"Минимальная сумма заказа {self.min_amount} руб")


class RegionValidator(Validator):

	def __init__(self, allowed_regions: list[str]):
		super().__init__()
		self.allowed_regions = allowed_regions

	def _check(self, order: Order):
		if order.customer.address.city not in self.allowed_regions:
			raise ValueError(f"Доставка в {order.customer.address.city} невозможна")


class PercentageDiscount(DiscountStrategy):

	def __init__(self, percentage: int):
		if not (0 <= percentage <= 100):
			raise ValueError("Процент скидки должен быть от 0 до 100")
		self.percentage = percentage

	def calculate_discount(self, order: Order) -> int:
		return order.items_total_price * self.percentage // 100


class FixedAmount(DiscountStrategy):

	def __init__(self, amount: int):
		if amount < 0:
			raise ValueError("Сумма скидки не может быть отрицательной")
		self.amount = amount

	def calculate_discount(self, order: Order) -> int:
		return min(self.amount, order.items_total_price)


class PromoCodeDiscount(DiscountStrategy):

	def __init__(self, code: str, percentage: int):
		self.code = code
		self.percentage = PercentageDiscount(percentage)

	def calculate_discount(self, order: Order) -> int:
		return self.percentage.calculate_discount(order)


class OrderProcessor:
	def __init__(
			self,
			validators: list[Validator],
			tax_calculator: TaxCalculator,
			shipping_calculator: ShippingCalculator
	):
		self.validators = validators
		self.tax_calculator = tax_calculator
		self.shipping_calculator = shipping_calculator


	def _apply_discount(self, order: Order, discount_strategy: DiscountStrategy) -> None:
		discount = discount_strategy.calculate_discount(order)
		order.discount_amount = discount

	def _validate_order(self, order: Order) -> bool:
		if not self.validators:
			raise ValueError("Список валидаторов пуст")

		for cur_val, next_val in zip(self.validators, self.validators[1:]):
			cur_val.set_next(next_val)

		self.validators[0].validate(order)
		return True

	def _calculate_tax(self, order: Order) -> None:
		order.tax_amount = self.tax_calculator.calculate_tax(order)

	def _cost_shipping(self, order: Order) -> None:
		order.shipping_cost = self.shipping_calculator.calculate_shipping(order)

	def process_order(
			self,
			order: Order,
			discount: DiscountStrategy | None = None
	):
		self._validate_order( order)

		if discount:
			self._apply_discount(order, discount)

		self._calculate_tax(order)

		self._cost_shipping(order)

		order.status = OrderStatus.HANDLED

		return order


if __name__ == '__main__':
	def print_order_info(order: Order, title: str = ""):
		if title:
			print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")
		print(
			f"Заказчик: {order.customer.email}\n"
			f"Сумма заказа: {order.items_total_price} руб\n"
			f"Скидка: {order.discount_amount} руб\n"
			f"Налог: {order.tax_amount} руб\n"
			f"Доставка: {order.shipping_cost} руб\n"
			f"Итого: {order.final_total} руб\n"
			f"Статус: {order.status.value}\n"
		)

	address = Address("Minsk", "Yellow street", 2312300)
	customer = Customer(1, "test@example.com", address)
	lst_product = [
		OrderItem("Phone", 1, 1, 1000, 200),
		OrderItem("TV", 2, 1, 1400, 800),
		OrderItem("Keyboard", 3, 1, 200, 300)
	]
	order = Order(1, customer, lst_product)
	# order_invalid = Order(2, customer, [OrderItem("Cheap item", 4, 1, 100, 50)])

	validators = [
		ItemsExistValidator(),
		MinimumOrderValidator(min_amount=500),
		RegionValidator(["Minsk", "Moscow", "Kiev"])
	]
	discount = PercentageDiscount(20)
	tax_calculator = RegionalTaxCalculator({
		"Minsk": 20,
		"Moscow": 18,
		"Kiev": 15
	})

	flat_tax = FlatTaxCalculator(10)

	weight_shipping = WeightBasedShipping(base_cost=100, cost_per_kg=10)
	free_shipping = FreeShippingAboveAmount(threshold=5000, fallback_calculator=weight_shipping)

	order_proc = OrderProcessor(
		validators=validators,
		tax_calculator=tax_calculator,
		shipping_calculator=free_shipping
	)

	try:
		print_order_info(order, "ДО ОБРАБОТКИ")
		processed_order = order_proc.process_order(
			order=order,
			discount=discount,
		)
		print_order_info(processed_order, "ПОСЛЕ ОБРАБОТКИ")
	except ValueError as e:
		print(f"Ошибка: {e}")
