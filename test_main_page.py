from pages.main_page import *
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

"""Объединяем тесты в класс и добавляем self в тесты - поле чего можно запустить командой -m login_guest"""

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        """Для перехода по страницам"""
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

"""Переход в корзину и проверки"""
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    basket = BasketPage(browser, link)
    basket.should_be_no_items_in_cart()
    basket.should_be_message_about_empty_cart()
