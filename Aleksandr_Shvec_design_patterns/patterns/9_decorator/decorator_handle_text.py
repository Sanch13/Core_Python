"""
📝 Задание: Система обработки текста
Контекст:
Ты разрабатываешь текстовый редактор. У тебя есть базовый текст, и нужно применять к
нему различные преобразования.

Требования:

Базовый компонент: класс PlainText — просто хранит и возвращает текст как есть
Создай декораторы:

UpperCaseDecorator — преобразует текст в ВЕРХНИЙ РЕГИСТР
TrimDecorator — удаляет пробелы в начале и конце
HtmlDecorator — оборачивает текст в HTML-теги <p>...</p>
MarkdownDecorator — оборачивает текст в маркдаун: **текст**
PrefixDecorator — добавляет префикс в начало (например, ">>> ")


Интерфейс: все классы должны иметь метод get_content() -> str
Демонстрация: покажи минимум 3 разные комбинации декораторов
Правильная структура (интерфейс → компонент → базовый декоратор → конкретные декораторы)

Дополнительный уровень сложности (если хочешь):
Добавь декоратор CensorDecorator, который:

Принимает список запрещённых слов
Заменяет их на ***
"""

from abc import ABC, abstractmethod


# 1. Базовый интерфейс
class Text(ABC):
	@abstractmethod
	def get_content(self) -> str:
		pass


# 2. Конкретный компонент
class PlainText(Text):
	def __init__(self, text: str):
		self.text = text

	def get_content(self) -> str:
		return self.text


# 3. Базовый декоратор
class TextDecorator(Text):
	def __init__(self, txt: Text):
		self._txt = txt

	def get_content(self) -> str:
		return self._txt.get_content()


# 4. Конкретные декораторы
class UpperCaseDecorator(TextDecorator):
	def get_content(self) -> str:
		return self._txt.get_content().upper()


class TrimDecorator(TextDecorator):
	def get_content(self) -> str:
		return self._txt.get_content().strip()


class HtmlDecorator(TextDecorator):
	def get_content(self) -> str:
		return f"<p>{self._txt.get_content()}</p>"


class MarkdownDecorator(TextDecorator):
	def get_content(self) -> str:
		return f"**{self._txt.get_content()}**"


class PrefixDecorator(TextDecorator):
	def __init__(self, txt: Text, prefix: str = ">>> "):
		super().__init__(txt)
		self._prefix = prefix

	def get_content(self) -> str:
		return f"{self._prefix}{self._txt.get_content()}"


class CensorDecorator(TextDecorator):
	def __init__(self, txt: Text, words: list[str]):
		super().__init__(txt)
		self._words = words

	def get_content(self) -> str:
		text1 = ["***" if word in self._words else word for word in self._txt.get_content().split()]
		return " ".join(text1)


if __name__ == "__main__":
	print()
	# Базовый текст
	text = PlainText("  hello world  ")
	print(text.get_content())

	text = UpperCaseDecorator(PlainText("  hello world  "))
	print(text.get_content())

	# С одним декоратором
	text = TrimDecorator(PlainText("  hello world  "))
	print(text.get_content())
	# Вывод: "hello world"

	# С несколькими декораторами
	text = HtmlDecorator(UpperCaseDecorator(TrimDecorator(PlainText("  hello world  "))))
	print(text.get_content())
	# Вывод: "<p>HELLO WORLD</p>"

	# Другая комбинация
	text = PrefixDecorator(MarkdownDecorator(PlainText("important")), prefix="NOTE: ")
	print(text.get_content())
	# Вывод: "NOTE: **important**"

	# Другая комбинация
	text = PrefixDecorator(HtmlDecorator(PlainText("awefae rgqew")))
	print(text.get_content())

	text = CensorDecorator(
		PlainText("This is bad and ugly text"),
		words=["bad", "ugly"]
	)
	print(text.get_content())

	text = PrefixDecorator(PrefixDecorator(PlainText("test"), ">> "), ">> ")
	print(text.get_content())
