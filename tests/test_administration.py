from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_header(browser, base_url):
    browser.get(base_url + "/administration/")
    header = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div/div[1]')))
    assert header

def test_username(browser):
    username = browser.find_element(By.XPATH, '//*[@id="input-username"]')
    assert username

def test_password(browser):
    password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    assert password

def test_button(browser):
    button = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
    assert button

def test_lable_username(browser):
    lable = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/label')
    assert lable

def test_lable_password(browser):
    lable = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[2]/label')
    assert lable
