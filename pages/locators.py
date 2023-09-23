from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM_LINK = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM_LINK = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ITEM_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    ITEM_NAME_IN_CART = (By.XPATH, "(//div[@class='alertinner ']//strong)[1]")
    ITEM_PRICE = (By.XPATH, "//p[@class='price_color']")
    ITEM_PRICE_IN_CART = (By.XPATH, "(//div[@class='alertinner ']//strong)[3]")
    # (//div[@class='alertinner ']//strong)[2] - qualifies for the Deferred benefit offer offer
