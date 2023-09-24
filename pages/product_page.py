from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_btn_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN), "Button to basket is not presented"

    def should_be_alert(self):
        alert = self.browser.switch_to.alert
        assert alert.text, "Alert is empty"

    def should_be_item_name_in_item_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME), "Item name is not presented"

    def should_be_item_price_in_item_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE), "Item name is not presented"

    def should_be_item_name_in_basket_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_BASKET)
        assert item_name, "Message about the item added to basket is not appeared "

    def should_be_item_price_in_basket_message(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_BASKET)
        assert item_price, "Message about the item price in basket is not appeared"

    def should_be_equal_name_in_basket_and_in_item_page(self):
        item_name_pg = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_name_msg = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_BASKET)
        assert item_name_pg.text == item_name_msg.text, "Basket item name in message is wrong"

    def should_be_equal_price_in_basket_and_in_item_page(self):
        item_price_pg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        item_price_msg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_BASKET)
        assert item_price_msg.text == item_price_pg.text, "Basket item price in message is wrong"

    def add_item_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket.click()

    def solve_math(self):
        self.solve_quiz_and_get_code()

    def click_ok_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_NAME_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_NAME_IN_BASKET), \
            "A success message is displayed but should disappear"
