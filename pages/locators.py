from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BTN = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM_LINK = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM_LINK = (By.XPATH, "//form[@id='register_form']")
    REGISTER_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTER_PASSWORD_1 = (By.XPATH, "//input[@name='registration-password1']")
    REGISTER_PASSWORD_2 = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BTN_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ITEM_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']//h1")
    ITEM_NAME_IN_BASKET = (By.XPATH, "(//div[@class='alertinner ']//strong)[1]")
    ITEM_PRICE = (By.XPATH, "//p[@class='price_color']")
    ITEM_PRICE_IN_BASKET = (By.XPATH, "(//div[@class='alertinner ']//strong)[3]")


class BasketPageLocators():
    BASKET_STATUS_TEXT = (By.XPATH, "//div[@id='content_inner']//p")
    BASKET_STATUS_ACTIVE = (By.XPATH, "//div[@id='content_inner']//h2[@class='col-sm-6 h3']")
