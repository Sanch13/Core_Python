import math


class Vector:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = \
			y

	def __repr__(self):
		print("__repr__")
		return f"Vector({self.x!r}, {self.y!r})"

	def __abs__(self):
		print("__abs__")
		return math.hypot(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))

	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)

	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)


v = Vector(3, 4)
print(v)
print(abs(v))
