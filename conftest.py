import pytest

from main import BooksCollector

@pytest.fixture(scope="function")
def test_books_collector():
        return BooksCollector()