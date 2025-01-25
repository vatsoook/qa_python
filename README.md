1. test_get_books_for_children_two_books # Проверяем фильтрацию книг по жанру, чтобы возвращать только те книги, которые подходят для детей 
2. test_add_new_book_add_one_books_true : #Проверяем добавление новой книги
3. test_add_new_book_repeated_name_false: # Проверяем, что не добавляется книга с повторным названием
4. test_add_new_book_long_name_false:   # Проверяем, что книга с длинным названием не добавляется
5. test_set_book_genre_book_collection_fantastic: # проверяем, корректно ли устанавливается жанр книги
6. test_set_book_genre_defunct_book_false:# Проверяем, что нельзя установить жанр для несуществующей книги
7. test_set_book_genre_defunct_genre_false: # Проверяем, что нельзя установить несуществующий жанр
8. test_get_books_with_specific_genre_set_genre_true:   # проверяем, добавление книг и назначение им жанров, а также может ли корректно возвращать список книг по заданному жанру
9. test_add_remove_favorites_cannot_add_again: # Проверяем, что нельзя добавить книгу повторно в избранное
10. test_add_remove_favorites_delete_books: # Удаляем книгу из избранного
11. test_get_book_genre_by_name  # проверяем получение жанр книги по её имени
12. test_get_list_of_favorites_books_true # Проверяем получение списка избранных книг
