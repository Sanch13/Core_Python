from dataclasses import dataclass


@dataclass(frozen=True)
class Author:
    name: str


@dataclass
class Book:
    id: int
    title: str
    author: Author
    is_available: bool = True

    def borrow(self):
        if self.is_available:
            self.__dict__["is_available"] = False  # Изменяем mutable состояние
        else:
            raise ValueError("Книга уже выдана")

    def return_book(self):
        if not self.is_available:
            self.__dict__["is_available"] = True
        else:
            raise ValueError("Книга уже доступна")
