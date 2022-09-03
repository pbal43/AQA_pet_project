from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

    def should_be_no_items_in_cart(self):
        assert self.is_not_element_present(*BasketLocators.CART_ITEM), "The cart isn't empty"

    def should_be_message_about_empty_cart(self):
        assert self.is_element_present(*BasketLocators.EMPTY_CART_MESSAGE), "There isn't the massage about empty cart"