from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasketPage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_basket_page(self):
        self.browser.get(self.base_url + "/en-gb?route=checkout/cart")

    def get_product_line(self):
        return WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody/tr')))