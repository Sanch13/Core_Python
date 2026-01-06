"""
Попробуй написать систему для рисования фигур на разных платформах:
Реализации (платформы):
VectorRenderer — векторная графика
RasterRenderer — растровая графика

Абстракции (фигуры):
Circle — круг
Square — квадрат

Каждая фигура должна уметь draw(), используя выбранный рендерер.
Подсказка: Структура будет похожа на пример выше, только вместо send() будет draw().
"""

from abc import ABC, abstractmethod


class Renderer(ABC):
	@abstractmethod
	def render_circle(self, radius: float) -> None:
		pass

	@abstractmethod
	def render_square(self, side: float) -> None:
		pass

	@abstractmethod
	def render_triangle(self, base: float) -> None:
		pass


class VectorRenderer(Renderer):
	def render_circle(self, radius: float) -> None:
		print(f"VectorRenderer отрисовал circle with radius={radius}")

	def render_square(self, side: float) -> None:
		print(f"VectorRenderer отрисовал square with side={side}")

	def render_triangle(self, base: float) -> None:
		print(f"VectorRenderer отрисовал triangle with base={base}")


class RasterRenderer(Renderer):
	def render_circle(self, radius: float) -> None:
		print(f"RasterRenderer отрисовал circle with radius={radius}")

	def render_square(self, side: float) -> None:
		print(f"RasterRenderer отрисовал square with side={side}")

	def render_triangle(self, base: float) -> None:
		print(f"RasterRenderer отрисовал triangle with base={base}")


class Figure(ABC):
	def __init__(self, renderer: Renderer) -> None:
		self.renderer = renderer

	@abstractmethod
	def draw(self):
		pass


class Triangle(Figure):
	def __init__(self, renderer: Renderer, base: float) -> None:
		super().__init__(renderer)
		self.base = base

	def draw(self):
		self.renderer.render_triangle(base=self.base)


class Circle(Figure):
	def __init__(self, renderer: Renderer, radius: float) -> None:
		super().__init__(renderer)
		self.radius = radius

	def draw(self):
		self.renderer.render_circle(radius=self.radius)


class Square(Figure):
	def __init__(self, renderer: Renderer, side: float) -> None:
		super().__init__(renderer)
		self.side = side

	def draw(self):
		self.renderer.render_square(side=self.side)


if __name__ == '__main__':
	vector = VectorRenderer()
	raster = RasterRenderer()

	vector_circle = Circle(renderer=vector, radius=0.5)
	vector_circle.draw()
	raster_circle = Circle(renderer=raster, radius=2.5)
	raster_circle.draw()

	vector_square = Square(renderer=vector, side=0.5)
	vector_square.draw()
	raster_square = Square(renderer=raster, side=2.5)
	raster_square.draw()

	vector_triangle = Triangle(renderer=vector, base=3.5)
	vector_triangle.draw()
	raster_triangle = Triangle(renderer=raster, base=5.5)
	raster_triangle.draw()


