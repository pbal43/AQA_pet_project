from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    """В метод ниже можно добавить book_id из отдельного файла с наименованием и ценой для сравнения с парсируемыми"""
    def should_be_this_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.parsed_product_name = product_name.text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.parsed_price = price.text

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "There isn't add button"

    def add_to_cart(self):
        add_cart_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_cart_button.click()
        self.solve_quiz_and_get_code()

    def checking_messages_cart(self):
        name_in_message_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART_MESSAGE)
        name_in_message_cart_parsed = name_in_message_cart.text
        price_in_message_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART_MESSAGE)
        price_in_message_cart_parsed = price_in_message_cart.text
        # print(name_in_message_cart_parsed, self.parsed_product_name, price_in_message_cart_parsed, self.parsed_price) - совпадает, даже с валютой (можно сравнивать чисто интеджер)
        assert name_in_message_cart_parsed == self.parsed_product_name, "Name isn't correct"
        print('Book: "' + name_in_message_cart_parsed + '" added to cart with correct name')
        assert price_in_message_cart_parsed == self.parsed_price, "Price isn't correct"
        print('Book price is correct and = ', price_in_message_cart_parsed)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
