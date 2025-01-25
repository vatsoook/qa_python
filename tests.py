import pytest
from main import BooksCollector


class TestBooksCollector:


    @pytest.mark.parametrize("books_data, expected_result",
                             [

                                 ({"Книга 1": "Фантастика", "Книга 2": "Мультфильмы"}, ["Книга 1", "Книга 2"]),

                                 ({"Книга 1": "Фантастика", "Книга 2": "Ужасы", "Книга 3": "Комедии"},
                                  ["Книга 1", "Книга 3"]),

                                 ({"Книга 1": "Ужасы", "Книга 2": "Детективы"}, []),

                                 ({}, []),

                                 ({"Книга 1": "Фантастика", "Книга 2": "Комедии", "Книга 3": "Мультфильмы"},
                                  ["Книга 1", "Книга 2", "Книга 3"])
                             ]
                             )
    def test_get_books_for_children_two_books(self, books_data, expected_result):
        collector = BooksCollector()
        collector.books_genre = books_data
        assert collector.get_books_for_children() == expected_result



def test_add_new_book_add_one_books_true (test_books_collector):
    test_books_collector.add_new_book("Книга 1")
    assert "Книга 1" in test_books_collector.get_books_genre()

def test_add_new_book_repeated_name_false(test_books_collector):
    test_books_collector.add_new_book("Книга 1")
    assert len(test_books_collector.books_genre) == 1, "Книга не должна добавиться повторно"

def test_add_new_book_long_name_false(test_books_collector):
    test_books_collector.add_new_book("Книга с длинным названием" + "a" * 40)
    assert len(test_books_collector.books_genre) == 0, "Книга с длинным названием не должна добавляться"


def test_set_book_genre_book_collection_fantastic(test_books_collector):
    test_books_collector.add_new_book("Книга 1")
    test_books_collector.set_book_genre("Книга 1", "Фантастика")
    assert test_books_collector.get_book_genre("Книга 1") == "Фантастика"

def test_set_book_genre_defunct_book_false(test_books_collector):
    test_books_collector.set_book_genre("Несуществующая книга", "Фантастика")
    assert test_books_collector.get_book_genre("Несуществующая книга") == None

def test_set_book_genre_defunct_genre_false(test_books_collector):
    test_books_collector.set_book_genre("Книга 1", "Несуществующий жанр")
    assert test_books_collector.get_book_genre("Книга 1") != "Фантастика", "Жанр не должен измениться для несуществующего жанра"


def test_get_books_with_specific_genre_set_genre_true(test_books_collector):
    test_books_collector.add_new_book("Книга 1")
    test_books_collector.set_book_genre("Книга 1", "Фантастика")

    test_books_collector.add_new_book("Книга 2")
    test_books_collector.set_book_genre("Книга 2", "Фантастика")

    test_books_collector.add_new_book("Книга 3")
    test_books_collector.set_book_genre("Книга 3", "Комедии")

    assert sorted(test_books_collector.get_books_with_specific_genre("Фантастика")) == sorted(["Книга 1", "Книга 2"])
    assert test_books_collector.get_books_with_specific_genre("Комедии") == ["Книга 3"]


def test_add_remove_favorites_cannot_add_again(test_books_collector):
    test_books_collector.add_book_in_favorites("Книга 1")
    assert len(test_books_collector.favorites) == 0, "Книга не должна добавляться повторно в избранное"


def test_add_remove_favorites_delete_books(test_books_collector):
    test_books_collector.delete_book_from_favorites("Книга 1")
    assert "Книга 1" not in test_books_collector.get_list_of_favorites_books()


def test_get_book_genre_by_name(test_books_collector):
    test_books_collector.add_new_book("Книга 1")
    test_books_collector.set_book_genre("Книга 1", "Фантастика")
    test_books_collector.add_new_book("Книга 2")
    test_books_collector.set_book_genre("Книга 2", "Ужасы")

    assert test_books_collector.get_book_genre("Книга 1") == "Фантастика"
    assert test_books_collector.get_book_genre("Книга 2") == "Ужасы"


def test_get_list_of_favorites_books_true(test_books_with_favorites):
    assert set(test_books_with_favorites.get_list_of_favorites_books()) == {"Книга 1", "Книга 2"}