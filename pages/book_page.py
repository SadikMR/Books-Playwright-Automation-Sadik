from playwright.sync_api import expect

from pages.base_page import BasePage


class BookPage(BasePage):

    TITLE = ".product_main h1"

    PRICE = ".price_color"

    AVAILABILITY = ".availability"

    DESCRIPTION = "#product_description"

    IMAGE = ".item.active img"

    def verify_page_loaded(self):

        expect(
            self.page.locator(self.TITLE)
        ).to_be_visible()

    def get_title(self):
        return self.page.locator(self.TITLE).inner_text()

    def get_price(self):
        return self.page.locator(self.PRICE).inner_text()

    def has_description(self):
        return self.page.locator(self.DESCRIPTION).count() > 0

    def image_visible(self):
        return self.page.locator(self.IMAGE).is_visible()

    def availability_text(self):
        return self.page.locator(self.AVAILABILITY).inner_text()