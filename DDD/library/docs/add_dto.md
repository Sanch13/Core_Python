### 📌 **Что такое DTO? И зачем он нужен?**  

**DTO (Data Transfer Object)** — это объект, который используется для передачи данных между слоями приложения.  

📌 **Зачем использовать DTO?**  
1. 🔹 **Изоляция доменной модели** — данные могут передаваться в изменённом формате, без влияния на внутреннюю модель.  
2. 🔹 **Безопасность** — можно скрыть внутренние поля (`id`, `пароли`) от клиента.  
3. 🔹 **Гибкость** — можно комбинировать данные из разных источников перед отправкой в API.  
4. 🔹 **Валидация** — DTO помогает валидировать входящие данные.  

📌 **Простая аналогия**:  
📦 **Domain Model (Модель БД)** → **DTO** → 🚚 **Отправка в API**  

---

### 📌 **Где внедрим DTO?**
1. **Входные данные** (`CreateBookDTO`, `UpdateBookDTO`) — когда клиент отправляет данные в API.  
2. **Выходные данные** (`BookDTO`) — когда данные возвращаются клиенту.  

---

### 📌 **Создадим DTO с Pydantic**  

📂 `app/presentation/schemas.py`  

```python
from pydantic import BaseModel, Field
from typing import Optional

class BookDTO(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

    class Config:
        from_attributes = True  # Позволяет работать с ORM-моделями SQLAlchemy

class CreateBookDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    published_year: int = Field(..., ge=0, le=2100)  # Ограничение года

class UpdateBookDTO(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    published_year: Optional[int] = Field(None, ge=0, le=2100)
```

📌 **Объяснение кода**:
- `BookDTO` → DTO для ответа в API.
- `CreateBookDTO` → DTO для создания книги.
- `UpdateBookDTO` → DTO для обновления (все поля опциональны).
- `Field(...)` → задаёт валидацию (`min_length`, `max_length`, `ge`, `le`).
- `from_attributes = True` → Позволяет автоматически преобразовывать SQLAlchemy-объекты.

---

### 📌 **Используем DTO в сервисе**  

📂 `app/application/use_cases.py`

```python
from app.domain.models import Book
from app.domain.repositories import BookRepository
from app.presentation.schemas import CreateBookDTO, UpdateBookDTO, BookDTO
from typing import List, Optional

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def list_books(self) -> List[BookDTO]:
        books = self.repository.get_all()
        return [BookDTO.model_validate(book) for book in books]

    def get_book(self, book_id: int) -> Optional[BookDTO]:
        book = self.repository.get_by_id(book_id)
        return BookDTO.model_validate(book) if book else None

    def create_book(self, book_data: CreateBookDTO) -> BookDTO:
        book = Book(id=None, **book_data.model_dump())
        new_book = self.repository.add(book)
        return BookDTO.model_validate(new_book)

    def update_book(self, book_id: int, book_data: UpdateBookDTO) -> Optional[BookDTO]:
        book = self.repository.get_by_id(book_id)
        if not book:
            return None
        
        updated_data = book_data.model_dump(exclude_unset=True)  # Убираем None
        for key, value in updated_data.items():
            setattr(book, key, value)

        updated_book = self.repository.update(book)
        return BookDTO.model_validate(updated_book)

    def delete_book(self, book_id: int) -> None:
        self.repository.delete(book_id)
```

📌 **Что изменилось?**  
✅ Теперь сервис принимает и возвращает **DTO**, а не доменные модели.  
✅ `model_validate(book)` — преобразует SQLAlchemy-модель в DTO.  
✅ `model_dump(exclude_unset=True)` — убирает `None` из `UpdateBookDTO`.  

---

### 📌 **Используем DTO в FastAPI**  
📂 `app/presentation/api/books.py`

```python
from fastapi import APIRouter, Depends, HTTPException
from app.application.use_cases import BookService
from app.presentation.schemas import BookDTO, CreateBookDTO, UpdateBookDTO
from typing import List

router = APIRouter()

@router.get("/", response_model=List[BookDTO])
def list_books(service: BookService = Depends()):
    return service.list_books()

@router.get("/{book_id}", response_model=BookDTO)
def get_book(book_id: int, service: BookService = Depends()):
    book = service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/", response_model=BookDTO)
def create_book(book_data: CreateBookDTO, service: BookService = Depends()):
    return service.create_book(book_data)

@router.put("/{book_id}", response_model=BookDTO)
def update_book(book_id: int, book_data: UpdateBookDTO, service: BookService = Depends()):
    book = service.update_book(book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, service: BookService = Depends()):
    service.delete_book(book_id)
    return {"message": "Книга удалена"}
```

📌 **Что изменилось?**  
✅ Теперь API принимает DTO (`CreateBookDTO`, `UpdateBookDTO`) вместо "сырого" `dict`.  
✅ DTO автоматически **валидирует входящие данные**.  
✅ `BookDTO` используется в `response_model`, чтобы гарантировать корректный ответ.  

---

### 📌 **Как проверить API?**
Запусти сервер:  
```sh
uvicorn app.main:app --reload
```
Открывай **Swagger** по адресу:  
📌 `http://127.0.0.1:8000/docs`

**Тестируем API через cURL:**
```sh
# Добавляем книгу
curl -X 'POST' 'http://127.0.0.1:8000/books/' \
-H 'Content-Type: application/json' \
-d '{"title": "1984", "author": "Джордж Оруэлл", "published_year": 1949}'

# Получаем список книг
curl -X 'GET' 'http://127.0.0.1:8000/books/'
```

---

### 📌 **Что мы сделали?**
✅ Внедрили **DTO** в проект.  
✅ **Разделили доменную логику и API.**  
✅ **Добавили валидацию** входных данных через Pydantic.  

---

🔥 **Что дальше?**
1. 📌 **Добавим авторизацию (JWT)**.
2. 📌 **Реализуем Alembic для миграций**.
3. 📌 **Добавим Unit-тесты**.

Какой шаг делать следующим? 🚀
