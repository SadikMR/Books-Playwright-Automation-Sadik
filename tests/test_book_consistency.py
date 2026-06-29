import pytest

from pages.book_page import BookPage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from utils.navigation import iterate_random_books


@pytest.mark.regression
def test_book_consistency(page):

    home = HomePage(page)
    category = CategoryPage(page)
    book = BookPage(page)

    for homepage_data in iterate_random_books(home, category, page):

        book.verify_book_loaded(homepage_data["title"])

        assert homepage_data["title"] == book.title()
        assert homepage_data["price"] == book.price()