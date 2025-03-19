from ..application.use_cases import LibraryUseCases
from ..infra.repositories import InMemoryBookRepository, InMemoryUserRepository
from ..domain.user import User


def main():
    book_repo = InMemoryBookRepository()
    user_repo = InMemoryUserRepository()
    library = LibraryUseCases(book_repo, user_repo)

    # Добавляем пользователя
    user = User(id=1, name="John Doe")
    user_repo.add(user)

    # Добавляем книги
    library.add_book("Clean Code", "Robert Martin")
    library.add_book("The Pragmatic Programmer", "Andrew Hunt")

    # Выдаем книгу
    try:
        library.borrow_book(1, 1)
        print("Книга успешно выдана!")
    except ValueError as e:
        print(e)

    # Возвращаем книгу
    try:
        library.return_book(1, 1)
        print("Книга успешно возвращена!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
