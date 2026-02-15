"""
"""
from __future__ import annotations

from collections import defaultdict

"""
# Задача 2: Middleware для HTTP-запросов 🌐
## Техническое задание
### Описание задачи
Тебе необходимо реализовать систему middleware (промежуточных обработчиков) для обработки 
HTTP-запросов. Каждый middleware выполняет свою специфическую проверку и решает, передавать ли 
запрос дальше по цепочке или прервать обработку.

## Требования к реализации
### 1. Структура данных запроса

Создай класс `Request` с следующими атрибутами:
- `path` (str) — путь запроса, например "/api/users"
- `method` (str) — HTTP метод: "GET", "POST", "PUT", "DELETE"
- `headers` (dict) — словарь заголовков, например `{"Authorization": "Bearer token123"}`
- `user_id` (Optional[int]) — ID пользователя (может быть None, если не аутентифицирован)
- `user_role` (Optional[str]) — роль пользователя: "admin", "user", "guest" (или None)
- `ip_address` (str) — IP адрес клиента

### 2. Базовый класс Middleware

Создай абстрактный базовый класс `Middleware` с методами:
- `set_next(middleware)` — устанавливает следующий middleware в цепочке
- `handle(request)` — обрабатывает запрос или передаёт следующему

### 3. Конкретные Middleware (создай 4-5 классов)
#### A) `AuthenticationMiddleware`
**Назначение:** Проверяет наличие токена аутентификации в заголовках.

**Логика:**
- Проверяет наличие заголовка "Authorization"
- Если заголовок есть и начинается с "Bearer " — устанавливает `user_id` и `user_role` (можешь симулировать это)
- Если заголовка нет — возвращает ошибку "401 Unauthorized: Missing authentication token"

#### B) `AuthorizationMiddleware`
**Назначение:** Проверяет права доступа пользователя к ресурсу.

**Логика:**
- Проверяет, что пути начинающиеся с "/admin" доступны только пользователям с ролью "admin"
- Если доступ запрещён — возвращает "403 Forbidden: Insufficient permissions"
- В остальных случаях передаёт дальше

#### C) `RateLimitMiddleware`
**Назначение:** Ограничивает количество запросов с одного IP.

**Логика:**
- Хранит словарь: IP → количество запросов
- Если с одного IP пришло больше 5 запросов — возвращает "429 Too Many Requests: Rate limit exceeded"
- Иначе увеличивает счётчик и передаёт дальше

#### D) `LoggingMiddleware`
**Назначение:** Логирует информацию о запросе.

**Логика:**
- Выводит в консоль: метод, путь, IP адрес, user_id
- Всегда передаёт запрос дальше (не прерывает цепочку)

#### E) `RequestHandlerMiddleware` (финальный обработчик)
**Назначение:** Успешная обработка запроса (конец цепочки).

**Логика:**
- Возвращает "200 OK: Request processed successfully for {path}"

---

## Тестовые данные

Создай список из 8-10 различных запросов для проверки всех сценариев:

1. ✅ Валидный запрос с токеном к обычному ресурсу
2. ❌ Запрос без токена аутентификации
3. ✅ Запрос админа к `/admin/users`
4. ❌ Запрос обычного пользователя к `/admin/settings`
5. ✅ Несколько запросов с одного IP (в пределах лимита)
6. ❌ Превышение rate limit (6-й запрос с одного IP)
7. ✅ Запрос гостя к публичному ресурсу `/public/info`
8. Любые другие комбинации для проверки

### Пример формата тестового запроса:

```python
test_requests = [
    Request(
        path="/api/users",
        method="GET",
        headers={"Authorization": "Bearer valid_token_123"},
        ip_address="192.168.1.100"
    ),
    Request(
        path="/admin/settings",
        method="POST",
        headers={},  # No auth header
        ip_address="192.168.1.101"
    ),
    # ... добавь остальные
]
```
## Ожидаемая структура классов (только имена, БЕЗ кода!)
```
Request
├── __init__(path, method, headers, ip_address, user_id=None, user_role=None)

Middleware (ABC)
├── set_next(middleware)
├── handle(request) [abstract]

AuthenticationMiddleware(Middleware)
├── handle(request)

AuthorizationMiddleware(Middleware)
├── handle(request)

RateLimitMiddleware(Middleware)
├── __init__()
├── handle(request)

LoggingMiddleware(Middleware)
├── handle(request)

RequestHandlerMiddleware(Middleware)
├── handle(request)
```

## Что нужно сделать
1. Создай все классы с английскими названиями
2. Напиши английские docstrings для всех классов и методов
3. Реализуй логику каждого middleware согласно описанию
4. Создай тестовые данные (8-10 запросов)
5. Построй цепочку middleware и прогони через неё все тестовые запросы
6. Выведи результат обработки каждого запроса

## Критерии оценки
- ✅ Правильное использование паттерна Chain of Responsibility
- ✅ Соблюдение принципов SOLID
- ✅ Читаемость и структура кода
- ✅ Наличие docstrings на английском
- ✅ Корректная обработка всех тестовых сценариев
- ✅ Логичная последовательность middleware в цепочке
"""
from collections import defaultdict
from abc import ABC, abstractmethod


