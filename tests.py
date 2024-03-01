import allure

from page_object import SearchHelper


def test_yandex_search(request, browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" and "Видео" in elements


def test_step1(browser):
    step1 = browser.screen('Шаг 1. Расчет')
    step1.click('Чекбокс - Подтверждение отсутствия Covid19 у сожителя')\
        .click('Чекбокс - Согласие на обработку персданных')\
        .click('Кнопка Продолжить')

    # step2 = browser.screen('Шаг 2.  Ввод данных')



@allure.feature('Random dog')
@allure.story('Получение фото случайной собаки и вложенные друг в друга шаги')
def test_allure_asjdklasdjklasjdl():
    assert 1 == 1