from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS_TEXT), "Missing message about empty basket"

    def should_not_be_active_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_STATUS_ACTIVE), "Basket is not empty"
