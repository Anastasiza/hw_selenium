from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import allure

class BasketPage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)  # Создание логгера для этого класса

    @allure.step("Open basket page")
    def get_basket_page(self):
        self.logger.info("Opening basket page")
        self.browser.get(self.base_url + "/en-gb?route=checkout/cart")

    @allure.step("Get product line")
    def get_product_line(self):
        self.logger.info("Getting product line")
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody/tr')))