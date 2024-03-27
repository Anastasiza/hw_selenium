import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def test_logo(browser, base_url):
    browser.get(base_url)
    assert WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.ID, 'logo')))


def test_banner(browser):
    banner = browser.find_element(By.XPATH, '//*[@id="carousel-banner-0"]')
    assert banner
    time.sleep(2)

def test_cart_button(browser):
    cart = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    assert cart
    time.sleep(2)

def test_featured(browser):
    featured = browser.find_element(By.XPATH, '//*[@id="content"]/h3')
    assert featured
    time.sleep(2)

def test_carusel_banner(browser):
    carusel = browser.find_element(By.XPATH, '//*[@id="carousel-banner-1"]')
    assert carusel