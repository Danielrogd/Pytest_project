from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.CART_STATUS_TEXT), "Missing message about empty cart"

    def should_not_be_active_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_STATUS_ACTIVE), "Cart is not empty"
