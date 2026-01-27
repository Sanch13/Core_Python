"""
Техническое задание: Image Loading Proxy (Виртуальный Proxy)
Описание задачи
Тебе нужно реализовать систему для работы с изображениями, которая будет откладывать загрузку
тяжёлых изображений до момента, когда они действительно понадобятся (ленивая загрузка).
Жизненная аналогия: Представь галерею изображений на сайте. Если загружать все картинки сразу —
страница будет грузиться вечность. Вместо этого мы показываем превью (placeholder), а полное
изображение загружаем только когда пользователь на него кликает.

Структура классов
1. Image (абстрактный класс)
Назначение: Общий интерфейс для работы с изображениями.
Методы:

display() -> None — отобразить изображение
get_size() -> int — получить размер изображения в байтах
get_filename() -> str — получить имя файла


2. RealImage (реальный объект)
Назначение: Класс, который выполняет реальную загрузку изображения с диска/сервера.
Атрибуты:

_filename: str — имя файла
_data: bytes — данные изображения
_size: int — размер в байтах

Методы:

__init__(filename: str) — конструктор, который сразу загружает изображение
_load_from_disk() -> None — имитирует загрузку (с задержкой)
display() -> None — показывает изображение
get_size() -> int — возвращает размер
get_filename() -> str — возвращает имя файла


3. ImageProxy (виртуальный заместитель)
Назначение: Proxy, который откладывает создание RealImage до момента первого обращения.
Атрибуты:

_filename: str — имя файла
_real_image: Optional[RealImage] — ссылка на реальное изображение (изначально None)
_load_count: int — счётчик количества загрузок (для статистики)

Методы:

__init__(filename: str) — конструктор, который НЕ загружает изображение
display() -> None — создаёт RealImage при первом вызове, затем делегирует
get_size() -> int — создаёт RealImage если нужно, возвращает размер
get_filename() -> str — возвращает имя файла без загрузки изображения
is_loaded() -> bool — проверяет, загружено ли изображение
get_load_count() -> int — возвращает количество загрузок


Требования к реализации

Используй абстрактный базовый класс (ABC и abstractmethod)
RealImage.__init__ должен имитировать загрузку с задержкой (time.sleep(2))
ImageProxy.__init__ должен быть мгновенным (без загрузки)
Добавь логирование всех операций (загрузка, отображение)
Реализуй подсчёт загрузок для статистики
Английские docstrings для всех классов и методов
Код должен быть чистым и типизированным
"""
import time
from abc import ABC, abstractmethod


class Image(ABC):
	@abstractmethod
	def display(self) -> None: ...

	@abstractmethod
	def get_size(self) -> int: ...

	@abstractmethod
	def get_filename(self) -> str: ...


class RealImage(Image):
	IMAGE_DATABASE = {
		"photo1.jpg": {
			"size": 2048576,  # 2 MB
			"description": "Mountain landscape"
		},
		"photo2.jpg": {
			"size": 4194304,  # 4 MB
			"description": "Ocean sunset"
		},
		"photo3.jpg": {
			"size": 1048576,  # 1 MB
			"description": "City skyline"
		},
		"avatar.png": {
			"size": 524288,  # 512 KB
			"description": "User avatar"
		},
		"banner.jpg": {
			"size": 3145728,  # 3 MB
			"description": "Website banner"
		}
	}

	def __init__(self, filename: str):
		self._filename: str = filename
		self._load_from_disk()

	def _load_from_disk(self) -> None:
		"""Imitate loading from disk with latency."""
		print(f"[REAL IMAGE] Loading {self._filename} from disk... (this takes time)")
		time.sleep(2)
		print(f"[REAL IMAGE] Successfully loaded {self._filename} "
		      f"({self.IMAGE_DATABASE[self._filename]['size']} bytes)")

	def display(self) -> None:
		"""Display image"""
		data = self.IMAGE_DATABASE.get(self._filename)
		print(f"[REAL IMAGE] Displaying: {self._filename} - {data['description']}")

	def get_size(self) -> int:
		"""Return size of image"""
		return self.IMAGE_DATABASE.get(self._filename).get("size", 0)

	def get_filename(self) -> str:
		"""Return filename"""
		return self._filename


class ImageProxy(Image):
	def __init__(self, filename: str):
		self._filename: str = filename
		self._real_image: RealImage | None = None
		self._load_count: int = 0

	def display(self) -> None:
		"""Display the image, loading it first if needed."""
		if self._real_image is None:
			print(f"[PROXY] First access to {self._filename} - loading real image...")
			self._real_image = RealImage(self._filename)
			self._load_count += 1  # Увеличиваем счётчик
		else:
			print(f"[PROXY] Using already loaded image: {self._filename}")

		self._real_image.display()

	def get_size(self) -> int:
		"""Get the image size in bytes, loading it first if needed."""
		if self._real_image is None:
			print(f"[PROXY] First access to {self._filename} - loading real image...")
			self._real_image = RealImage(self._filename)
			self._load_count += 1

		return self._real_image.get_size()

	def get_filename(self) -> str:
		"""Get the filename without loading the image."""
		return self._filename

	def is_loaded(self) -> bool:
		"""Check if the real image has been loaded."""
		return self._real_image is not None

	def get_load_count(self) -> int:
		"""Get the number of times the image was loaded."""
		return self._load_count


if __name__ == "__main__":
	print("=== Creating Image Proxies (should be instant) ===")

	# Создаём прокси для трёх изображений (должно быть быстро)
	image1 = ImageProxy("photo1.jpg")
	image2 = ImageProxy("photo2.jpg")
	image3 = ImageProxy("avatar.png")

	print(f"Created proxy for: {image1.get_filename()}")
	print(f"Created proxy for: {image2.get_filename()}")
	print(f"Created proxy for: {image3.get_filename()}")

	# Проверяем, загружены ли изображения
	print(f"\nIs image1 loaded? {image1.is_loaded()}")  # False
	print(f"Is image2 loaded? {image2.is_loaded()}")  # False

	print("\n=== Displaying image1 (will trigger loading) ===")
	image1.display()  # Здесь произойдёт загрузка (медленно)

	print(f"\nIs image1 loaded now? {image1.is_loaded()}")  # True

	print("\n=== Displaying image1 again (should be fast) ===")
	image1.display()  # Уже загружено (быстро)

	print("\n=== Getting size of image2 (will trigger loading) ===")
	size = image2.get_size()
	print(f"Image2 size: {size} bytes")

	print("\n=== Getting filename of image3 (NO loading) ===")
	filename = image3.get_filename()
	print(f"Image3 filename: {filename}")
	print(f"Is image3 loaded? {image3.is_loaded()}")  # False - не загружали!

	print("\n=== Statistics ===")
	print(f"Image1 load count: {image1.get_load_count()}")
	print(f"Image2 load count: {image2.get_load_count()}")
	print(f"Image3 load count: {image3.get_load_count()}")

	print("\n=== Comparison: Creating RealImage directly ===")
	print("Creating RealImage (will load immediately)...")
	real_image = RealImage("banner.jpg")  # Загрузка происходит сразу
	print("RealImage created and loaded!")
