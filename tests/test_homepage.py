def test_homepage_loads(home_page):
    assert "Books to Scrape" in home_page.title()