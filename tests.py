import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def single_book(self):
        # предподготовленный список из одной книги для простых проверок
        book_name = 'Шерлок Холмс'
        book_genre = 'Детективы'

        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        return collector.books_genre

    @pytest.fixture
    def set_of_books(self):
        # предподготовленный список из четырёх книг для работы со списками
        books_name = ['Шерлок Холмс', 'Понедельник начинается в субботу', 'Остров сокровищ', 'Граф Дракула']
        books_genre = ['Детективы', 'Фантастика', 'Фантастика', 'Ужасы']

        collector = BooksCollector()
        for b in range(0, len(books_name)):
            collector.add_new_book(books_name[b])
            collector.set_book_genre(books_name[b], books_genre[b])

        return collector.books_genre

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Понедельник начинается в субботу')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_check_genre_is_empty_for_one_book(self):
        # простая проверка, что жанр выставляется пустой для новой книги

        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')

        assert str(list(collector.books_genre.values())[0]) == ''

    def test_set_book_genre_for_one_book_set_value_of_genre_out_of_list(self):
        # проверка, что жанр может быть поставлен книге, только если он есть в списке жанров

        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Роман')

        assert str(list(collector.books_genre.values())[0]) == ''

    def test_get_book_genre_one_book_return_correct_value_of_genre(self, single_book):
        # проверка, что жанр вовращается корректный по методу get

        collector = BooksCollector()
        collector.books_genre = single_book

        # тут получилась палка о двух концах: либо надо было просто ввести параметризацию
        # тогда 2 строчки кода на наполнение справочника будут в каждом аналогичном кейсе
        # либо как тут, двойное преобразование, которое тоже выглядит не очень :(
        ask_book_genre = collector.get_book_genre(str(list(single_book.keys())[0]))

        assert ask_book_genre == 'Детективы'

    def test_get_books_with_specific_genre_for_four_books_return_correct_number_of_books_by_genre(self, set_of_books):
        # проверка, что поиск по жанру возвращает корректное число книг

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre_for_four_books_return_correct_number_of_books(self, set_of_books):
        # проверка, что список книг вовращается корректный по методу get

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_genre()) == 4

    def test_get_books_for_children_for_four_books_return_correct_number_of_books(self, set_of_books):
        # проверка, что список книг для детей имеет корректное количество книг после применения метода

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_for_children()) == 2

    def test_get_books_for_children_for_four_books_check_items_from_genre_age_rating_not_in_list(self, set_of_books):
        # проверка, что книги с одним из жанров для взрослых не в списке книг для детей

        collector = BooksCollector()
        collector.books_genre = set_of_books
        books_for_children = collector.get_books_for_children()

        assert collector.genre_age_rating[0] not in books_for_children

    def test_add_book_in_favorites_one_book_will_added_successfully(self, single_book):
        # добавление книги из справочника книг в избранное

        collector = BooksCollector()
        collector.books_genre = single_book
        collector.add_book_in_favorites(str(list(single_book.keys())[0]))

        assert 'Шерлок Холмс' in collector.favorites

    def test_add_book_in_favorites_one_book_not_from_books_dictionary_will_not_added(self, set_of_books):
        # попытка добавления книги НЕ из справочника книг в избранное

        collector = BooksCollector()

        book_out_of_list = 'Гостья'
        collector.books_genre = set_of_books
        collector.add_book_in_favorites(book_out_of_list)

        assert 'Гостья' not in collector.favorites

    def test_delete_book_from_favorites_one_book_will_removed_successfully(self, single_book):
        # удаление книги из избранного

        collector = BooksCollector()
        collector.books_genre = single_book
        collector.add_book_in_favorites(str(list(single_book.keys())[0]))
        collector.delete_book_from_favorites(str(list(single_book.keys())[0]))

        assert 'Шерлок Холмс' not in collector.favorites

    def test_delete_book_from_favorites_one_book_will_not_found_in_list(self, single_book):
        # попытка удаления книги, которой нет в избранном, из избранного

        collector = BooksCollector()
        collector.books_genre = single_book
        book_out_of_list = 'Гостья'

        collector.add_book_in_favorites(str(list(single_book.keys())[0]))
        collector.delete_book_from_favorites(book_out_of_list)

        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_three_added_books_present_in_the_list(self, set_of_books):
        # проверка, что количество избранных книг соответствует количеству добавленных книг

        collector = BooksCollector()
        collector.books_genre = set_of_books
        collector.add_book_in_favorites(str(list(set_of_books.keys())[0]))
        collector.add_book_in_favorites(str(list(set_of_books.keys())[1]))
        collector.add_book_in_favorites(str(list(set_of_books.keys())[2]))

        assert len(collector.get_list_of_favorites_books()) == 3
