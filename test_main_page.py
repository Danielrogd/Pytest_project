from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_presence_of_btn_that_add_item_to_cart(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
