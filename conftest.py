import pytest
from playwright.sync_api import Playwright


BASE_URL = "https://books.toscrape.com/"


@pytest.fixture(scope="function")
def home_page(page):
    page.goto(BASE_URL)
    return page