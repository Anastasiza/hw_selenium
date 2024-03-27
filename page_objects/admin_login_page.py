import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class AdminLoginPage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)  # Создание логгера для этого класса

    @allure.step("Open admin page")
    def get_admin_page(self):
        self.logger.info("Opening admin page")
        self.browser.get(self.base_url + '/administration/')

    @allure.step("Login as admin")
    def login(self):
        self.logger.info("Logging in as admin")
        username_input = WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="input-username"]')))
        username_input.send_keys("user")

        pass_input = self.browser.find_element(By.XPATH, '//*[@id="input-password"]')
        pass_input.send_keys("bitnami")

        button = self.browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
        button.click()
        time.sleep(2)
        token = self.browser.current_url[-32::]
        return token

    @allure.step("Get dashboard label")
    def lable(self):
        self.logger.info("Getting dashboard label")
        dash_lable = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/h1")))
        return dash_lable