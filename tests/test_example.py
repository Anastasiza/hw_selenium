import time

def test_check_title(browser):
    assert "Your Store" in browser.title
    time.sleep(3)
