from pages.base_page import BasePage

from utils.selectors import CategorySelectors


class CategoryPage(BasePage):

    def verify_loaded(self):

        self.wait_visible(CategorySelectors.HEADER)

    def books(self):

        return self.locator(CategorySelectors.BOOKS)

    def next_button(self):

        return self.locator(CategorySelectors.NEXT)

    def has_next_page(self):

        return self.next_button().count() > 0

    def next_page(self):

        self.next_button().click()