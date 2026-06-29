import pytest

from pages.category_page import CategoryPage
from pages.home_page import HomePage


@pytest.mark.regression
def test_random_categories(page):

    home = HomePage(page)
    category = CategoryPage(page)

    home.open()

    selected = home.random_categories()

    for item in selected:
        name = home.open_category(item)

        category.verify_category_loaded(name)

        selected_books = category.random_books()

        assert len(selected_books) == 5

        page.go_back()