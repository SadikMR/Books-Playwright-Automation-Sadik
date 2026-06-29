from pathlib import Path

from playwright.sync_api import Page, Locator, expect

from utils.logger import get_logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)


    def visit(self, url: str):
        self.logger.info(f"Opening: {url}")
        self.page.goto(url)

    def reload(self):
        self.logger.info("Reloading page")
        self.page.reload()

    def go_back(self):
        self.logger.info("Going back")
        self.page.go_back()


    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str):
        self.logger.info(f"Clicking: {selector}")
        self.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.logger.info(f"Filling: {selector}")
        self.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.locator(selector).inner_text().strip()

    def get_attribute(self, selector: str, attribute: str):
        return self.locator(selector).get_attribute(attribute)

    def count(self, selector: str) -> int:
        return self.locator(selector).count()


    def expect_visible(self, selector: str):
        expect(self.locator(selector)).to_be_visible()

    def expect_hidden(self, selector: str):
        expect(self.locator(selector)).to_be_hidden()

    def expect_text(self, selector: str, text: str):
        expect(self.locator(selector)).to_have_text(text)

    def expect_contains_text(self, selector: str, text: str):
        expect(self.locator(selector)).to_contain_text(text)

    def expect_count(self, selector: str, count: int):
        expect(self.locator(selector)).to_have_count(count)

    def expect_attribute(self, selector: str, attribute: str, value):
        expect(self.locator(selector)).to_have_attribute(attribute, value)


    def screenshot(self, name: str):
        Path("screenshots").mkdir(exist_ok=True)
        self.page.screenshot(path=f"screenshots/{name}.png", full_page=True)

    @property
    def current_url(self):
        return self.page.url

    @property
    def page_title(self):
        return self.page.title()