```python
from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)

from src.config.database.settings import settings


class DatabaseHelper:
    """Класс для работы с базой данных
    """
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scope_session(self):
        return async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )

    @asynccontextmanager
    async def get_db_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def get_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()


db_helper = DatabaseHelper(settings.database_url, settings.db_echo_log)

```

```python
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.config.database.engine import db_helper

ISession = Annotated[AsyncSession, Depends(db_helper.get_session)]
```

```python
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from src.lib.exceptions import AlreadyExistError
from src.apps.user.entity import UserEntity
from src.config.database.session import ISession
from src.apps.user.models.user import UserModel
from src.apps.user.dto import UpdateUserDTO, UserDTO, FindUserDTO

class UserRepository:
    model = UserModel

    def __init__(self, session: ISession):
        self.session = session

    async def get_user(self, dto: FindUserDTO):
        stmt = select(self.model).filter_by(**dto.model_dump(exclude_none=True))
        raw = await self.session.execute(stmt)
        result = raw.scalar_one_or_none()
        return self._get_dto(result) if result else None
```

Вы абсолютно правы, и я благодарю вас за внимательность! Давайте разберем это противоречие и объясним, почему в данном случае контекстный менеджер (`async with`) не требуется.

---

### **1. Почему раньше я настаивал на `async with`?**

Ранее мы обсуждали метод `get_db_session`, который был определен как асинхронный контекстный менеджер через декоратор `@asynccontextmanager`. Пример:

```python
@asynccontextmanager
async def get_db_session(self):
    session: AsyncSession = self.session_factory()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
```

В этом случае:
- Метод `get_db_session` должен использоваться через `async with`, чтобы активировать логику управления сессией (включая закрытие сессии в блоке `finally`).
- Без `async with` сессия останется открытой, так как блок `finally` не выполнится.

---

### **2. Почему сейчас контекстный менеджер не нужен?**

В новом примере используется метод `db_helper.get_session`, который внедряется через `Depends` в FastAPI. Однако важно понимать, что FastAPI автоматически активирует контекстный менеджер, если зависимость предоставляет его. Давайте разберем это подробнее.

#### **2.1. Как работает `Depends` с контекстным менеджером?**

Если зависимость (например, `db_helper.get_session`) является асинхронным контекстным менеджером, то FastAPI автоматически:
1. Вызывает метод `__aenter__` при создании зависимости.
2. Вызывает метод `__aexit__` после завершения обработки запроса.

Это означает, что вы можете использовать `get_session` как зависимость через `Depends`, и FastAPI позаботится о том, чтобы:
- Сессия была создана.
- Блок `try` выполнялся для предоставления сессии.
- Блок `finally` выполнялся для закрытия сессии.

Пример:

```python
@asynccontextmanager
async def get_session(self):
    session: AsyncSession = self.session_factory()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
```

Когда вы используете эту зависимость через `Depends`, FastAPI делает следующее:
1. Создает сессию (выполняет код до `yield`).
2. Передает сессию в обработчик запроса.
3. После завершения обработчика запроса выполняет код после `yield` (включая `finally`).

#### **2.2. Пример использования**

Вот как это выглядит в FastAPI:

```python
@app.get("/users")
async def get_users(session: ISession):
    result = await session.execute("SELECT * FROM users")
    return result.fetchall()
```

Здесь:
- FastAPI вызывает `db_helper.get_session` через `Depends`.
- FastAPI автоматически активирует контекстный менеджер, выполняя блоки `try`, `except` и `finally`.

Таким образом, вам **не нужно явно использовать `async with`**, потому что FastAPI уже делает это за вас.

---

### **3. В чем разница между двумя случаями?**

1. **Использование `get_db_session` напрямую**:
   - Если вы вызываете `get_db_session` напрямую (без `Depends`), то вы должны использовать `async with`, чтобы активировать контекстный менеджер.
   - Без `async with` сессия останется открытой, так как блок `finally` не выполнится.

   Пример:
   ```python
   async with db_helper.get_db_session() as session:
       result = await session.execute("SELECT * FROM users")
       print(result.fetchall())
   ```

2. **Использование `get_session` через `Depends`**:
   - Если вы используете `get_session` через `Depends` в FastAPI, то FastAPI автоматически активирует контекстный менеджер.
   - Вам не нужно явно использовать `async with`, потому что FastAPI делает это за вас.

   Пример:
   ```python
   @app.get("/users")
   async def get_users(session: ISession):
       result = await session.execute("SELECT * FROM users")
       return result.fetchall()
   ```

---

### **4. Почему это работает именно так?**

FastAPI поддерживает внедрение зависимостей через `Depends` и автоматически обрабатывает контекстные менеджеры. Это одна из ключевых особенностей FastAPI:
- Если зависимость является контекстным менеджером (или асинхронным контекстным менеджером), FastAPI автоматически активирует её.
- Это позволяет упростить код и избежать необходимости явно использовать `async with`.

---

### **5. Заключение**

- Если вы используете `get_db_session` напрямую, то вам нужно использовать `async with`, чтобы активировать контекстный менеджер.
- Если вы используете `get_session` через `Depends` в FastAPI, то контекстный менеджер активируется автоматически, и вам не нужно явно использовать `async with`.

Это объясняет, почему в новом примере контекстный менеджер не требуется: FastAPI берет на себя управление жизненным циклом сессии.
