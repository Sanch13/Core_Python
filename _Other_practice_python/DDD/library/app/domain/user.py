from dataclasses import dataclass
from typing import List


@dataclass
class User:
    id: int
    name: str
    borrowed_books: List[int] = None

    def __post_init__(self):
        self.borrowed_books = self.borrowed_books or []

    def borrow_book(self, book_id: int):
        if len(self.borrowed_books) >= 1:
            raise ValueError("Пользователь может взять только одну книгу")
        self.borrowed_books.append(book_id)

    def return_book(self, book_id: int):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
        else:
            raise ValueError("Книга не была взята этим пользователем")
