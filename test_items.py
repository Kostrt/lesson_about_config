import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_cart_button(browser):
    try:
        browser.get(link)
        time.sleep(5)
        button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    
    finally:
        assert button, "No ADD-button on the link"