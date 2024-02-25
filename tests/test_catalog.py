from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_search(browser, base_url):
    browser.get(base_url + "/en-gb/catalog/")
    search = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="search"]/input')))
    assert search


def test_column(browser):
    column = browser.find_element(By.XPATH, '//*[@id="column-left"]')
    assert column


def test_contniue(browser):
    continiue = browser.find_element(By.XPATH, '//*[@id="content"]/div/a')
    assert continiue


def test_breadcrumb(browser):
    breadcrumb = browser.find_element(By.XPATH, '//*[@id="error-not-found"]/ul')
    assert breadcrumb

def test_container(browser):
    container = browser.find_element(By.XPATH, '/html/body/footer/div')
    assert container