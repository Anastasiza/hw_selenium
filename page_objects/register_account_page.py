from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class RegisterPage:
    def __init__(self,browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def get_register_page(self):
        self.browser.get(self.base_url + '/en-gb?route=account/register')

    def registrate_new_user(self):
        input_first_name = self.browser.find_element(By.XPATH, '//*[@id="input-firstname"]')
        input_first_name.send_keys('Иван')
        time.sleep(1)

        input_last_name = self.browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
        input_last_name.send_keys('Иванов')
        time.sleep(1)

        input_email = self.browser.find_element(By.XPATH, '//*[@id="input-email"]')
        input_email.send_keys('ivanov@mail.ru')
        time.sleep(1)

        input_password = self.browser.find_element(By.XPATH, '//*[@id="input-password"]')
        input_password.send_keys('OpirOp86')
        time.sleep(3)

        click_policy = self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input')
        self.browser.execute_script("arguments[0].click();", click_policy)
        time.sleep(3)

        click_continue = self.browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button')
        self.browser.execute_script("arguments[0].click();", click_continue)
        time.sleep(1)

        message = self.browser.find_element(By.XPATH, '//*[@id="content"]/h1').text
        return message

