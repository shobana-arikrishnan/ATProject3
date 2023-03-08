import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from scenarios.adminsearch import AdminSearch


class TestSearchFunction:

    @pytest.fixture(scope="class")
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture(scope="class")
    def web_page(self, driver):
        yield AdminSearch(self.driver)

    @pytest.fixture(scope="class")
    def setup_web_page(self, web_page):
        web_page.browse()
        web_page.login()
        yield web_page

    # TC_PIM_01 - TestCase to validate the search bar functionality on admin page

    def test_menu_on_admin_page(self, setup_web_page):
        setup_web_page.go_to_admin()
        assert setup_web_page.validate_menu()

    def test_search_bar(self, setup_web_page):
        assert setup_web_page.validate_search()
        assert setup_web_page.perform_search_for_admin()
        assert setup_web_page.perform_search_for_pim()
        assert setup_web_page.perform_search_for_leave()
        assert setup_web_page.perform_search_for_time()
        assert setup_web_page.perform_search_for_recruitment()
        assert setup_web_page.perform_search_for_my_info()
        assert setup_web_page.perform_search_for_performance()
        assert setup_web_page.perform_search_for_dashboard()
        assert setup_web_page.perform_search_for_directory()
        assert setup_web_page.perform_search_for_maintenance()
        assert setup_web_page.perform_search_for_buzz()

