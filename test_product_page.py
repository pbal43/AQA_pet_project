import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import time
import random
# Можно добавить имена - для генерации email и потом заморозить

"Проверка по 1 адресу"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_this_product()
    product_page.should_be_add_button()
    product_page.add_to_cart()
    product_page.checking_messages_cart()
#
#
# "Проверка по нескольким адресам"
#
#
# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
#
#
# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_this_product()
#     product_page.should_be_add_button()
#     product_page.add_to_cart()
#     time.sleep(5)
#     product_page.checking_messages_cart()

# """Упал на offer7 => пропускаем тест с этим урлом и пробуем с 2 другими для примера"""
#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="fixing")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_this_product()
#     product_page.should_be_add_button()
#     product_page.add_to_cart()
#     # time.sleep(5)
#     product_page.checking_messages_cart()

"""Проверка успешных сообщений после добавления товара в корзину"""

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

"""Переход в корзину и проверки"""
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    basket = BasketPage(browser, link)
    basket.should_be_no_items_in_cart()
    basket.should_be_message_about_empty_cart()


"""Группировка тестов и setup (для зарегистрированного пользователя) - но setup юзать - плохая практика"""


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "qwertyy"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, password)
        basket_page = BasketPage(browser, link)
        basket_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_this_product()
        product_page.should_be_add_button()
        product_page.add_to_cart()
        product_page.checking_messages_cart()

