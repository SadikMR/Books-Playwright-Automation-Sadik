from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.selectors import CategorySelectors
from utils.helper import choose_random


class CategoryPage(BasePage):

    def verify_category_loaded(self, category_name):
        self.logger.info(
            f"Verifying category: {category_name}"
        )

        expect(
            self.locator(CategorySelectors.HEADER)
        ).to_have_text(category_name)

        self.logger.info("✓ Category page loaded.")

    def books(self):
        return self.locator(CategorySelectors.BOOKS)
    
    def random_books(self, count=5):
        self.logger.info("Selecting random books...")

        books = self.books().all()

        selected = choose_random(books, count)

        self.logger.info(
            f"Selected {len(selected)} random book(s)."
        )

        return selected
    
    def open_book(self, book):
        title = book.locator("h3 a").get_attribute("title")

        self.logger.info(f"Opening book: {title}")

        book.locator("h3 a").click()

        return title