import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import catalog


class BaseScreen:


    def __init__(self, driver):
        self.driver = driver
        self.locators = {}

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def load_locators(self, file_name):
        with open('locators/{}'.format(file_name)) as f:
            self.locators = yaml.safe_load(f)
        t = 1


    def screen(self, screen_name):
        ScreenClass = catalog.get(screen_name)
        return ScreenClass(self.driver)