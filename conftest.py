import pytest
from main import BooksCollector


@pytest.fixture
def single_book():
    # предподготовленный список из одной книги для простых проверок
    book_name = 'Шерлок Холмс'
    book_genre = 'Детективы'

    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, book_genre)

    return collector.get_books_genre()


@pytest.fixture
def set_of_books():
    # предподготовленный список из четырёх книг для работы со списками
    books_name = ['Шерлок Холмс', 'Понедельник начинается в субботу', 'Остров сокровищ', 'Граф Дракула']
    books_genre = ['Детективы', 'Фантастика', 'Фантастика', 'Ужасы']

    collector = BooksCollector()
    for b in range(0, len(books_name)):
        collector.add_new_book(books_name[b])
        collector.set_book_genre(books_name[b], books_genre[b])

    return collector.get_books_genre()