from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.constants import BASE_URL
from utils.selectors import HomeSelectors
from utils.helper import choose_random

from urllib.parse import urljoin

class HomePage(BasePage):

    def open(self):
        self.visit(BASE_URL)

    def verify_homepage(self):
        self.logger.info("Verifying homepage URL...")
        expect(self.page).to_have_url(BASE_URL)
        self.logger.info("✓ Homepage URL is correct.")

        self.logger.info("Verifying homepage title...")
        expected_title = "All products | Books to Scrape - Sandbox"
        expect(self.page).to_have_title(expected_title)
        self.logger.info("✓ Homepage title is correct.")

    def verify_homepage_loaded(self):
        self.logger.info("Verifying homepage is loaded...")
        self.expect_visible(HomeSelectors.LOGO_TEXT)
        self.logger.info("✓ Homepage loaded successfully.")

    def categories(self):
        return self.locator(HomeSelectors.CATEGORY_LINKS)

    def books(self):
        return self.locator(HomeSelectors.BOOK_LINKS)

    def headings(self):
        return self.locator(HomeSelectors.HEADINGS)

    def books_section(self):
        return self.locator(HomeSelectors.BOOKS_SECTION)

    def category_count(self):
        return self.count(HomeSelectors.CATEGORY_LINKS)

    def book_count(self):
        return self.count(HomeSelectors.BOOKS)

    def verify_all_headings(self):
        self.logger.info("Verifying all visible headings...")

        headings = self.headings().all()

        for heading in headings:
            expect(heading).to_be_visible()
            assert heading.inner_text().strip()

        self.logger.info(
            f"✓ Verified {len(headings)} visible heading(s) with non-empty text."
        )

    def verify_books_section(self):
        self.logger.info("Verifying books section...")

        expect(self.books_section()).to_be_visible()

        total_books = self.book_count()
        assert total_books > 0

        self.logger.info(
            f"✓ Books section is visible and contains {total_books} book(s)."
        )

    def open_first_book(self):
        self.logger.info("Opening first book...")
        self.books().first.click()

    def open_category(self, category):
        category_name = category.inner_text().strip()

        self.logger.info(f"Opening category: {category_name}")

        category.click()

        return category_name

    def random_categories(self, count=5):
        self.logger.info("Selecting random categories...")

        categories = self.categories().all()

        selected = choose_random(categories, count)

        self.logger.info(
            f"Selected {len(selected)} random categor(ies)."
        )

        return selected
    
    def links(self):
        return self.locator("a")


    def get_all_links(self):
        self.logger.info("Collecting hyperlinks...")

        urls = set()

        for link in self.links().all():
            href = link.get_attribute("href")

            if not href:
                continue

            if href.startswith("#"):
                continue

            if href.startswith("javascript:"):
                continue

            urls.add(urljoin(self.page.url, href))

        self.logger.info(
            f"✓ Collected {len(urls)} unique hyperlink(s)."
        )

        return sorted(urls)