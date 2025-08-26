from ..domain.book import Book
from ..domain.user import User
from ..infra.database import Database
from ..infra.models import BookModel, UserModel, BorrowedBookModel


class BookRepository:
    def __init__(self, db: Database):
        self.db = db

    def add(self, book: Book):
        """Добавляет новую книгу."""
        with self.db.get_session() as session:
            book_model = BookModel(
                id=book.id,
                title=book.title,
                author=str(book.author.name),
                is_available=book.is_available
            )
            session.add(book_model)
            session.commit()

    def get(self, book_id: int) -> Book:
        """Возвращает книгу по ID."""
        with self.db.get_session() as session:
            book_model = session.query(BookModel).filter_by(id=book_id).first()
            if book_model:
                return book_model.to_domain()
            return None

    def update(self, book: Book):
        """Обновляет существующую книгу."""
        with self.db.get_session() as session:
            book_model = session.query(BookModel).filter_by(id=book.id).first()
            if book_model:
                book_model.title = book.title
                book_model.author = str(book.author.name)
                book_model.is_available = book.is_available
                session.commit()

    def delete(self, book_id: int):
        """Удаляет книгу."""
        with self.db.get_session() as session:
            book_model = session.query(BookModel).filter_by(id=book_id).first()
            if book_model:
                session.delete(book_model)
                session.commit()

    def get_all(self):
        """Возвращает все книги."""
        with self.db.get_session() as session:
            return [book_model.to_domain() for book_model in session.query(BookModel).all()]


class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def add(self, user: User):
        """Добавляет нового пользователя."""
        with self.db.get_session() as session:
            user_model = UserModel(id=user.id, name=user.name)
            session.add(user_model)
            session.commit()

    def get(self, user_id: int) -> User:
        """Возвращает пользователя по ID."""
        with self.db.get_session() as session:
            user_model = session.query(UserModel).filter_by(id=user_id).first()
            if user_model:
                return user_model.to_domain()
            return None

    def borrow_book(self, user_id: int, book_id: int):
        """Зарегистрирует выдачу книги пользователю."""
        with self.db.get_session() as session:
            borrowed_book = BorrowedBookModel(user_id=user_id, book_id=book_id)
            session.add(borrowed_book)
            session.commit()

    def return_book(self, user_id: int, book_id: int):
        """Зарегистрирует возврат книги пользователем."""
        with self.db.get_session() as session:
            borrowed_book = session.query(BorrowedBookModel).filter_by(user_id=user_id,
                                                                       book_id=book_id).first()
            if borrowed_book:
                session.delete(borrowed_book)
                session.commit()
