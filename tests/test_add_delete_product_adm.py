from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_page import AdminPage

admin_page = None

def test_add_product(browser, base_url):
    global admin_page
    product_name = "AApple"

    adm_login = AdminLoginPage(browser, base_url)
    adm_login.get_admin_page()
    token = adm_login.login()

    admin_page = AdminPage(browser, base_url, token)
    admin_page.get_admin_page()
    actual_saves_product_name = admin_page.add_product_page(product_name)
    assert actual_saves_product_name == product_name+"\nEnabled"

def test_delet_product(browser, base_url):
    no_result = admin_page.delete_product()
    assert no_result == "No results!"

