import pytest
from selenium import webdriver
from page_object import BasePage
from screens.base import BaseScreen


@pytest.fixture(scope="session")
def browser(request):
    driver = webdriver.Chrome()
    request.driver = driver
    yield BaseScreen(driver)
    driver.quit()

