import warnings
from typing import Optional


class DatabaseConnection:
	_instance: Optional['DatabaseConnection'] = None
	_initialized: bool = False

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls)
		else:
			if args or kwargs:
				existing = cls._instance
				warnings.warn(
					f"DatabaseConnection уже инициализирован с параметрами "
					f"{existing.host}:{existing.port}:{existing.database}. "
					f"Новые параметры будут проигнорированы!",
					UserWarning
				)

		return cls._instance

	def __init__(self, host: str = None, port: int = None, database: str = None):
		if not DatabaseConnection._initialized:
			if host is None or port is None or database is None:
				raise ValueError("При первом создании нужны все параметры: host, port, database")

			self.host = host
			self.port = port
			self.database = database
			self._connected = False
			DatabaseConnection._initialized = True

	@classmethod
	def get_instance(cls):
		"""Явный способ получить существующий экземпляр"""
		if cls._instance is None:
			raise RuntimeError("Сначала создайте экземпляр с параметрами!")
		return cls._instance

	def connect(self):
		"""Подключение к БД"""
		if not self._connected:
			print(f"✅ Подключено к {self.host}:{self.port}/{self.database}")
			self._connected = True
		else:
			print(f"ℹ️ Уже подключено к {self.host}:{self.port}/{self.database}")

	def query(self, sql: str):
		if not self._connected:
			print("⚠️ Нет подключения! Подключаемся...")
			self.connect()
		print(f"🔍 Выполняем: {sql}")

	def __str__(self):
		return f"DatabaseConnection({self.host}:{self.port}/{self.database})"


if __name__ == '__main__':
	host1, port1, database1 = "localhost", 5432, "test"
	db1 = DatabaseConnection(host1, port1, database1)
	db1.connect()
	sql = "SELECT 1;"
	db1.query(sql)
	host2, port2, database2 = "mysql", 6666, "prod"
	db2 = DatabaseConnection(host2, port2, database2)
	db2.connect()
	sql = "SELECT * from users;"
	db2.query(sql)
	print(db1 is db2)
	print(db1)
	print(db2)
	db = DatabaseConnection.get_instance()
	print(db)
	print(db1 is db2 is db)
