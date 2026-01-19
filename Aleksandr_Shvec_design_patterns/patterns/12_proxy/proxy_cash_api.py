"""
Техническое задание: Кэширующий Proxy для API запросов
Описание задачи
Тебе нужно реализовать систему для работы с API, которая будет кэшировать результаты запросов, чтобы избежать повторных обращений к серверу для одинаковых данных.

Структура классов
1. WeatherAPI (абстрактный класс)
Назначение: Общий интерфейс для работы с API погоды.
Методы:

get_weather(city: str) -> dict — получить данные о погоде для города


2. RealWeatherAPI (реальный объект)
Назначение: Класс, который выполняет реальные HTTP-запросы к API (в нашем случае имитирует).
Методы:

get_weather(city: str) -> dict — выполняет "тяжёлый" запрос к API

Особенности:

Имитирует задержку сети (например, time.sleep(2))
Возвращает данные о погоде из заранее подготовленного словаря


3. WeatherAPIProxy (заместитель с кэшированием)
Назначение: Proxy, который кэширует результаты запросов.
Атрибуты:

_real_api — ссылка на реальный API объект
_cache — словарь для хранения результатов (ключ: город, значение: данные)
_cache_ttl — время жизни кэша в секундах (опционально)

Методы:

get_weather(city: str) -> dict — проверяет кэш, если данных нет — делегирует запрос реальному API
clear_cache() — очищает кэш
get_cache_stats() -> dict — возвращает статистику (количество запросов в кэш, количество обращений к API)


Требования к реализации

Используй абстрактный базовый класс (ABC и abstractmethod)
Добавь английские docstrings для всех классов и методов
Proxy должен логировать обращения (cache hit / cache miss)
Реализуй подсчёт статистики запросов
Код должен быть чистым и читаемым

"""
import datetime
import time
from abc import ABC, abstractmethod


class Logger:
	"""Logging operations"""

	def _log(self, level: str, message: str):
		timestamp = datetime.datetime.now().strftime("%H:%M:%S")
		print(f"[{timestamp}] [{level}] {message}")

	def info(self, message: str) -> None:
		"""Information message"""
		self._log("INFO", message)


class WeatherAPI(ABC):
	"""A general interface for working with weather APIs."""

	@abstractmethod
	def get_weather(self, city: str) -> dict:
		"""Get weather data for the city."""
		pass


class RealWeatherAPI(WeatherAPI):
	"""A class that performs actual HTTP requests to the API."""

	WEATHER_DATA = {
		"London": {
			"temperature": 15,
			"condition": "Cloudy",
			"humidity": 65,
			"wind_speed": 20
		},
		"Paris": {
			"temperature": 18,
			"condition": "Sunny",
			"humidity": 55,
			"wind_speed": 10
		},
		"Tokyo": {
			"temperature": 22,
			"condition": "Rainy",
			"humidity": 80,
			"wind_speed": 15
		},
		"New York": {
			"temperature": 12,
			"condition": "Windy",
			"humidity": 60,
			"wind_speed": 25
		},
		"Moscow": {
			"temperature": -5,
			"condition": "Snowy",
			"humidity": 75,
			"wind_speed": 30
		}
	}

	def get_weather(self, city: str) -> dict:
		"""Get weather data for the city."""
		print(f"Fetching weather data for {city}... (this takes time)")
		time.sleep(2)
		if city not in self.WEATHER_DATA:
			raise ValueError(f"This city: {city} does not available")
		return self.WEATHER_DATA[city]



class WeatherAPIProxy(WeatherAPI):
	"""A proxy that caches the results of requests."""

	def __init__(
			self,
			real_api: RealWeatherAPI | None = None,
	):
		self._real_api: RealWeatherAPI = real_api or RealWeatherAPI()
		self._cache: dict[str, dict] = {}
		self._stats: dict = {
			"cache_hits": 0,
			"cache_misses": 0,
			"total_requests": 0
		}
		self._logger = Logger()

	def get_weather(self, city: str) -> dict:
		"""It checks the cache, and if the data is not found, it delegates the request to the actual API."""
		self._stats["total_requests"] += 1

		if city in self._cache:
			self._logger.info(f"[CACHE HIT] Returning cached data for: {city}")
			self._stats["cache_hits"] += 1
			return self._cache[city]

		self._logger.info("Cache miss")
		self._stats["cache_misses"] += 1
		data = self._real_api.get_weather(city)
		self._cache[city] = data
		return data

	def clear_cache(self) -> None:
		"""Clears the cache"""
		self._cache.clear()

	def get_cache_stats(self) -> dict:
		"""Returns statistics (number of requests to the cache, number of API calls)"""
		return self._stats


if __name__ == "__main__":
	# Создаём Proxy
	weather_service = WeatherAPIProxy()

	# Первый запрос для London (должен пойти к API - медленно)
	print("Request 1 - London:")
	print(weather_service.get_weather("London"))

	# Второй запрос для London (должен взять из кэша - быстро)
	print("\nRequest 2 - London (cached):")
	print(weather_service.get_weather("London"))

	# Запрос для Paris (должен пойти к API)
	print("\nRequest 3 - Paris:")
	print(weather_service.get_weather("Paris"))

	# Ещё раз London (из кэша)
	print("\nRequest 4 - London (cached):")
	print(weather_service.get_weather("London"))

	# Статистика
	print("\nCache statistics:")
	print(weather_service.get_cache_stats())

	# Очистка кэша
	weather_service.clear_cache()
	print("\nCache cleared!")

	# После очистки - снова медленный запрос
	print("\nRequest 5 - London (after cache clear):")
	print(weather_service.get_weather("London"))

	# Итоговая статистика
	print("\nFinal statistics:")
	print(weather_service.get_cache_stats())


