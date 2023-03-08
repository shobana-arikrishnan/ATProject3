import pytest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from scenarios.pimmodule import PIMModule


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.close()


@pytest.fixture(scope="session")
def web_page(driver):
    yield PIMModule(driver)


@pytest.fixture(scope="session")
def setup_web_page(web_page):
    web_page.browse()
    web_page.login()
    yield web_page
    web_page.delete_employee()

