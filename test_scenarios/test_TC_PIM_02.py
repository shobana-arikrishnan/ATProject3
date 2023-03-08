import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from scenarios.adminmanagementpage import UserManagement


class TestDropDownAdminPage:

    @pytest.fixture(scope="class")
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture(scope="class")
    def web_page(self, driver):
        yield UserManagement(self.driver)

    @pytest.fixture(scope="class")
    def setup_web_page(self, web_page):
        web_page.browse()
        web_page.login()
        yield web_page

    # TC_PIM_02 - TestCase to validate the dropdown menus on admin page

    def test_menu_on_admin_page(self, setup_web_page):
        setup_web_page.go_to_admin()
        assert setup_web_page.validate_menu()

    def test_dropdown_on_admin_page(self, setup_web_page):
        assert setup_web_page.check_dropdown_admin_page()


