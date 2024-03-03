from page_objects.home_page import HomePage
from page_objects.basket_page import BasketPage


def test_add_product_basket(browser, base_url):
    hp = HomePage(browser, base_url)
    hp.get_home_page()
    hp.add_product_to_basket()
    pb = BasketPage(browser, base_url)
    pb.get_basket_page()
    assert pb.get_product_line()
