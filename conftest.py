import pytest

from main import BooksCollector

@pytest.fixture(scope="function")
def test_books_collector():
        return BooksCollector()


@pytest.fixture
def test_books_with_favorites():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.add_book_in_favorites("Книга 1")
    collector.add_book_in_favorites("Книга 2")
    return collector