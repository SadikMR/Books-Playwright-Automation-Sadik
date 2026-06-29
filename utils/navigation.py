from pages.home_page import HomePage
from pages.category_page import CategoryPage


def iterate_random_books(home: HomePage, category: CategoryPage, page):
    home.open()

    selected_categories = home.random_categories()

    for selected_category in selected_categories:

        category_name = home.open_category(selected_category)

        category.verify_category_loaded(category_name)

        selected_books = category.random_books()

        for book_index in selected_books:

            homepage_data = category.open_book(book_index)

            yield homepage_data

            page.go_back()

            # Wait until the category page is fully loaded again
            category.verify_category_loaded(category_name)

        page.go_back()

        # Wait until the homepage is fully loaded again
        home.verify_homepage_loaded()