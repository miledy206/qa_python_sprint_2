from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Понедельник начинается в субботу')
        books_list = collector.get_books_genre()

        # проверяем, что добавилось именно две
        assert len(books_list.keys()) == 2

    def test_add_new_book_check_genre_is_empty_for_one_book(self):
        """простая проверка, что жанр выставляется пустой для новой книги"""

        collector = BooksCollector()
        book = 'Шерлок Холмс'
        collector.add_new_book(book)

        assert collector.get_book_genre(book) == ''

    def test_set_book_genre_for_one_book_set_value_of_genre_out_of_list(self):
        """ проверка, что жанр может быть поставлен книге, только если он есть в списке жанров """

        collector = BooksCollector()
        book = 'Шерлок Холмс'
        genre = 'Роман'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == ''

    def test_get_book_genre_one_book_return_correct_value_of_genre(self):
        """ проверка, что жанр вовращается корректный по методу get """

        collector = BooksCollector()
        book = 'Шерлок Холмс'
        genre = 'Детективы'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == 'Детективы'

    def test_get_books_with_specific_genre_for_four_books_return_correct_number_of_books_by_genre(self, set_of_books):
        """проверка, что поиск по жанру возвращает корректное число книг"""

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre_for_four_books_return_correct_number_of_books(self, set_of_books):
        """проверка, что список книг вовращается корректный по методу get"""

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_genre()) == 4

    def test_get_books_for_children_for_four_books_return_correct_number_of_books(self, set_of_books):
        """проверка, что список книг для детей имеет корректное количество книг после применения метода"""

        collector = BooksCollector()
        collector.books_genre = set_of_books

        assert len(collector.get_books_for_children()) == 2

    def test_get_books_for_children_for_four_books_check_items_from_genre_age_rating_not_in_list(self, set_of_books):
        """проверка, что книги с одним из жанров для взрослых не в списке книг для детей"""

        collector = BooksCollector()
        collector.books_genre = set_of_books
        books_for_children = collector.get_books_for_children()

        assert collector.genre_age_rating[0] not in books_for_children

    def test_add_book_in_favorites_one_book_will_added_successfully(self):
        """добавление книги из справочника книг в избранное"""

        collector = BooksCollector()
        book = 'Шерлок Холмс'
        genre = 'Детективы'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        collector.add_book_in_favorites(book)

        assert book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_one_book_not_from_books_dictionary_will_not_added(self, set_of_books):
        """попытка добавления книги НЕ из справочника книг в избранное"""

        collector = BooksCollector()

        book_out_of_list = 'Гостья'
        collector.books_genre = set_of_books
        collector.add_book_in_favorites(book_out_of_list)

        assert book_out_of_list not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_will_removed_successfully(self, single_book):
        """удаление книги из избранного"""

        collector = BooksCollector()
        book = 'Шерлок Холмс'
        genre = 'Детективы'

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert 'Шерлок Холмс' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_will_not_found_in_list(self, single_book):
        """попытка удаления книги, которой нет в избранном, из избранного"""

        collector = BooksCollector()
        collector.books_genre = single_book
        book_out_of_list = 'Гостья'

        collector.add_book_in_favorites(str(list(single_book.keys())[0]))
        collector.delete_book_from_favorites(book_out_of_list)

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_three_added_books_present_in_the_list(self, set_of_books):
        """проверка, что количество избранных книг соответствует количеству добавленных книг"""

        collector = BooksCollector()
        collector.books_genre = set_of_books
        collector.add_book_in_favorites(str(list(set_of_books.keys())[0]))
        collector.add_book_in_favorites(str(list(set_of_books.keys())[1]))
        collector.add_book_in_favorites(str(list(set_of_books.keys())[2]))

        assert len(collector.get_list_of_favorites_books()) == 3
