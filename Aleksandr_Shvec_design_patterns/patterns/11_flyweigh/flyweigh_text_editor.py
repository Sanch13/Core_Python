"""
Задание: Текстовый редактор с форматированием
Контекст:
Ты создаёшь упрощённый текстовый редактор (как Google Docs). В документе тысячи символов, и
многие из них имеют одинаковое форматирование (шрифт, размер, цвет, стиль).
Проблема без Flyweight:
10,000 символов × (шрифт + размер + цвет + жирность + курсив) = огромное дублирование данных

Решение с Flyweight:
Форматирование хранится отдельно и переиспользуется

📋 Структура классов:
1. CharacterStyle (Flyweight - легковес)
Назначение: Stores shared formatting properties
Хранит:

font: str — название шрифта (например, "Arial", "Times New Roman")
size: int — размер шрифта (12, 14, 16)
color: str — цвет текста ("black", "red", "blue")
bold: bool — жирный текст
italic: bool — курсив

Методы:
__init__(...) — Initialize character style with formatting properties
apply(character: str, position: int) -> None — Display character with this style at position


2. StyleFactory (Фабрика легковесов)
Назначение: Manages creation and reuse of CharacterStyle objects
Хранит:
_styles: dict[tuple, CharacterStyle] — кэш стилей (ключ = кортеж всех параметров)

Методы:
get_style(font, size, color, bold, italic) -> CharacterStyle — Returns existing style or creates new one
get_total_styles() -> int — Returns number of unique styles created


3. Character (Контекст)
Назначение: Represents a single character in the document with unique data
Хранит:
char: str — сам символ ('a', 'b', 'c', ...)
position: int — позиция в документе (0, 1, 2, ...)
style: CharacterStyle — ссылка на объект стиля (flyweight)

Методы:
__init__(char, position, style) — Initialize character with its unique properties
render() -> None — Render this character with its style

4. Document (Клиент)
Назначение: Manages all characters in the text document
Хранит:
characters: list[Character] — список всех символов в документе

Методы:
add_text(text: str, font, size, color, bold, italic) -> None — Add formatted text to document
render() -> None — Render entire document
show_statistics() -> None — Display memory usage statistics

🎯 Требования к реализации:

Используй @dataclass(frozen=True) для CharacterStyle
В StyleFactory ключ словаря — кортеж всех параметров форматирования
Метод add_text() должен:

Принимать строку текста
Получать стиль через фабрику
Создавать Character для каждого символа
Автоматически определять позицию (текущая длина документа)

Создай тестовые данные:

Заголовок (Arial, 24, black, bold, не курсив)
Обычный текст (Times New Roman, 12, black, не bold, не курсив)
Выделенная цитата (Times New Roman, 12, blue, не bold, italic)
Важное предупреждение (Arial, 14, red, bold, не курсив)

Добавь минимум 200 символов чтобы увидеть эффект переиспользования
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CharacterStyle:
	"""Stores shared formatting properties"""

	font: str
	size: int
	color: str
	bold: bool
	italic: bool

	def apply(self, character: str, position: int) -> None:
		"""Display character with this style at position"""
		style_info = f"font={self.font}, size={self.size}, color={self.color}"
		formatting = []
		if self.bold:
			formatting.append("BOLD")
		if self.italic:
			formatting.append("ITALIC")

		format_str = f" [{', '.join(formatting)}]" if formatting else ""
		print(f"'{character}' at pos {position} ({style_info}){format_str}")



class StyleFactory:
	"""Manages creation and reuse of CharacterStyle objects"""

	_styles: dict[tuple[str, int, str, bool, bool], CharacterStyle] = {}

	@classmethod
	def get_style(
			cls,
			font: str,
			size: int,
			color: str,
			bold: bool,
			italic: bool,
	) -> CharacterStyle:
		"""Returns existing style or creates new one"""

		key = (font, size, color, bold, italic)

		if key not in cls._styles:
			print(f"[Factory] Create new CharacterStyle")
			cls._styles[key] = CharacterStyle(font, size, color, bold, italic)
		else:
			print(f"[Factory] Reuse exist CharacterStyle")

		return cls._styles[key]

	@classmethod
	def get_total_styles(cls) -> int:
		"""Returns number of unique styles created"""
		return len(cls._styles)


class Character:
	"""Represents a single character in the document with unique data"""

	def __init__(self, char: str, position: int, style: CharacterStyle):
		self.char = char
		self.position = position
		self.style = style

	def render(self) -> None:
		"""Render this character with its style"""
		self.style.apply(self.char, self.position)


class Document:
	"""Manages all characters in the text document"""

	def __init__(self):
		self.characters: list[Character] = []

	def add_text(
			self,
			text: str,
			font: str,
			size: int,
			color: str,
			bold: bool,
			italic: bool
	) -> None:
		"""Add formatted text to document"""

		character_style = StyleFactory.get_style(font, size, color, bold, italic)

		for char in text:
			position = len(self.characters)
			character = Character(char, position, character_style)
			self.characters.append(character)

	def render(self) -> None:
		"""Render entire document"""
		print("\n" + "=" * 70)
		print("DOCUMENT PREVIEW")
		print("=" * 70)

		# Show full text
		text = ''.join(char.char for char in self.characters)
		print(text)

		print("\n" + "=" * 70)
		print("DETAILED CHARACTER INFO (first 50 characters)")
		print("=" * 70 + "\n")

		# Show details for first 50 characters
		for char in self.characters[:50]:
			char.render()

		if len(self.characters) > 50:
			print(f"\n... and {len(self.characters) - 50} more characters")

	def show_statistics(self) -> None:
		"""Display memory usage statistics"""
		print(f"\n{'=' * 60}")
		print(f"All character: {len(self.characters)}")
		print(f"All unique style characters: {StyleFactory.get_total_styles()}")
		print(f"All memory:  {len(self.characters)} objects of the CharacterStyle "
		      f"Only use {StyleFactory.get_total_styles()}")
		print(f"{'=' * 60}\n")


if __name__ == "__main__":
	doc = Document()

	# Заголовок
	doc.add_text("Chapter 1: Introduction",
	             font="Arial", size=24, color="black", bold=True, italic=False)

	# Обычный текст
	doc.add_text("\nThis is a regular paragraph with normal formatting. ",
	             font="Times New Roman", size=12, color="black", bold=False, italic=False)

	# Цитата
	doc.add_text("'The only way to do great work is to love what you do.' ",
	             font="Times New Roman", size=12, color="blue", bold=False, italic=True)

	# Предупреждение
	doc.add_text("\nWARNING: Important information! ",
	             font="Arial", size=14, color="red", bold=True, italic=False)

	# Ещё обычный текст (должен переиспользовать стиль!)
	doc.add_text("This text uses the same style as the first paragraph.",
	             font="Times New Roman", size=12, color="black", bold=False, italic=False)

	# Рендеринг и статистика
	doc.render()
	doc.show_statistics()