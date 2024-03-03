from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class CatalogPage:
    def __init__(self,browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_catalog_page(self):
        self. browser.get(self.base_url + '/en-gb/catalog/desktops/mac')
        time.sleep(3)

    def change_currency(self):
        currency_button = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a')))
        currency_button.click()
        time.sleep(2)

        currency_change = self.browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
        currency_change.click()
        time.sleep(2)

    def get_actual_currency(self):
        price_sample = self.browser.find_element(By.XPATH,
                                                 '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]')
        ActionChains(self.browser).move_to_element(price_sample).perform()
        price_sample_first_element = price_sample.text[0]
        return price_sample_first_element