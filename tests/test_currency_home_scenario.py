from page_objects.home_page import HomePage


def test_currency_home(browser, base_url):
    hp = HomePage(browser, base_url)
    hp.get_home_page()
    hp.change_currency()
    assert hp.get_actual_currency() == '£'

