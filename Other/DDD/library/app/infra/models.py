from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

    def to_domain(self):
        from ..domain.book import Book, Author
        return Book(id=self.id, title=self.title, author=Author(name=self.author),
                    is_available=self.is_available)


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    borrowed_books = relationship("BorrowedBookModel", back_populates="user")

    def to_domain(self):
        from ..domain.user import User
        return User(id=self.id, name=self.name,
                    borrowed_books=[bb.book_id for bb in self.borrowed_books])


class BorrowedBookModel(Base):
    __tablename__ = "borrowed_books"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)

    user = relationship("UserModel", back_populates="borrowed_books")
    book = relationship("BookModel")
