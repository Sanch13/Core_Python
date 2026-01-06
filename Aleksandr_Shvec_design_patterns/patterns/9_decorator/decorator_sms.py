"""
Задача: Создай систему уведомлений, где базовый класс отправляет SMS. Добавь декораторы для:

Отправки email
Отправки в Telegram
Логирования уведомлений
"""

from abc import ABC, abstractmethod


# 1. Базовый интерфейс
class Message(ABC):
	@abstractmethod
	def send(self):
		pass


# 2. Конкретный компонент (базовый класс отправляет SMS)
class SMS(Message):
	def send(self) -> str:
		return f"Send SMS"


# 3. Базовый декоратор
class MessageDecorator(Message):
	def __init__(self, message: Message):
		self._message = message

	def send(self) -> str:
		return self._message.send()


# 4. Конкретные декораторы
class Email(MessageDecorator):
	def send(self) -> str:
		return f"{self._message.send()} + Send Email"


class Telegram(MessageDecorator):
	def send(self) -> str:
		return f"{self._message.send()} + Send Telegram"


class Logger(MessageDecorator):
	def send(self):
		return f"[LOG] Начало отправки\n{self._message.send()}\n[LOG] Отправка завершена"


if __name__ == "__main__":
	sms = SMS()
	print(sms.send())

	email = Email(SMS())
	print(email.send())

	tg = Telegram(Email(SMS()))
	print(tg.send())

	log = Logger(Telegram(Email(SMS())))
	print(log.send())
