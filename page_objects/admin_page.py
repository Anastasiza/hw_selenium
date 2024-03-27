from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging
import allure

class AdminPage:
    def __init__(self, browser, base_url, token):
        self.product_name = None
        self.browser = browser
        self.base_url = base_url
        self.token = token
        self.logger = logging.getLogger(__name__)  # Создание логгера для этого класса

    @allure.step("Open admin page")
    def get_admin_page(self):
        self.logger.info("Opening admin page")
        self.browser.get(self.base_url + '/administration/index.php?route=common/dashboard&user_token=' + self.token)

    @allure.step("Add product page")
    def add_product_page(self, product_name):
        self.logger.info("Adding product page")
        self.product_name = product_name
        self.browser.get(self.base_url + '/administration/index.php?route=catalog/product.form&user_token=' + self.token)
        input_product_name = self.browser.find_element(By.XPATH, '//*[@id="input-name-1"]')
        input_product_name.send_keys(product_name)
        time.sleep(1)

        input_meta_tag = self.browser.find_element(By.XPATH, '//*[@id="input-meta-title-1"]')
        input_meta_tag.send_keys('Tag')
        time.sleep(1)

        clic_data = self.browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[2]/a')
        clic_data.click()
        time.sleep(1)

        input_model = self.browser.find_element(By.XPATH, '//*[@id="input-model"]')
        input_model.send_keys('Model')
        time.sleep(1)

        clic_seo = self.browser.find_element(By.XPATH, '//*[@id="form-product"]/ul/li[11]/a')
        clic_seo.click()
        time.sleep(1)

        input_keyword = self.browser.find_element(By.XPATH, '//*[@id="input-keyword-0-1"]')
        input_keyword.send_keys('TEST')
        time.sleep(1)

        clic_save = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
        clic_save.click()
        time.sleep(1)
        self.browser.get(self.base_url + '/administration/index.php?route=catalog/product&user_token=' + self.token)

        input_filter = self.browser.find_element(By.XPATH, '//*[@id="input-name"]')
        input_filter.send_keys(product_name)
        time.sleep(1)

        click_filter = self.browser.find_element(By.XPATH, '//*[@id="button-filter"]')
        self.browser.execute_script("arguments[0].click();", click_filter)
        time.sleep(1)

        saved_product_name = self.browser.find_element(By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr/td[3]").text
        return saved_product_name

    @allure.step("Delete product")
    def delete_product(self):
        self.logger.info("Deleting product")
        self.browser.get(self.base_url + '/administration/index.php?route=catalog/product&user_token=' + self.token)
        input_filter = self.browser.find_element(By.XPATH, '//*[@id="input-name"]')
        input_filter.send_keys(self.product_name)
        time.sleep(1)

        click_filter = self.browser.find_element(By.XPATH, '//*[@id="button-filter"]')
        self.browser.execute_script("arguments[0].click();", click_filter)
        time.sleep(1)

        click_checkbox = self.browser.find_element(By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[1]/input')
        click_checkbox.click()
        time.sleep(1)

        click_delete = self.browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
        click_delete.click()
        self.browser.switch_to.alert.accept()
        time.sleep(1)
        no_result = self.browser.find_element(By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr/td").text
        return no_result







