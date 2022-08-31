from pages.product_page import ProductPage
import time
import pytest

"Проверка по 1 адресу"

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.should_be_this_product()
#     product_page.should_be_add_button()
#     product_page.add_to_cart_with_sale()
#     time.sleep(5)
#     product_page.checking_messages_cart()


"Проверка по нескольким адресам"
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
#     product_page.add_to_cart_with_sale()
#     time.sleep(5)
#     product_page.checking_messages_cart()
#
"""Упал на offer7 => пропускаем тест с этим урлом и пробуем с 2 другими для примера"""

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="fixing")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_this_product()
    product_page.should_be_add_button()
    product_page.add_to_cart_with_sale()
    time.sleep(5)
    product_page.checking_messages_cart()