from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.selectors import CategorySelectors


class CategoryPage(BasePage):

    def verify_category_loaded(self, category_name):
        self.logger.info(
            f"Verifying category: {category_name}"
        )

        expect(
            self.locator(CategorySelectors.HEADER)
        ).to_have_text(category_name)

        self.logger.info("✓ Category page loaded.")