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

        total = self.books().count()

        indices = choose_random(list(range(total)), count)

        self.logger.info(
            f"Selected {len(indices)} random book(s)."
        )

        return indices
    
    def open_book(self, index):

        book = self.books().nth(index)

        title = book.locator("h3 a").get_attribute("title")
        price = book.locator(".price_color").inner_text().strip()

        self.logger.info(f"Opening book: {title}")

        book.locator("h3 a").click()

        self.page.wait_for_load_state("domcontentloaded")

        return {
            "title": title,
            "price": price,
        }