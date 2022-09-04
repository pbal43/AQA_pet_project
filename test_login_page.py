from .pages.login_page import *


def test_guest_on_the_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
