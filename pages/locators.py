from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRODUCT_NAME_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRODUCT_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .add_to_cart") # придумал локатор
