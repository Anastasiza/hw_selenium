from page_objects.admin_login_page import AdminLoginPage


def test_auth(browser, base_url):
    adm = AdminLoginPage(browser, base_url)
    adm.get_admin_page()
    adm.login()
    assert adm.lable()


