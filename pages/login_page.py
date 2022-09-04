from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There isn't login in page URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_input.send_keys(email)
        pass_input_1 = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD)
        pass_input_1.send_keys(password)
        pass_input_2 = self.browser.find_element(*LoginPageLocators.REG_RE_PASS_FILED)
        pass_input_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        register_button.click()

