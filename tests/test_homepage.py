import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
def test_homepage(page):
    home = HomePage(page)

    home.open()
    home.verify_homepage()
    home.verify_homepage_loaded()
    home.verify_all_headings()
    home.verify_books_section()