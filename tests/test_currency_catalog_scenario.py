import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_currency_catalog(browser, base_url):
    browser.get(base_url + '/en-gb/catalog/desktops/mac')

    currency_button = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a')))
    currency_button.click()
    time.sleep(2)

    currency_change = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/a')
    currency_change.click()
    time.sleep(2)

    price_sample = browser.find_element(By.XPATH, '//*[@id="product-list"]/div/div/div[2]/div/div/span[1]')
    ActionChains(browser).move_to_element(price_sample).perform()
    price_sample_first_element = price_sample.text[0]
    time.sleep(2)

    assert price_sample_first_element == '£'