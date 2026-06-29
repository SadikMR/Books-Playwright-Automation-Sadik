class HomeSelectors:
    # CSS Selector
    BOOKS = "article.product_pod"

    # XPath Selector
    CATEGORY_LINKS = "//div[@class='side_categories']//ul/li/ul/li/a"

    # CSS Selector
    BOOK_LINKS = "article.product_pod h3 a"

    # CSS Selector
    BOOKS_SECTION = "ol.row"

    # CSS Selector
    PAGE_HEADER = ".page-header"

    # CSS Selector
    HEADINGS = "h1, h2, h3, h4, h5, h6"

    # Text Selector
    LOGO_TEXT = "text=Books to Scrape"


class CategorySelectors:
    # CSS Selector
    BOOKS = "article.product_pod"

    # CSS Selector
    NEXT = "li.next a"

    # XPath Selector
    HEADER = "//div[contains(@class,'page-header')]/h1"


class BookSelectors:
    TITLE = ".product_main h1"
    PRICE = ".product_main .price_color"
    AVAILABILITY = ".product_main .availability"
    IMAGE = ".item.active img"
    DESCRIPTION = "#product_description + p"