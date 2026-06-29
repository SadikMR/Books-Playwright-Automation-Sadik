from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.selectors import BookSelectors


class BookPage(BasePage):

    def title(self):
        return self.get_text(BookSelectors.TITLE)

    def price(self):
        return self.get_text(BookSelectors.PRICE)

    def availability(self):
        return self.get_text(BookSelectors.AVAILABILITY)

    def description(self):
        return self.get_text(BookSelectors.DESCRIPTION)

    def verify_book_loaded(self, expected_title):
        self.logger.info(f"Verifying book details page: {expected_title}")

        expect(
            self.locator(BookSelectors.TITLE)
        ).to_have_text(expected_title)

        self.logger.info(
            "✓ Details page loaded and H1 title matches the selected book."
        )

    def verify_book_information(self):
        self.logger.info("Verifying book information...")

        expect(
            self.locator(BookSelectors.PRICE)
        ).to_be_visible()

        expect(
            self.locator(BookSelectors.AVAILABILITY)
        ).to_be_visible()

        expect(
            self.locator(BookSelectors.IMAGE)
        ).to_be_visible()

        expect(
            self.locator(BookSelectors.DESCRIPTION)
        ).to_be_visible()

        self.logger.info(
            "✓ Price, availability, image, and description are visible."
        )

    def verify_data_consistency(self, homepage_data):
        self.logger.info(
            "Comparing homepage and details page data..."
        )

        assert homepage_data["title"] == self.title()
        assert homepage_data["price"] == self.price()

        self.logger.info(
            "✓ Homepage and details page data match."
        )

    def verify_image_attributes(self):
        self.logger.info("Verifying image attributes...")

        image = self.locator(BookSelectors.IMAGE)

        expect(image).to_be_visible()

        src = image.get_attribute("src")
        alt = image.get_attribute("alt")
        class_name = image.get_attribute("class")

        assert src
        assert alt
        assert class_name

        self.logger.info(
            "✓ Image contains valid src, alt, and class attributes."
        )