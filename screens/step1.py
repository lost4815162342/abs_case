from screens.base import BaseScreen


class Step1Screen(BaseScreen):
    """"Экран Шага 1"""

    URL = "https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.URL)
        self._load_locators('step1.yml')