"""
## ✅ Вопрос 1: Почему Proxy и RealWeatherAPI должны реализовывать один интерфейс?
**Твой ответ:** ✅ **Правильно!** 
Да, они должны иметь одинаковый интерфейс, чтобы Proxy мог **полностью заменить** реальный объект. Клиентский код не должен знать, работает он с Proxy или с реальным объектом.
**Дополнение:** Это называется **принцип подстановки Лисков (LSP)** — объекты должны быть взаимозаменяемыми без изменения корректности программы.
====================================================================================================
## ⚠️ Вопрос 2: В чём разница между Proxy и Decorator?
**Твой ответ:** ❌ **Неточно**
> "декоратор обарачивает множество других объектов, прокси управляет одним"
**Это не совсем так.** И Proxy, и Decorator могут работать с одним объектом.
### Ключевое различие:
| Паттерн | Цель | Как работает |
|---------|------|--------------|
| **Proxy** | **Контролирует доступ** к объекту | Имеет ту же функциональность, что и оригинал, но добавляет контроль (доступ, кэширование, ленивая загрузка) |
| **Decorator** | **Расширяет функциональность** объекта | Добавляет **новое поведение**, не изменяя интерфейс |
**Пример:**
- **Proxy:** Секретарь директора — не добавляет новых функций, просто контролирует доступ
- **Decorator:** Кофе с молоком и сахаром — добавляет новые свойства к базовому кофе
====================================================================================================
## ✅ Вопрос 3: Можно ли кэширование добавить в RealWeatherAPI?
**Твой ответ:** ✅ **Правильно!**
Да, технически можно, но это нарушит **Single Responsibility Principle (SRP)**. 
`RealWeatherAPI` должен отвечать только за получение данных, а кэширование — это отдельная ответственность.
**Бонус:** Proxy позволяет добавлять такую логику **без изменения** исходного класса (**Open/Closed Principle**).
====================================================================================================
## ❌ Вопрос 4: Что произойдёт с `real_api: RealWeatherAPI = RealWeatherAPI()`?
**Твой ответ:** ❌ **Неправильно**
> "это будут разные объекты"
**Нет! Это главная проблема.**
### Что на самом деле происходит:

# ❌ ПЛОХО
def __init__(self, real_api: RealWeatherAPI = RealWeatherAPI()):
    self._real_api = real_api

**Объект `RealWeatherAPI()` создаётся ОДИН РАЗ** при определении функции, а не при каждом вызове!

```python
proxy1 = WeatherAPIProxy()
proxy2 = WeatherAPIProxy()

# proxy1._real_api и proxy2._real_api указывают на ОДИН И ТОТ ЖЕ объект!
print(proxy1._real_api is proxy2._real_api)  # True ❌
```

**Демонстрация проблемы:**

```python
class BadExample:
    def __init__(self, data: list = []):  # ❌ Плохо!
        self.data = data

obj1 = BadExample()
obj2 = BadExample()

obj1.data.append(1)
print(obj2.data)  # [1] — изменение в obj1 повлияло на obj2!
```

**Правильно:**

```python
def __init__(self, real_api: Optional[RealWeatherAPI] = None):
    self._real_api = real_api or RealWeatherAPI()  # ✅ Создаётся каждый раз
```
====================================================================================================
## ⚠️ Вопрос 5: Как ограничить размер кэша?
**Твой ответ:** ⚠️ **Частично правильно**
> "проверял бы длину переменной кеша"
**Да, но что дальше?** Просто проверка `len(self._cache)` не решает проблему — нужно **удалить старые данные**.
### Варианты реализации:

#### Вариант 1: FIFO (First In, First Out)
```python
def get_weather(self, city: str) -> dict:
    if city not in self._cache:
        if len(self._cache) >= 100:
            # Удаляем самый старый элемент
            oldest_city = next(iter(self._cache))
            del self._cache[oldest_city]
        
        data = self._real_api.get_weather(city)
        self._cache[city] = data
    
    return self._cache[city]
```

#### Вариант 2: LRU (Least Recently Used) — лучший вариант
```python
from collections import OrderedDict

class WeatherAPIProxy(WeatherAPI):
    def __init__(self, max_cache_size: int = 100):
        self._cache = OrderedDict()
        self._max_cache_size = max_cache_size
    
    def get_weather(self, city: str) -> dict:
        if city in self._cache:
            # Перемещаем в конец (как недавно использованный)
            self._cache.move_to_end(city)
            return self._cache[city]
        
        if len(self._cache) >= self._max_cache_size:
            # Удаляем самый давно использованный (первый)
            self._cache.popitem(last=False)
        
        data = self._real_api.get_weather(city)
        self._cache[city] = data
        return data
```

#### Вариант 3: Готовое решение из Python
```python
from functools import lru_cache

# Но это для функций, не для классов в чистом виде

"""