class Request:
	def __init__(
			self,
			path: str,
			method: str,
			headers: dict,
			ip_address: str,
			user_id: int | None = None,
			user_role: str | None = None,
	):
		self.path = path
		self.method = method
		self.headers = headers
		self.ip_address = ip_address
		self.user_id = user_id if user_id is not None else "Anonymous"
		self.user_role = user_role

	def __repr__(self):
		return f"Request(method={self.method}, path={self.path}, ip={self.ip_address}, user_id={self.user_id}, role={self.user_role})"


class Middleware(ABC):
	"""Abstract base class for middleware handlers."""

	def __init__(self):
		self._next_middleware: Middleware | None = None

	def set_next(self, middleware: Middleware) -> Middleware:
		self._next_middleware = middleware
		return middleware

	@abstractmethod
	def handle(self, request: Request): ...


class AuthenticationMiddleware(Middleware):
	"""Validates authentication token in request headers."""

	def __init__(self):
		super().__init__()
		self._header_auth = "Authorization"

	def handle(self, request: Request):
		if self._header_auth not in request.headers:
			return "401 Unauthorized: Missing authentication token"

		if self._has_bearer(request):
			token = request.headers[self._header_auth]
			if "admin" in token:
				request.user_role = "admin"
				request.user_id = 1
			elif "guest" in token:
				request.user_role = "guest"
				request.user_id = 999
			else:
				request.user_role = "user"
				request.user_id = 100

		if self._next_middleware:
			return self._next_middleware.handle(request)

		return "No more handlers in chain"

	def _has_bearer(self, request: Request) -> bool:
		header_auth_value = request.headers.get(self._header_auth)
		return header_auth_value is not None and "Bearer " in header_auth_value


class AuthorizationMiddleware(Middleware):
	"""Check user rules to service"""

	def handle(self, request: Request):
		if request.path.startswith("/admin") and request.user_role != "admin":
			return "403 Forbidden: Insufficient permissions"

		if self._next_middleware:
			return self._next_middleware.handle(request)

		return "No more handlers in chain"


class RateLimitMiddleware(Middleware):
	"""Limit amount of request from one IP"""

	def __init__(self):
		super().__init__()
		self.ip: defaultdict[str, int] = defaultdict(int)

	def handle(self, request: Request):
		ip_address = request.ip_address
		if self.ip[ip_address] >= 5:
			return "429 Too Many Requests: Rate limit exceeded"

		self.ip[ip_address] += 1

		if self._next_middleware:
			return self._next_middleware.handle(request)

		return "No more handlers in chain"


