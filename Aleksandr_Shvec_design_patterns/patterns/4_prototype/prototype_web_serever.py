import copy
from abc import ABC, abstractmethod


class Server(ABC):
	def __init__(self, name: str, cpu: int, ram: int):
		self.name = name
		self.cpu = cpu
		self.ram = ram
		self.installed_software = []

	@abstractmethod
	def clone(self):
		pass

	def install_software(self, *software: str):
		"""Устанавливает ПО на сервер"""
		self.installed_software.extend(software)

	def __str__(self):
		software = ", ".join(self.installed_software) if self.installed_software else "None"
		return (f"{self.name}: CPU={self.cpu} | RAM={self.ram}GB | "
				f"Software=[{software}]")


class WebServer(Server):
	def __init__(self, name="WebServer"):
		super().__init__(name=name, cpu=2, ram=4)

	def clone(self):
		return copy.deepcopy(self)


class DatabaseServer(Server):
	def __init__(self, name="DatabaseServer"):
		super().__init__(name=name, cpu=4, ram=16)

	def clone(self):
		return copy.deepcopy(self)


class ServerFactory:
	def __init__(self):
		self._prototypes = {}

	def register(self, key: str, prototype: Server):
		self._prototypes[key] = prototype.clone()

	def create(self, key: str, name: str = None) -> Server:
		if key not in self._prototypes:
			raise ValueError(f"Прототип '{key}' не зарегистрирован")

		clone = self._prototypes[key].clone()
		if name:
			clone.name = name
		return clone


if __name__ == '__main__':
	# web = WebServer()
	# db = DatabaseServer()
	# print(web)
	# print(db)
	# web_1 = web.clone()
	# web_1.name = "WebServer-prod-1"
	# print(web_1)
	# db_1 = db.clone()
	# db_1.name = "DatabaseServer-prod-1"
	# print(db_1)
	# web.install_software("nginx", "certbot")
	# db.install_software("postgresql", "redis")
	# print(web)
	# print(db)

	factory = ServerFactory()
	web_proto = WebServer()
	factory.register('web', web_proto)
	web_proto.install_software('malware')
	factory.register('database', DatabaseServer())

	web1 = factory.create('web', 'web-prod-1')
	web2 = factory.create('web', 'web-prod-2')
	print(web1, web2)
	web1.install_software("nginx", "certbot")
	web2.install_software("fail2ban", "curl")
	print(web1, web2)
	db1 = factory.create('database', 'db-master')
	db2 = factory.create('database', 'db-slave')
	print(db1, db2)
	db1.install_software("postgresql", "redis")
	db2.install_software("mysql", "ssh")
	print(db1, db2)



	print("=== Запуск тестов ===\n")

	factory = ServerFactory()
	factory.register("web", WebServer())
	factory.register("db", DatabaseServer())

	# Тест 1: Имя по умолчанию
	print("Тест 1: Имя по умолчанию")
	server1 = factory.create("web")
	assert server1.name == "WebServer", "❌ Должно быть имя прототипа!"
	print(f"✅ {server1.name}")

	# Тест 2: Кастомное имя
	print("\nТест 2: Кастомное имя")
	server2 = factory.create("web", "web-prod-01")
	assert server2.name == "web-prod-01", "❌ Должно быть кастомное имя!"
	print(f"✅ {server2.name}")

	# Тест 3: Независимость клонов
	print("\nТест 3: Независимость клонов")
	server1.install_software("nginx")
	server2.install_software("apache")
	assert "nginx" not in server2.installed_software, "❌ Клоны должны быть независимы!"
	assert "apache" not in server1.installed_software, "❌ Клоны должны быть независимы!"
	print(f"✅ server1: {server1.installed_software}")
	print(f"✅ server2: {server2.installed_software}")

	# Тест 4: Разные типы серверов
	print("\nТест 4: Разные типы серверов")
	db1 = factory.create("db", "db-master")
	assert db1.cpu == 4 and db1.ram == 16, "❌ Неверные характеристики DB сервера!"
	assert server1.cpu == 2 and server1.ram == 4, "❌ Неверные характеристики Web сервера!"
	print(f"✅ Web: {server1.cpu}CPU, {server1.ram}GB")
	print(f"✅ DB: {db1.cpu}CPU, {db1.ram}GB")

	# Тест 5: Ошибка при несуществующем прототипе
	print("\nТест 5: Обработка ошибок")
	try:
		factory.create("unknown")
		assert False, "❌ Должна быть ошибка!"
	except ValueError as e:
		print(f"✅ Поймали ошибку: {e}")

	print("\n" + "=" * 50)
	print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
	print("=" * 50)

	# Тест 6: Защита прототипа от изменений
	print("\nТест 6: Защита прототипа")
	web_original = WebServer()
	factory2 = ServerFactory()
	factory2.register("web", web_original)

	# Меняем оригинал ПОСЛЕ регистрации
	web_original.install_software("virus")
	web_original.name = "HACKED"

	# Создаём сервер из фабрики
	clean_server = factory2.create("web")
	assert "virus" not in clean_server.installed_software, "❌ Прототип не защищён!"
	assert clean_server.name == "WebServer", "❌ Прототип не защищён!"
	print(f"✅ Прототип защищён: {clean_server}")