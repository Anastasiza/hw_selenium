from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_product_image(browser, base_url):
    browser.get(base_url + "/en-gb/product/macbook")
    product = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/a/img')))
    assert product

def test_title(browser):
    title = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')
    assert title

def test_prise(browser):
    prise = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2/span')
    assert prise

def test_input_qantiti(browser):
    qantiti = browser.find_element(By.XPATH, '//*[@id="input-quantity"]')
    assert qantiti

def test_button_card(browser):
    button = browser.find_element(By.XPATH, '//*[@id="button-cart"]')
    assert button

