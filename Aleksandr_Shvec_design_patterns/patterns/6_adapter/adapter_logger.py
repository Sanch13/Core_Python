"""
Задача: Унификация работы с логгерами
Контекст:
Ты работаешь над приложением, которое должно логировать события.
У тебя есть три разных библиотеки логирования с несовместимыми интерфейсами:

StandardLogger (твой старый код) — метод log(message, level)
FileLogger (сторонняя библиотека) — метод write_to_file(text)
CloudLogger (новый сервис) — метод send_log(data: dict)

Тебе нужно создать единый интерфейс для работы со всеми логгерами,
чтобы остальной код приложения не знал о различиях между ними.

Требования:
1. Создай абстрактный интерфейс Logger
С единственным методом log
2. Реализуй три класса логгеров
3. Создай адаптеры:
FileLoggerAdapter — адаптирует FileLogger к интерфейсу Logger
Должен формировать текст вида: "[INFO] message" перед записью
CloudLoggerAdapter — адаптирует CloudLogger к интерфейсу Logger
Должен преобразовывать параметры в словарь: {"level": "INFO", "message": "text", "timestamp": "..."}
"""
import datetime
from abc import ABC, abstractmethod


class Logger(ABC):
	VALID_LEVELS = ("INFO", "WARNING", "ERROR")

	def log(self, message: str, level: str = "INFO") -> None:
		"""
		message: текст сообщения
		level: уровень логирования ("INFO", "WARNING", "ERROR")
		"""
		if level not in self.VALID_LEVELS:
			raise ValueError(
				f"Invalid level '{level}'. Must be one of {self.VALID_LEVELS}"
			)
		self._log_impl(message, level)

	@abstractmethod
	def _log_impl(self, message: str, level: str) -> None:
		pass


class StandardLogger:
	def log(self, message: str, level: str) -> None:
		"""
		message: текст сообщения
		level: уровень логирования ("INFO", "WARNING", "ERROR")
		"""
		print(f"[{level}] {message}")


class StandardLoggerAdapter(Logger):
	def __init__(self, logger: StandardLogger) -> None:
		self._logger = logger

	def _log_impl(self, message: str, level: str) -> None:
		self._logger.log(message, level)


class FileLogger:
	def __init__(self, filename: str):
		self._filename = filename

	def write_to_file(self, text: str) -> None:
		print(f"Writing to {self._filename}: {text}")


class FileLoggerAdapter(Logger):
	def __init__(self, file_logger: FileLogger):
		self._file_logger = file_logger

	def _log_impl(self, message: str, level: str) -> None:
		text = f"[{level}] {message}"
		self._file_logger.write_to_file(text=text)


class CloudLogger:
	def __init__(self, api_key: str):
		self.api_key = api_key

	def send_log(self, data: dict) -> None:
		"""Отправляет словарь в облако"""
		print(f"Sending to cloud (API: {self.api_key}): {data}")


class CloudLoggerAdapter(Logger):
	def __init__(self, cloud_logger: CloudLogger):
		self._cloud_logger = cloud_logger

	def _log_impl(self, message: str, level: str) -> None:
		data = {
			"level": level,
			"message": message,
			"timestamp": datetime.datetime.now().isoformat()
		}
		self._cloud_logger.send_log(data=data)


def process_user_action(logger: Logger, action: str):
	"""Обрабатывает действие пользователя и логирует его"""
	logger.log(f"User action: {action}", level="INFO")


if __name__ == "__main__":
	logger_standard = StandardLogger()
	logger_standard_adapter = StandardLoggerAdapter(logger=logger_standard)
	logger_file = FileLogger(filename="app.log")
	logger_file_adapter = FileLoggerAdapter(file_logger=logger_file)
	logger_cloud = CloudLogger(api_key="secret123")
	logger_cloud_adapter = CloudLoggerAdapter(cloud_logger=logger_cloud)

	process_user_action(logger_standard_adapter, action="login")
	process_user_action(logger_file_adapter, action="register")
	process_user_action(logger_cloud_adapter, action="logout")
