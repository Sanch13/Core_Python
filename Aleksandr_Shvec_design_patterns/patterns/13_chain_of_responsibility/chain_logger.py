""""""
from __future__ import annotations

"""
📋 Задание: Система логирования с уровнями
Описание задачи
Тебе нужно реализовать систему логирования, где каждый логгер обрабатывает сообщения определённого 
уровня важности. Если логгер не может обработать сообщение (уровень выше его компетенции), 
он передаёт его следующему в цепочке.
Требования
1. Создай enum для уровней логирования:
DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4
CRITICAL = 5

2. Создай класс LogMessage:
Атрибуты: level (уровень), message (текст сообщения)

3. Создай абстрактный класс Logger:
Метод set_next() — устанавливает следующий логгер
Абстрактный метод log() — обрабатывает сообщение
Атрибут _log_level — уровень, который обрабатывает этот логгер

4. Создай конкретные логгеры:
ConsoleLogger — выводит DEBUG и INFO в консоль
FileLogger — записывает WARNING в файл (имитация)
EmailLogger — отправляет ERROR и CRITICAL по email (имитация)

5. Логика обработки:
Каждый логгер проверяет: если уровень сообщения <= его уровня, он обрабатывает
Затем всегда передаёт сообщение следующему логгеру (чтобы один запрос мог обработаться несколькими логгерами)
"""
"""
Что нужно сделать

Напиши код по требованиям выше
Используй английские названия классов и методов
Добавь docstrings на английском для всех классов и методов
Протестируй на предоставленных данных
Покажи мне код — я проверю и дам фидбек
Отвечу на вопросы для проверки понимания

Подсказка: В этой реализации каждый логгер должен передавать сообщение дальше всегда, а не только 
когда не может обработать (это важное отличие от примера с техподдержкой).
"""
from enum import IntEnum
from abc import ABC, abstractmethod


class LogLevel(IntEnum):
	"""Enumeration of log levels."""
	DEBUG = 1
	INFO = 2
	WARNING = 3
	ERROR = 4
	CRITICAL = 5


class LogMessage:
	"""Class for request of message"""

	def __init__(self, level: int, message: str):
		self.level = level
		self.message = message


class Logger(ABC):
	"""Abstract base class for loggers."""

	def __init__(self):
		self._next_logger: Logger | None = None

	@abstractmethod
	def log(self, message: LogMessage) -> None: ...
	"""Log message if its level is appropriate for this logger."""

	def set_next(self, logger: Logger) -> Logger:
		"""Set next logger in chain"""
		self._next_logger = logger
		return logger


class ConsoleLogger(Logger):
	def __init__(self):
		super().__init__()
		self._handle_levels = {LogLevel.DEBUG, LogLevel.INFO}

	def log(self, message: LogMessage) -> None:
		if message.level in self._handle_levels:
			print(f"[CONSOLE] {message.level.name}: {message.message}")

		if self._next_logger:
			self._next_logger.log(message)


class FileLogger(Logger):
	def __init__(self):
		super().__init__()
		self._handle_levels = {LogLevel.WARNING}

	def log(self, message: LogMessage) -> None:
		if message.level in self._handle_levels:
			print(f"[FILE] {message.level.name}: {message.message}")

		if self._next_logger:
			self._next_logger.log(message)


class EmailLogger(Logger):
	def __init__(self):
		super().__init__()
		self._handle_levels = {LogLevel.ERROR, LogLevel.CRITICAL}

	def log(self, message: LogMessage) -> None:
		if message.level in self._handle_levels:
			print(f"[EMAIL] {message.level.name}: {message.message}")

		if self._next_logger:
			self._next_logger.log(message)


if __name__ == '__main__':
	# Создай цепочку: Console → File → Email
	console_logger = ConsoleLogger()
	file_logger = FileLogger()
	email_logger = EmailLogger()

	console_logger.set_next(file_logger).set_next(email_logger)

	# Протестируй на этих сообщениях:
	test_messages = [
		LogMessage(LogLevel.DEBUG, "Application started"),
		LogMessage(LogLevel.INFO, "User logged in: user123"),
		LogMessage(LogLevel.WARNING, "Disk space low: 15% remaining"),
		LogMessage(LogLevel.ERROR, "Database connection failed"),
		LogMessage(LogLevel.CRITICAL, "System crash imminent!"),
	]

	print("=== Обработка ===\n")
	for msg in test_messages:
		console_logger.log(msg)
		print()
