def test_default_pagination_option(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_default_pagination_option()


def test_filter_by_size(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.select_size()
    eco_friendly_page.clear_filter()


def test_filter_by_price(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.filter_price()
