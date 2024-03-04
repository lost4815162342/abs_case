import allure
import pytest
from selenium import webdriver
import screens


@pytest.fixture(scope="session")
def first_screen(request):
    """Запуск браузера и инициация начального состояния """
    driver = webdriver.Chrome()
    FirstScreen = screens.catalog.get('Шаг 1. Расчет')
    yield FirstScreen(driver)
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Будущий доступ к отчету через свойства"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    """По данным отчета, прикладываем скриншот для упавших тестов"""
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            first_screen = request.node.funcargs['first_screen']
            allure.attach(first_screen.driver.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
