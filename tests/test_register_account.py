from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.register_account_page import RegisterPage


def test_register_account(browser, base_url):
    register = RegisterPage(browser, base_url)
    register.get_register_page()
    message = register.registrate_new_user()
    assert message == "Your Account Has Been Created!"

