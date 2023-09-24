from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.Cart_page import CartPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page_login = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()
        page_login.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page_cart = CartPage(browser, link)
        page.open()
        page_cart.go_to_cart_page()
        page_cart.should_not_be_active_cart()
        page_cart.should_be_empty_cart_message()
