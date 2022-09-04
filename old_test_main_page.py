from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

"""Пример использования функций"""


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)


"""Пример кейсов с использованием экземпляра класса ProductPage"""
# def test_add_to_cart(browser):
#     page = ProductPage(url="http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/", browser)   # инициализируем объект Page Object
#     page.open()                           # открываем страницу в браузере
#     page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
#     page.add_product_to_cart()            # жмем кнопку добавить в корзину
#     page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом