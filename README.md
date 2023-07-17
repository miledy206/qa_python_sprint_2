# qa_python

#### The project was created for studying of Python unit test.
#### This project contains the one class BookCollector with the list of methods.
#### There was used the pytest lib for creating and running unit-tests

### List of methods (main.py):
* **add_new_book** - add a book in the dictionary
* **set_book_genre** - add a genre to the book from the existing list
* **get_book_genre** - return a genre by the name of the book from the dictionary
* **get_books_with_specific_genre** - return the list of books by specific genre from the dictionary
* **get_books_genre** - return the dictionary with all added books with genres
* **get_books_for_children** - return the list of books for children especially
* **add_book_in_favorites** - add a book from the dictionary to a favorite list
* **delete_book_from_favorites** - delete the book from the favorite list
* **get_list_of_favorites_books** - return the list of the favorites books

#### Every method was covered at least by one unit test

### List of unit-tests (tests.py):
* **test_add_new_book_add_two_books** - check, that 2 added books present in the dictionary
* **test_add_new_book_check_genre_is_empty_for_one_book** - check, that a genre is empty for new added book
* **test_set_book_genre_for_one_book_set_correct_value_of_genre** - check, that a genre from the list will be added into the dictionary for the book
* **test_set_book_genre_for_one_book_set_value_of_genre_out_of_list** - check, that genre NOT from the list will NOT be added into the dictionary for the book
* **test_get_book_genre_one_book_return_correct_value_of_genre** - check, that the get method returns the correct genre by the name of the book
* **test_get_books_with_specific_genre_for_four_books_return_correct_number_of_books_by_genre** - check, that get method returns the correct list of books by specific genre
* **test_get_books_genre_for_four_books_return_correct_number_of_books** - check, that the get method return the correct number of dictionary pairs
* **test_get_books_for_children_for_four_books_return_correct_number_of_books** - check, that the list of books for children has the correct number of books
* **test_get_books_for_children_for_four_books_check_items_from_genre_age_rating_not_in_list** - check, that the list of books for children does not have the genre from the age rating list
* **test_add_book_in_favorites_one_book_will_added_successfully** - check, that book from dictionary will be added to a favorite list successfully
* **test_add_book_in_favorites_one_book_not_from_books_dictionary_will_not_added** - check, that book NOT from dictionary will NOT be added to a favorite list
* **test_delete_book_from_favorites_one_book_will_removed_successfully** - check, that a book from favorite list will be removed successfully
* **test_delete_book_from_favorites_one_book_will_not_found_in_list** - check, that method does nothing with the book NOT from the favorite list during removing
* **test_get_list_of_favorites_books_three_added_books_present_in_the_list** - check, that the get method returns the correct number of added favorite books in the favorite list

*the test coverage is not 100%, some of "if" cases were not covered*