from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_RE_PASS_FILED = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"')


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    PRODUCT_NAME_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRODUCT_PRICE_IN_CART_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info p:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    CART_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p[text()]')

