import pytest
from _Other_practice_python.OOP_real_tasks.order_system import Order, OrderItem, Customer, Address, OrderStatus, PercentageDiscount, \
	FixedAmount, ItemsExistValidator, MinimumOrderValidator, RegionValidator, RegionalTaxCalculator, \
	FlatTaxCalculator, WeightBasedShipping, FreeShippingAboveAmount, OrderProcessor, \
	PromoCodeDiscount


@pytest.fixture
def sample_customer():
	"""Фикстура для создания тестового клиента"""
	address = Address("Minsk", "Test St", 123456)
	return Customer(1, "test@example.com", address)


@pytest.fixture
def sample_items():
	"""Фикстура для создания тестовых товаров"""
	return [
		OrderItem("Item1", 1, 2, 100, 500),
		OrderItem("Item2", 2, 1, 300, 800)
	]


@pytest.fixture
def sample_order(sample_customer, sample_items):
	return Order(1, sample_customer, sample_items)


class TestOrderItem:
	def test_subtotal_calculation(self):
		"""Проверяет расчет subtotal"""
		item = OrderItem("Laptop", 1, quantity=2, price=1000, weight=2000)
		assert item.subtotal == 2000  # 2 × 1000

	def test_subtotal_single_item(self):
		item = OrderItem("Mouse", 2, quantity=1, price=500, weight=100)
		assert item.subtotal == 500


class TestOrder:
	def test_items_total_price(self, sample_order):
		"""Проверяет расчет общей суммы товаров"""
		# (2 × 100) + (1 × 300) = 500
		assert sample_order.items_total_price == 500

	def test_total_weight(self, sample_order):
		"""Проверяет расчет общего веса"""
		# (2 × 500) + (1 × 800) = 1800
		assert sample_order.total_weight == 1800

	def test_final_total_with_discount_tax_shipping(self, sample_order):
		"""Проверяет финальную сумму с учетом скидки, налога, доставки"""
		sample_order.discount_amount = 50
		sample_order.tax_amount = 90
		sample_order.shipping_cost = 100

		# 500 - 50 + 90 + 100 = 640
		assert sample_order.final_total == 640


class TestPercentageDiscount:
	def test_10_percent_discount(self, sample_order):
		discount = PercentageDiscount(10)

		result = discount.calculate_discount(sample_order)
		assert result == 50  # 10% от 500

	def test_invalid_percentage_above_100(self):
		with pytest.raises(ValueError, match="Процент скидки должен быть от 0 до 100"):
			PercentageDiscount(150)

	def test_invalid_percentage_negative(self):
		with pytest.raises(ValueError):
			PercentageDiscount(-10)


class TestFixedAmount:
	def test_fixed_discount_within_order_total(self, sample_order):
		discount = FixedAmount(200)

		result = discount.calculate_discount(sample_order)
		assert result == 200

	def test_fixed_discount_exceeds_order_total(self, sample_order):
		discount = FixedAmount(1000)  # Больше чем 500

		result = discount.calculate_discount(sample_order)
		assert result == 500  # Ограничено суммой заказа


class TestPromoCodeDiscount:
	def test_20_percent_discount(self, sample_order):
		discount = PromoCodeDiscount("SUMMER2024", 20)  # ✅ Промокод!

		result = discount.calculate_discount(sample_order)
		assert result == 100  # 20% от 500

	def test_promo_code_stores_code(self):
		"""Проверяет, что промокод сохраняется"""
		discount = PromoCodeDiscount("WINTER2025", 15)
		assert discount.code == "WINTER2025"


class TestItemsExistValidator:
	def test_empty_order(self, sample_customer):
		order = Order(1, sample_customer, [])
		validator = ItemsExistValidator()

		with pytest.raises(ValueError, match="В заказе нет товаров"):
			validator.validate(order)


class TestMinimumOrderValidator:
	def test_minimum_order(self, sample_order):
		min_amount = 500
		validator = MinimumOrderValidator(min_amount)

		with pytest.raises(ValueError, match=f"Минимальная сумма заказа {min_amount} руб"):
			validator.validate(sample_order)


class TestRegionValidator:
	def test_valid_region_order(self, sample_order):
		validator = RegionValidator(["Minsk", "Moscow", "Kiev"])

		result = validator.validate(sample_order)
		assert result == True

	def test_invalid_region_order(self, sample_order):
		lst_city = ["Rostov"]
		city_delivery = sample_order.customer.address.city
		validator = RegionValidator(lst_city)

		with pytest.raises(ValueError, match=f"Доставка в {city_delivery} невозможна"):
			validator.validate(sample_order)


class TestRegionalTaxCalculator:
	def test_calculate_tax_with_exist_city(self, sample_order):
		tax_region_calculator = RegionalTaxCalculator({
			"Minsk": 20,
			"Moscow": 18,
			"Kiev": 15
		})
		tax_result = tax_region_calculator.calculate_tax(sample_order)

		assert tax_result == 100

	def test_calculate_tax_with_default_rate_for_unknown_city(self, sample_order):
		tax_region_calculator = RegionalTaxCalculator({"Kiev": 15})
		tax_result = tax_region_calculator.calculate_tax(sample_order)

		assert tax_result == 100


class TestFlatTaxCalculator:
	def test_calculate_tax_fix_tax(self, sample_order):
		tax_fix_calculator = FlatTaxCalculator(15)
		tax_result = tax_fix_calculator.calculate_tax(sample_order)

		assert tax_result == 75


class TestWeightBasedShipping:
	def test_calculate_shipping_default(self, sample_order):
		weight_calculator = WeightBasedShipping()
		price_delivery = weight_calculator.calculate_shipping(sample_order)

		assert price_delivery == 110


class TestFreeShippingAboveAmount:
	def test_calculate_shipping_free(self, sample_order):
		weight_calculator = WeightBasedShipping()
		threshold = 500
		calculator = FreeShippingAboveAmount(threshold, weight_calculator)
		price_delivery = calculator.calculate_shipping(sample_order)

		assert price_delivery == 0

	def test_calculate_shipping_not_free(self, sample_order):
		weight_calculator = WeightBasedShipping()
		threshold = 4000
		calculator = FreeShippingAboveAmount(threshold, weight_calculator)
		price_delivery = calculator.calculate_shipping(sample_order)

		assert price_delivery == 110


class TestOrderProcessor:
	def test_integration_process_order(self, sample_order):
		validators = [
			ItemsExistValidator(),
			MinimumOrderValidator(min_amount=400),
			RegionValidator(["Minsk", "Moscow", "Kiev"])
		]
		tax_calculator = RegionalTaxCalculator({
			"Minsk": 20,
			"Moscow": 18,
			"Kiev": 15
		})
		shipping_calculator = FreeShippingAboveAmount(
			threshold=5000,
		    fallback_calculator=WeightBasedShipping()
		)
		discount = PercentageDiscount(20)
		ord_poc = OrderProcessor(validators, tax_calculator, shipping_calculator)

		final_order = ord_poc.process_order(sample_order, discount)

		assert final_order.shipping_cost == 110
		assert final_order.tax_amount == 80
		assert final_order.discount_amount == 100
		assert final_order.final_total == 590
		assert final_order.status == OrderStatus.HANDLED
