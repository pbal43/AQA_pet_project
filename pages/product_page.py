from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_this_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        parsed_product_name = product_name.text
        assert parsed_product_name == "The shellcoder's handbook", "It's not an expected book"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There isn't add button"

    def add_to_cart_with_sale(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_cart_button.click()
        self.solve_quiz_and_get_code()

    # def checking_cart():
    #     name_in_cart =
    #
    #     assert product_name = name_in_cart