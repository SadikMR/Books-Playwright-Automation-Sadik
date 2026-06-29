import pytest

from playwright.sync_api import expect

from pages.home_page import HomePage

from pages.book_page import BookPage


@pytest.mark.smoke
def test_book_details(page):

    home = HomePage(page)

    home.open()

    home.open_first_book()

    book = BookPage(page)

    book.verify_loaded()

    expect(page.locator(".product_main h1")).not_to_be_empty()

    expect(page.locator(".price_color")).to_contain_text("£")

    expect(page.locator(".item.active img")).to_have_attribute(
        "src",
        lambda value: value.endswith(".jpg"),
    )