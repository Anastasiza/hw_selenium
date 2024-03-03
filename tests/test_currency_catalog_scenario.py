from page_objects.catalog_page import CatalogPage


def test_currency_catalog(browser, base_url):
    cp = CatalogPage(browser, base_url)
    cp.get_catalog_page()
    cp.change_currency()
    assert cp.get_actual_currency() == '£'
