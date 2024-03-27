from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure
import logging


class HomePage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)  # Создание логгера для этого класса

    @allure.step("Open home page")
    def get_home_page(self):
        self.logger.info("Opening home page")
        self.browser.get(self.base_url)
        time.sleep(5)

    @allure.step("Change currency")
    def change_currency(self):
        self.logger.info("Changing currency")
        currency_button = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a')))
        currency_button.click()
        time.sleep(2)

        currency_change = self.browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
        currency_change.click()
        time.sleep(2)

    @allure.step("Get actual currency")
    def get_actual_currency(self):
        self.logger.info("Getting actual currency")
        price_sample = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]')
        ActionChains(self.browser).move_to_element(price_sample).perform()
        price_sample_first_element = price_sample.text[0]
        return price_sample_first_element

    @allure.step("Add product to basket")
    def add_product_to_basket(self):
        self.logger.info("Adding product to basket")
        add_button = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')))
        self.browser.execute_script("arguments[0].click();", add_button)