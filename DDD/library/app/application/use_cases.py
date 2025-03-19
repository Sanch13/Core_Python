from ..domain.book import Book, Author
from ..domain.user import User


class LibraryUseCases:
    def __init__(self, book_repo, user_repo):
        self.book_repo = book_repo
        self.user_repo = user_repo

    def add_book(self, title, author_name):
        """Добавляет новую книгу."""
        books = self.book_repo.get_all()
        book_id = len(books) + 1
        book = Book(id=book_id, title=title, author=Author(name=author_name))
        self.book_repo.add(book)

    def borrow_book(self, user_id, book_id):
        """Выдает книгу пользователю."""
        book = self.book_repo.get(book_id)
        if not book or not book.is_available:
            raise ValueError("Книга недоступна или не существует")

        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("Пользователь не найден")

        # Проверяем, что у пользователя нет другой книги
        borrowed_books = self.user_repo.get_borrowed_books(user_id)
        if len(borrowed_books) >= 1:
            raise ValueError("Пользователь может взять только одну книгу")

        # Выдаем книгу
        book.borrow()
        self.book_repo.update(book)
        self.user_repo.borrow_book(user_id, book_id)

    def return_book(self, user_id, book_id):
        """Возвращает книгу."""
        book = self.book_repo.get(book_id)
        if not book or book.is_available:
            raise ValueError("Книга уже доступна или не существует")

        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("Пользователь не найден")

        # Возвращаем книгу
        book.return_book()
        self.book_repo.update(book)
        self.user_repo.return_book(user_id, book_id)
