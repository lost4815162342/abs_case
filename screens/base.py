import allure
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import screens


class BaseScreen:
    """Базовый Экран"""

    def __init__(self, driver):
        self.driver = driver
        self.locators = {}

    def _find_element(self, locator, time):
        """Реализация поиска элемента через Selenium"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def _find_elements(self, locator, time):
        """Реализация поиска элементов через Selenium"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def _load_locators(self, file_name):
        """Загрузка справочника элементов из yaml"""
        with open('locators/{}'.format(file_name)) as f:
            self.locators = {k: (list(v.keys())[0], list(v.values())[0],) for k, v in yaml.safe_load(f).items()}

    def _scroll_to_by_name(self, element_name):
        """Реализация скроллла по имени элемента через Selenium"""
        element = self.find_element(element_name)
        self._scroll_to_by_element(element)
        return self

    def _scroll_to_by_element(self, element):
        """Реализация скролла по элементу через Selenium"""
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        return self

    def find_element(self, element_name, time=10, scroll=True):
        with allure.step(f'Поиск элемента "{element_name}"'):
            locator = self.locators.get(element_name)
            element = self._find_element(locator, time=time)
            if scroll:
                self._scroll_to_by_element(element)
            return element

    def _click(self, element):
        """Реализация клика через Selenium"""
        ActionChains(self.driver).click(element).perform()

    def click(self, element_name):
        with allure.step(f'Клик по "{element_name}"'):
            element = self.find_element(element_name)
            self._click(element)
        return self

    def screen(self, screen_name):
        """Загрузка экрана по названию из каталога экранов"""
        ScreenClass = screens.catalog.get(screen_name)
        return ScreenClass(self.driver)

    @allure.title('Заполнение данных формы')
    def input_data(self, data):
        for element_name, value in data.items():
            self.input(element_name, value)
        return self

    def input(self, element_name, value, with_click=True):
        with allure.step(f'Заполнение поля "{element_name}" значением "{value}"'):
            element = self.find_element(element_name)
            if with_click:
                self._click(element)
            element.send_keys(value)
        return self
