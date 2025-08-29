Привет! Отличный выбор — FastAPI, PostgreSQL и SQLAlchemy хорошо сочетаются и позволяют строить масштабируемые и поддерживаемые приложения.  

## 🔹 **Чистая архитектура и DDD**  
Чистая архитектура (Clean Architecture) и DDD (Domain-Driven Design) помогают разделить код на логические слои, чтобы он был гибким, тестируемым и легко расширяемым.  

---

### 📌 **Основные слои Чистой архитектуры**  
💡 **Главная идея**: разделить код так, чтобы бизнес-логика не зависела от инфраструктуры (БД, API, UI и т. д.).

1. **Доменный слой (Domain Layer)**
   - Чистая бизнес-логика приложения.
   - Определяет сущности (Entities) и объекты-значения (Value Objects).
   - Использует паттерны, такие как `Aggregate Root`, `Repository`, `Service`.

2. **Слой приложения (Application Layer)**
   - Содержит use cases (случаи использования).
   - Выполняет оркестрацию работы доменного слоя.

3. **Инфраструктурный слой (Infrastructure Layer)**
   - Работа с базой данных (ORM), кэшем, внешними API.
   - Хранилище данных (репозитории).
   - Обеспечивает внешние зависимости.

4. **Внешний слой (Presentation Layer)**
   - Интерфейсы для пользователей (API, Web UI).
   - Подключение к FastAPI.

---

### 📌 **Что будем делать?**
Приложение **"Библиотека книг"** будет поддерживать:
- CRUD-операции для книг (`Book`).
- Авторизацию пользователей (JWT).
- Валидацию входящих данных.

---

### 📌 **Шаг 1: Базовая структура проекта**  
Создадим минимальный каркас с папками:

```
library_app/
│── app/
│   ├── domain/          # Доменный слой
│   │   ├── models.py    # Описание сущностей
│   │   ├── repositories.py # Интерфейсы репозиториев
│   │   ├── services.py  # Бизнес-логика
│   ├── application/     # Слой приложения
│   │   ├── use_cases.py # Кейсы использования
│   ├── infrastructure/  # Инфраструктурный слой
│   │   ├── database.py  # Подключение к БД
│   │   ├── repositories/ # Реализация репозиториев
│   ├── presentation/    # Внешний слой
│   │   ├── api/         # Эндпоинты FastAPI
│   │   ├── schemas.py   # Pydantic-схемы
│   ├── config.py        # Настройки
│   ├── main.py          # Точка входа
│── alembic/             # Миграции
│── requirements.txt     # Зависимости
│── .env                 # Переменные окружения
```

---

### 📌 **Шаг 2: Установка зависимостей**
Установим нужные пакеты:

```sh
pip install fastapi uvicorn
pip install sqlalchemy psycopg2-binary alembic
pip install pydantic pydantic-settings
```

---

### 📌 **Шаг 3: Определяем доменную модель "Book"**  
Файл `app/domain/models.py`:

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    published_year: int
```

📌 Здесь:
- `dataclass` используется для хранения данных.
- `id` — необязательное поле, так как при создании книги оно ещё не назначено.

---

### 📌 **Шаг 4: Интерфейс репозитория (Domain Layer)**
Файл `app/domain/repositories.py`:

```python
from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Book

class BookRepository(ABC):
    """ Интерфейс для работы с книгами. """

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, book_id: int) -> Optional[Book]:
        pass

    @abstractmethod
    def add(self, book: Book) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        pass
```

📌 Этот интерфейс позволит нам легко менять способ хранения данных, не изменяя бизнес-логику.

---

### 📌 **Шаг 5: Реализация репозитория (Infrastructure Layer)**
Файл `app/infrastructure/repositories/book_repository.py`:

```python
from sqlalchemy.orm import Session
from typing import List, Optional
from app.domain.models import Book
from app.domain.repositories import BookRepository
from app.infrastructure.database import BookDB  # SQLAlchemy-модель

class BookRepositoryImpl(BookRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all(self) -> List[Book]:
        return self.db.query(BookDB).all()

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.db.query(BookDB).filter(BookDB.id == book_id).first()

    def add(self, book: Book) -> Book:
        db_book = BookDB(**book.__dict__)
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def update(self, book: Book) -> Book:
        db_book = self.db.query(BookDB).filter(BookDB.id == book.id).first()
        if db_book:
            for key, value in book.__dict__.items():
                setattr(db_book, key, value)
            self.db.commit()
            self.db.refresh(db_book)
        return db_book

    def delete(self, book_id: int) -> None:
        self.db.query(BookDB).filter(BookDB.id == book_id).delete()
        self.db.commit()
```

📌 Здесь:
- `BookDB` — это SQLAlchemy-модель, которая будет храниться в БД.
- Этот класс реализует интерфейс `BookRepository`, используя SQLAlchemy.

---

### 📌 **Шаг 6: Реализация use-case (Application Layer)**
Файл `app/application/use_cases.py`:

```python
from app.domain.models import Book
from app.domain.repositories import BookRepository
from typing import List, Optional

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def list_books(self) -> List[Book]:
        return self.repository.get_all()

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.repository.get_by_id(book_id)

    def create_book(self, title: str, author: str, published_year: int) -> Book:
        book = Book(id=None, title=title, author=author, published_year=published_year)
        return self.repository.add(book)

    def update_book(self, book: Book) -> Book:
        return self.repository.update(book)

    def delete_book(self, book_id: int) -> None:
        self.repository.delete(book_id)
```

📌 Здесь:
- `BookService` работает с `BookRepository`, но **не знает о БД**.

---

### 📌 **Шаг 7: Подключаем FastAPI**
Файл `app/presentation/api/books.py`:

```python
from fastapi import APIRouter, Depends
from app.application.use_cases import BookService
from app.presentation.schemas import BookSchema

router = APIRouter()

@router.get("/", response_model=List[BookSchema])
def list_books(service: BookService = Depends()):
    return service.list_books()
```