class LoggingMiddleware(Middleware):
	"""Log request"""

	def handle(self, request: Request):
		print(f"{request.method} {request.path} {request.ip_address} {request.user_id}")

		if self._next_middleware:
			return self._next_middleware.handle(request)

		return "No more handlers in chain"

class RequestHandlerMiddleware(Middleware):
	"""Final handler that processes successful requests"""

	def handle(self, request: Request):
		return f"200 OK: Request processed successfully for {request.path}"


if __name__ == "__main__":
	test_requests = [
		# ✅ Test 1: Valid request with token to regular resource
		Request(
			path="/api/users",
			method="GET",
			headers={"Authorization": "Bearer valid_token_123"},
			ip_address="192.168.1.100"
		),

		# ❌ Test 2: Request without authentication token
		Request(
			path="/api/profile",
			method="GET",
			headers={},  # No Authorization header
			ip_address="192.168.1.101"
		),

		# ✅ Test 3: Admin request to /admin resource
		Request(
			path="/admin/users",
			method="POST",
			headers={"Authorization": "Bearer admin_token_456"},
			ip_address="192.168.1.102"
		),

		# ❌ Test 4: Regular user request to /admin resource (forbidden)
		Request(
			path="/admin/settings",
			method="DELETE",
			headers={"Authorization": "Bearer user_token_789"},
			ip_address="192.168.1.103"
		),

		# ✅ Test 5: Multiple requests from same IP (request #1 - within limit)
		Request(
			path="/api/posts",
			method="GET",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ✅ Test 6: Multiple requests from same IP (request #2 - within limit)
		Request(
			path="/api/comments",
			method="GET",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ✅ Test 7: Multiple requests from same IP (request #3 - within limit)
		Request(
			path="/api/likes",
			method="POST",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ✅ Test 8: Multiple requests from same IP (request #4 - within limit)
		Request(
			path="/api/shares",
			method="POST",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ✅ Test 9: Multiple requests from same IP (request #5 - last allowed)
		Request(
			path="/api/notifications",
			method="GET",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ❌ Test 10: Rate limit exceeded (request #6 from same IP)
		Request(
			path="/api/messages",
			method="GET",
			headers={"Authorization": "Bearer valid_token_111"},
			ip_address="192.168.1.200"
		),

		# ✅ Test 11: Guest request to public resource
		Request(
			path="/public/info",
			method="GET",
			headers={"Authorization": "Bearer guest_token_999"},
			ip_address="192.168.1.104"
		),

		# ✅ Test 12: Valid POST request with authentication
		Request(
			path="/api/articles",
			method="POST",
			headers={"Authorization": "Bearer valid_token_555"},
			ip_address="192.168.1.105"
		),

		# ❌ Test 13: Another request without token (different IP)
		Request(
			path="/api/data",
			method="GET",
			headers={"Content-Type": "application/json"},  # No Authorization
			ip_address="192.168.1.106"
		),

		# ✅ Test 14: Admin accessing admin panel
		Request(
			path="/admin/dashboard",
			method="GET",
			headers={"Authorization": "Bearer admin_super_token"},
			ip_address="192.168.1.107"
		),
	]

	auth = AuthenticationMiddleware()
	authz = AuthorizationMiddleware()
	rate_limit = RateLimitMiddleware()
	log = LoggingMiddleware()
	handler = RequestHandlerMiddleware()

	auth.set_next(authz).set_next(rate_limit).set_next(log).set_next(handler)

	print("=" * 60)
	print("TESTING MIDDLEWARE CHAIN")
	print("=" * 60)

	for i, request in enumerate(test_requests, 1):
		print(f"\n--- Test {i} ---")
		print(f"Request: {request.method} {request.path}")
		print(f"IP: {request.ip_address}")
		print(f"Has Auth: {'Yes' if 'Authorization' in request.headers else 'No'}")

		result = auth.handle(request)

		print(f"Result: {result}")
		print("-" * 60)