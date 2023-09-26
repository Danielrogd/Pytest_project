from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.Basket_page import BasketPage
import pytest
import time
import random


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_to_basket()
    page.add_item_to_basket()
    page.should_be_alert()
    page.solve_math()
    time.sleep(2)
    page.should_be_item_name_in_item_page()
    page.should_be_item_price_in_item_page()
    page.should_be_item_name_in_basket_message()
    page.should_be_item_price_in_basket_message()
    page.should_be_equal_name_in_basket_and_in_item_page()
    page.should_be_equal_price_in_basket_and_in_item_page()


@pytest.mark.xfail(reason="fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_to_basket()
    page.add_item_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="fail")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_btn_to_basket()
    page.add_item_to_basket()
    page.should_not_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page_basket = BasketPage(browser, link)
    page.open()
    page_basket.go_to_basket_page()
    page_basket.should_not_be_active_basket()
    page_basket.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_btn_to_basket()
        page.add_item_to_basket()
        page.should_be_alert()
        page.solve_math()
        time.sleep(2)
        page.should_be_item_name_in_item_page()
        page.should_be_item_price_in_item_page()
        page.should_be_item_name_in_basket_message()
        page.should_be_item_price_in_basket_message()
        page.should_be_equal_name_in_basket_and_in_item_page()
        page.should_be_equal_price_in_basket_and_in_item_page()
