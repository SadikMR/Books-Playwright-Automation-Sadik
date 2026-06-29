import pytest

from pages.home_page import HomePage


@pytest.mark.regression
def test_broken_links(page):

    home = HomePage(page)

    home.open()

    links = home.get_all_links()

    home.logger.info("Checking hyperlinks...")

    broken_links = []

    for url in links:

        response = page.request.get(url)

        home.logger.info(
            f"{response.status} - {url}"
        )

        if not response.ok:
            broken_links.append(
                f"{url} ({response.status})"
            )

    assert not broken_links, (
        "Broken links found:\n"
        + "\n".join(broken_links)
    )

    home.logger.info(
        f"✓ Verified {len(links)} hyperlink(s). No broken links found."
    )