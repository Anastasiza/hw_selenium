from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_first_name(browser, base_url):
    browser.get(base_url + "/en-gb?route=account/register")
    first_name = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="input-firstname"]')))
    assert first_name


def test_last_name(browser):
    last_name = browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
    assert last_name


def test_mail(browser):
    mail = browser.find_element(By.XPATH, '//*[@id="input-email"]')
    assert mail


def test_password(browser):
    password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    assert password


def test_continue_input(browser):
    cont = browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button')
    assert cont
