from screens.base import BaseScreen


class Step2Screen(BaseScreen):
    """"Экран Шага 2"""

    def __init__(self, driver):
        super().__init__(driver)
        self._load_locators('step2.yml')
