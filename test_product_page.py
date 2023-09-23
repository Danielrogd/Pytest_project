from .pages.product_page import ProductPage
from .pages.Cart_page import CartPage
import pytest
import time


# @pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# def test_guest_can_add_product_to_basket(browser, offer):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_btn_to_cart()
#     page.add_item_to_cart()
#     page.should_be_alert()
#     page.solve_math()
#     time.sleep(2)
#     page.should_be_item_name_in_item_page()
#     page.should_be_item_price_in_item_page()
#     page.should_be_item_name_in_cart_message()
#     page.should_be_item_price_in_cart_message()
#     page.should_be_equal_name_in_cart_and_in_item_page()
#     page.should_be_equal_price_in_cart_and_in_item_page()

# @pytest.mark.xfail(reason="fail")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_btn_to_cart()
#     page.add_item_to_cart()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail(reason="fail")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_btn_to_cart()
#     page.add_item_to_cart()
#     page.should_not_be_disappeared()


# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()



def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page_cart = CartPage(browser, link)
    page.open()
    page_cart.go_to_cart_page()
    page_cart.should_not_be_active_cart()
    page_cart.should_be_empty_cart_message()
