import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_auth(browser, base_url):
    browser.get(base_url + "/administration/")

    username_input = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="input-username"]')))
    username_input.send_keys("user")

    pass_input = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    pass_input.send_keys("bitnami")

    button = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
    button.click()
    dash_lable = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/div/h1")))
    assert dash_lable
