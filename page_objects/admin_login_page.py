import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class AdminLoginPage:

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_admin_page(self):
        self. browser.get(self.base_url + '/administration/')


    def login(self):
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

    def lable(self):
        dash_lable = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/h1")))
        return dash_lable