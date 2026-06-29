import pytest

from pages.book_page import BookPage
from pages.home_page import HomePage


@pytest.mark.smoke
def test_book_details(page):
    home = HomePage(page)

    home.open()
    home.open_first_book()

    book = BookPage(page)

    book.verify_book_loaded()
    book.verify_title()
    book.verify_price()
    book.verify_availability()
    book.verify_image()
    book.verify_description()