import allure
import pytest


@allure.epic('Тестовое задание')
class TestClass:
    PERSONAL_DATA_VALID = {
        "Поле ввода - ФИО страхователя": "Тестов Тест Тестович",
        "Поле ввода - Дата рождения страхователя": "11.11.1991",
        "Поле ввода - Серия/номер паспорта страхователя": "1212-212121",
        "Поле ввода - Дата выдачи": "12.12.2011",
        "Поле ввода - Адрес регистрации": "г.Тестославль, ул Тестовая д. 404",
        "Поле ввода - Телефон": "4041230000",
        "Поле ввода - Email": "delme@test.test",
    }

    PERSONAL_DATA_INVALID = {
        "Поле ввода - ФИО страхователя": "Тестов Тест Тестович",
        "Поле ввода - Дата рождения страхователя": "01.03.2006",
        "Поле ввода - Серия/номер паспорта страхователя": "1212-212121",
        "Поле ввода - Дата выдачи": "12.12.2011",
        "Поле ввода - Адрес регистрации": "г.Тестославль, ул Тестовая д. 404",
        "Поле ввода - Телефон": "0000000000",
        "Поле ввода - Email": "delme@test.test",
    }

    @allure.title('Проверка успешного перехода по всем шагам')
    def test_success_all_steps(self, first_screen):
        with allure.step('Экран: Шаг 1. Расчет'):
            step1 = first_screen.screen('Шаг 1. Расчет') \
                .click('Чекбокс - Подтверждение отсутствия Covid19 у сожителя') \
                .click('Чекбокс - Согласие на обработку персданных') \
                .click('Кнопка Продолжить')

        with allure.step('Экран: Шаг 2.  Ввод данных'):
            step2 = step1.screen('Шаг 2.  Ввод данных') \
                .input_data(self.PERSONAL_DATA_VALID) \
                .click("Кнопка Перейти к оплате")

        with allure.step('Экран: Кабинет оплаты'):
            step2.screen("Кабинет оплаты") \
                .check_screen() \
                .check_domain()

    @allure.title('Проверка отсутствия перехода(негативная проверка)')
    def test_error_switch_to_pay(self, first_screen):
        with allure.step('Экран: Шаг 1. Расчет'):
            step1 = first_screen.screen('Шаг 1. Расчет') \
                .click('Чекбокс - Подтверждение отсутствия Covid19 у сожителя') \
                .click('Чекбокс - Согласие на обработку персданных') \
                .click('Кнопка Продолжить')

        with allure.step('Экран: Шаг 2.  Ввод данных'):
            step2 = step1.screen('Шаг 2.  Ввод данных') \
                .input_data(self.PERSONAL_DATA_INVALID) \
                .click("Кнопка Перейти к оплате")

        with allure.step('Экран: Кабинет оплаты. Негативные проверки'):
            tinkoff = step2.screen("Кабинет оплаты")
            with pytest.raises(Exception):
                tinkoff.check_screen()
            with pytest.raises(Exception):
                tinkoff.check_domain()

    @allure.title('Тест, который всегда валится в ошибку')
    def test_error_with_screenshot(self, first_screen):
        with allure.step('Экран: Шаг 1. Расчет'):
            step1 = first_screen.screen('Шаг 1. Расчет') \
                .click('Чекбокс - Подтверждение отсутствия Covid19 у сожителя') \
                .click('Чекбокс - Согласие на обработку персданных') \
                .click('Кнопка Продолжить')

        with allure.step('Падение теста'):
            raise Exception("Вспышки на солнце")
