"""
Фасад для системы онлайн-заказа (корзина + оплата + доставка + уведомления)
"""


class User:
	"""User"""

	def __init__(self, name: str, balance: int, address: str):
		self._name = name
		self._balance = balance
		self._address = address

	def get_balance(self) -> int:
		"""Get balance user"""
		return self._balance

	def change_balance(self, amount: int) -> None:
		"""Change user balance"""
		self._balance -= amount

	def get_address(self) -> str:
		return self._address

	def get_name(self) -> str:
		return self._name


class Product:
	"""Product"""

	def __init__(self, name: str, price: int) -> None:
		self._name = name
		self._price = price

	def get_name(self) -> str:
		return self._name

	def get_price(self) -> int:
		return self._price


class Cart:
	"""Shopping cart"""

	def __init__(self):
		self._products: list[Product] = []

	def add_product(self, product: Product) -> None:
		"""Add product to cart"""
		self._products.append(product)

	def remove_product(self, product: Product) -> None:
		"""Remove product from cart"""
		if product in self._products:
			self._products.remove(product)

	def total_price_cart(self) -> int:
		"""Get total price all products"""
		return sum(p.get_price() for p in self._products)

	def get_all_products(self) -> list[Product]:
		return self._products.copy()

	def clear_cart(self) -> None:
		self._products.clear()


class Payment:
	"""Payment"""

	def __init__(self, user: User, cart: Cart):
		self._user = user
		self._cart = cart

	def pay_all_products_from_cart(self) -> None:
		"""Pay all product from cart"""
		user_balance = self._user.get_balance()
		total = self._cart.total_price_cart()
		if user_balance < total:
			raise ValueError(f"Insufficient balance. Need {total}. User balance {user_balance}")

		self._user.change_balance(amount=total)

	def get_user_address_and_products(self) -> tuple[str, list[Product]]:
		address = self._user.get_address()
		products = self._cart.get_all_products()
		return address, products


class Delivery:
	"""Delivery"""

	def delivery_products_by_address(self, payment: Payment) -> None:
		address, products = payment.get_user_address_and_products()
		print(f"Delivery products:[{[p.get_name() for p in products]}] to the address: {address}")


class Notification:
	"""Notification"""

	def __init__(self, user: User):
		self._user = user

	def send_message(self) -> None:
		print(f"All products will delivery person {self._user.get_name()} to the address {self._user.get_address()}")


class OnlineOrderProductsFacade:
	"""Order products by online with notification"""

	def __init__(self, user: User, cart: Cart):
		self._user = user
		self._cart = cart
		self._payment = Payment(self._user, self._cart)
		self._delivery = Delivery()
		self._notification = Notification(self._user)

	def payment_products_online(self):
		print("\n🎯 Payments for products...\n")

		try:
			total = self._cart.total_price_cart()

			self._process_payment(total)

			self._process_delivery()

			self._cart.clear_cart()
			print("Cart is empty !!!")

			self._send_notification()

		except ValueError as e:
			print(f"Payment error {e}")
			raise
		except Exception as e:
			print(f"Error {e}")
			raise

	def _process_payment(self, total):
		self._payment.pay_all_products_from_cart()
		print("Payments successful !!!")
		print(f"Total price: {total} $")

	def _process_delivery(self):
		self._delivery.delivery_products_by_address(self._payment)
		print("Delivery is successful !!!")

	def _send_notification(self):
		self._notification.send_message()
		print("Notification send successfully !!!")


# Клиентский код
if __name__ == "__main__":
	p1 = Product("TV", 1500)
	p2 = Product("SmartPhone", 700)
	p3 = Product("Chair", 300)

	alex_cart = Cart()
	alex_cart.add_product(p1)
	alex_cart.add_product(p2)
	alex_cart.add_product(p3)

	alex = User("Alex", 2500, "Wall Street 232")

	online_order = OnlineOrderProductsFacade(alex, alex_cart)
	online_order.payment_products_online()

