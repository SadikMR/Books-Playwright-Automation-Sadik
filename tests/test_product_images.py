import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_product_images(page):

    home = HomePage(page)

    home.open()

    max_pages = 5

    current_page = 1

    while current_page <= max_pages:

        home.logger.info(
            f"Validating images on page {current_page}..."
        )

        home.verify_product_images()

        if current_page == max_pages:
            break

        if not home.has_next_page():
            break

        home.open_next_page()

        current_page += 1

    home.logger.info(
        "✓ Product image validation completed."
    )