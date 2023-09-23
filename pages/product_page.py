from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_btn_to_cart(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN), "Button to cart is not presented"

    def should_be_alert(self):
        alert = self.browser.switch_to.alert
        assert alert.text, "Alert is empty"

    def should_be_item_name_in_item_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME), "Item name is not presented"

    def should_be_item_price_in_item_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE), "Item name is not presented"

    def should_be_item_name_in_cart_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_CART)
        assert item_name, "Message about the item added to cart is not appeared "

    def should_be_item_price_in_cart_message(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_CART)
        assert item_price, "Message about the item price in cart is not appeared"

    def should_be_equal_name_in_cart_and_in_item_page(self):
        item_name_pg = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name_msg = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_CART)
        assert item_name_pg.text == item_name_msg.text, "Cart item name in message is wrong"

    def should_be_equal_price_in_cart_and_in_item_page(self):
        item_price_pg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_price_msg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_CART)
        assert item_price_msg.text == item_price_pg.text, "Cart item price in message is wrong"

    def add_item_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart.click()

    def solve_math(self):
        self.solve_quiz_and_get_code()

    def click_ok_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_NAME_IN_CART), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_NAME_IN_CART), \
            "A success message is displayed but should disappear"