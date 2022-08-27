from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Проверка существования элемента"""

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):   # except(Наименование исключения - выбрасывает Пайтон при ошибке - можно подставлять - мб можно вообще без него - делал так давно))
            return False
        return True

    def open(self):
        self.browser.get(self.url)