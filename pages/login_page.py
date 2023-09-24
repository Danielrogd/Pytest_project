from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        input_password_1.send_keys(password)
        input_password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        input_password_2.send_keys(password)
        btn_submit = self.browser.find_element(*LoginPageLocators.REGISTER_BTN_SUBMIT)
        btn_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Login is not presented in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Register form link is not presented"
