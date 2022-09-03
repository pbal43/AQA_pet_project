from .base_page import BasePage
# from .locators import MainPageLocators

"""Закомменили, так как вынесли методы в base_page"""

# class MainPage(BasePage):

    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
    #
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click()
    #     """Допустим, добавили alert, можно записать обработку здесь, а не в каждом тесте"""
    #     alert = self.browser.switch_to.alert
    #     alert.accept()


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

"""Конструктор выше с ключевым словом super на самом деле только вызывает конструктор класса предка
и передает ему все те аргументы, которые мы передали в конструктор MainPage."""