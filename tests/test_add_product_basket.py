import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_add_product_basket(browser, base_url):
    browser.get(base_url)

    add_button = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')))
    browser.execute_script("arguments[0].click();", add_button)

    time.sleep(1)

    basket_button = browser.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[4]/a')
    browser.execute_script("arguments[0].click();", basket_button)

    time.sleep(1)
    basket_table_line = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="shopping-cart"]/div/table/tbody/tr')))
    assert basket_table_line
