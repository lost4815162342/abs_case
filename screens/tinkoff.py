import allure

from screens.base import BaseScreen


class TinkoffScreen(BaseScreen):
    """"Экран Кабинета оплаты Тинькофф"""

    DOMAIN = 'securepayments.tinkoff.ru'
    REQUIRED_ELEMENTS = ['Заголовок Быстрая Оплата', 'Заголовок Оплата картой']

    def __init__(self, driver):
        super().__init__(driver)
        self._load_locators('tinkoff.yml')

    @allure.title('Проверка что экран кабинета оплаты Тинькофф загружен')
    def check_screen(self):
        with allure.step('Проверка обязательных элементов'):
            for element_name in self.REQUIRED_ELEMENTS:
                with allure.step(f'Проверка элемента {element_name}'):
                    assert self.find_element(element_name, time=30), f'Не найден элемент "{element_name}"'
        return self

    @allure.title('Проверка перехода на сайт Тинькофф')
    def check_domain(self):
        assert self.DOMAIN in self.driver.current_url, f'Не произошел переход на домен {self.DOMAIN}, текущий адрес {self.driver.current_url}'
        return self
