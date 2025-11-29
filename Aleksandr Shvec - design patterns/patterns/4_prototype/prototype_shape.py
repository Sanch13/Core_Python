import copy
from abc import ABC, abstractmethod


class Shape(ABC):
	def __init__(self, x: int, y: int, color: str = "black"):
		self.x = x
		self.y = y
		self.color = color

	@abstractmethod
	def clone(self):
		pass

	@abstractmethod
	def draw(self):
		pass


class Circle(Shape):
	def __init__(self, x: int, y: int, radius: float, color: str = "red"):
		super().__init__(x=x, y=y, color=color)
		self.radius = radius

	def clone(self):
		return copy.deepcopy(self)

	def draw(self):
		print(f"Circle at ({self.x}, {self.y}) color={self.color} radius={self.radius}")


class Rectangle(Shape):
	def __init__(self, x: int, y: int, width: float, height: float, color: str = "black"):
		super().__init__(x=x, y=y, color=color)
		self.width = width
		self.height = height

	def clone(self):
		return copy.deepcopy(self)

	def draw(self):
		print(
			f"Rectangle at ({self.x}, {self.y}) color={self.color} width={self.width} height={self.height}")


class Triangle(Shape):
	def __init__(
			self,
			x: int,
			y: int,
			side_a: float,
			side_b: float,
			side_c: float,
			color: str = "blue"
	):
		super().__init__(x=x, y=y, color=color)
		self.side_a = side_a
		self.side_b = side_b
		self.side_c = side_c

	def clone(self):
		return copy.deepcopy(self)

	def draw(self):
		print(
			f"Triangle at ({self.x}, {self.y}) color={self.color} side_a={self.side_a} side_b={self.side_b} side_c={self.side_c}")


class ShapeFactory:
	def __init__(self):
		self._prototypes = {}

	def register(self, key: str, prototype: Shape):
		self._prototypes[key] = prototype.clone()

	def create(self, key: str, x: int = None, y: int = None) -> Shape:
		if key not in self._prototypes:
			raise ValueError(f"Прототип '{key}' не зарегистрирован")

		clone = self._prototypes[key].clone()
		if x is not None:
			clone.x = x
		if y is not None:
			clone.y = y
		return clone


if __name__ == '__main__':
	circle1 = Circle(x=10, y=20, radius=5)
	circle1.draw()
	circle2 = circle1.clone()
	circle2.x = 50
	circle2.y = 60
	circle2.draw()

	rectangle1 = Rectangle(x=10, y=20, width=5, height=5, color="blue")
	rectangle1.draw()
	rectangle2 = rectangle1.clone()
	rectangle2.x = 50
	rectangle2.y = 60
	rectangle2.color = "black"
	rectangle2.draw()

	triangle1 = Triangle(x=10, y=20, side_a=1, side_b=2, side_c=3)
	triangle1.draw()
	triangle2 = triangle1.clone()
	triangle2.x = 50
	triangle2.y = 60
	triangle2.color = "red"
	triangle2.draw()

	factory = ShapeFactory()
	factory.register("circle", Circle(x=10, y=20, radius=5))
	factory.register("rectangle", Rectangle(x=10, y=20, width=5, height=5, color="blue"))
	factory.register("triangle", Triangle(x=10, y=20, side_a=1, side_b=2, side_c=3))

	c1 = factory.create("circle")
	r1 = factory.create("rectangle")
	t1 = factory.create("triangle")
	c1.draw()
	r1.draw()
	t1.draw()
	c1.color = "green"
	r1.color = "yellow"
	t1.color = "violet"
	c1.draw()
	r1.draw()
	t1.draw()
