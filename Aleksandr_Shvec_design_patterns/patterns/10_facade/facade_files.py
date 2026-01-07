"""
## 📋 Задача

Создай систему обработки файлов с данными о пользователях:
1. **FileReader** — читает файл (JSON/CSV/XML)
2. **DataParser** — парсит содержимое в нужный формат
3. **DataValidator** — проверяет корректность данных (email, возраст, обязательные поля)
4. **DataStorage** — сохраняет валидные данные в базу/файл
5. **Logger** — логирует все операции

**Фасад** должен объединить все это в один простой метод: `process_file(filepath)`

## 🎯 Требования
1. Классы подсистемы должны работать **независимо** друг от друга
2. Фасад должен **упростить** весь процесс
3. Добавь **обработку ошибок** на каждом этапе
4. Используй **типизацию**
5. Код должен быть **чистым и читаемым**

## 💡 Подсказки

**Структура данных** (для примера):
```json
[
  {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
  },
  {
    "name": "Bob",
    "email": "bob@example.com",
    "age": 30
  }
]
```

**Валидация должна проверять:**
- Email содержит `@` и `.`
- Возраст от 0 до 120
- Имя не пустое

**Logger должен выводить:**
[INFO] Reading file: data.json
[INFO] Parsing data...
[INFO] Validating 2 records...
[WARNING] Record skipped: invalid email
[INFO] Saving 1 valid records...
[SUCCESS] Processing completed!

## 📝 Пример использования (как должно работать)

# Клиентский код - просто и понятно!
processor = FileProcessorFacade()
processor.process_file("users.json")

# Вся сложная логика скрыта внутри фасада
"""
import datetime
import json
from pathlib import Path


class Logger:
	"""Logging operations"""

	def _log(self, level: str, message: str):
		timestamp = datetime.datetime.now().strftime("%H:%M:%S")
		print(f"[{timestamp}] [{level}] {message}")

	def info(self, message: str) -> None:
		"""Information message"""
		self._log("INFO", message)

	def warning(self, message: str) -> None:
		"""Warning message"""
		self._log("WARNING", message)

	def error(self, message: str) -> None:
		"""Error message"""
		self._log("ERROR", message)

	def success(self, message: str) -> None:
		"""Success message"""
		self._log("SUCCESS", message)


class FileReader:
	"""FileReader"""

	def __init__(self, logger: Logger):
		self._logger = logger

	def read_file(self, filename: str) -> str:
		file_path = Path(filename)

		if not file_path.exists():
			self._logger.error(f"File does not exist: {filename}")
			raise FileNotFoundError(f"File not found: {filename}")

		with open(filename, "r", encoding="utf-8") as f:
			data = f.read()

		self._logger.info('File read successfully')
		return data

	def check_format_file(self, filename: str, allowed_formats: list[str] | None = None) -> None:
		if allowed_formats is None:
			allowed_formats = [".json", ".csv", ".xml"]

		file_extension = Path(filename).suffix.lower()
		normalized_formats = [f if f.startswith(".") else f".{f}" for f in allowed_formats]
		normalized_formats = [f.lower() for f in normalized_formats]

		if file_extension not in normalized_formats:
			self._logger.error(f"Unsupported format: {file_extension}")
			raise ValueError(
				f"Format {file_extension} not supported. Allowed: {normalized_formats}")

		self._logger.info(f"File format is valid: {file_extension}")


class DataParser:
	"""DataParser"""

	def __init__(self, logger: Logger):
		self._logger = logger

	def parse(self, data: str) -> list[dict]:
		parsed_data = json.loads(data)
		self._logger.info(f"Parsed {len(parsed_data)} records")
		return parsed_data


class DataValidator:
	"""DataValidator"""

	def __init__(self, logger: Logger):
		self._logger = logger

	def validate_data(self, data: list[dict]) -> list[dict]:
		count = 0
		cleaned_data = []
		for item in data:
			try:
				self._check_name(item.get("name"))
				self._check_email(item.get("email"))
				self._check_age(item.get("age"))
				count += 1
				cleaned_data.append(item)
			except ValueError as e:
				self._logger.error(f"Handle error: {e}")
			except Exception as e:
				self._logger.error(f"Error {e}")

		self._logger.info(f"Handle {count} records")

		return cleaned_data

	def _check_email(self, email):
		if not email or ("@" not in email) or ("." not in email):
			raise ValueError(f"Email not valid. email: {email}")

	def _check_age(self, age):
		if age is None or age < 0 or age > 120:
			raise ValueError(f"Age not valid. age: {age}")

	def _check_name(self, name):
		if not name:
			raise ValueError(f"Name not valid. name: {name}")


class DataStorage:
	"""DataStorage"""

	def __init__(self, logger: Logger):
		self._logger = logger

	def save(self, data: list[dict], filename: str = "cleaned_data.json") -> None:
		with open(filename, "w", encoding="utf-8") as f:
			json.dump(data, f, indent=4, ensure_ascii=True)

		self._logger.info("Data write successfully!")


class FileProcessorFacade:
	def __init__(self):
		self._logger = Logger()
		self._file_reader = FileReader(self._logger)
		self._parser = DataParser(self._logger)
		self._validator = DataValidator(self._logger)
		self._file_storage = DataStorage(self._logger)

	def process_file(self, filename: str):
		self._logger.info(f"Starting file processing: {filename}")
		try:
			data = self._process_get_data_from_file(filename)

			parsed_data = self._process_parse_data(data)

			clean_data = self._process_valid_data(parsed_data)

			self._process_save_data(clean_data)

			self._logger.success("File processing completed successfully!")

		except (ValueError, TypeError, FileNotFoundError) as e:
			self._logger.error(f"Processing failed: {e}")
			raise
		except Exception as e:
			self._logger.error(f"Unexpected error: {e}")
			raise

	def _process_get_data_from_file(self, filename: str) -> str:
		self._logger.info("Start process read_file")
		self._file_reader.check_format_file(filename)
		data = self._file_reader.read_file(filename)
		self._logger.info("Finish process read_file. Successfully")
		return data

	def _process_parse_data(self, data: str) -> list[dict]:
		self._logger.info("Start process parse_data")
		data = self._parser.parse(data)
		self._logger.info("Finish process parse_data. Successfully")
		return data

	def _process_valid_data(self, data: list[dict]) -> list[dict]:
		self._logger.info("Start process valid_data")
		clean_data = self._validator.validate_data(data)
		skipped = len(data) - len(clean_data)
		if skipped > 0:
			self._logger.info(f"Skipped {skipped} records")
		self._logger.info("Finish process valid_data. Successfully")
		return clean_data

	def _process_save_data(self, data: list[dict]) -> None:
		self._logger.info("Start process save_data")
		self._file_storage.save(data)
		self._logger.info("Finish process save_data. Successfully")


if __name__ == '__main__':
	# Клиентский код - просто и понятно!
	processor = FileProcessorFacade()
	processor.process_file("users.json")

