import os

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from yaml_function import YAML

yaml_file = os.getcwd() + '\\config.yaml'
base_config = YAML(yaml_file).read()
data_config = base_config['Data']
locator_config = base_config['Locators']


class AdminSearch:

    def __init__(self, driver):
        self.url = data_config['url']
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def login(self):
        try:
            username_locator = self.wait.until(
                EC.presence_of_element_located((By.NAME, locator_config['username_locator'])))
            password_locator = self.wait.until(
                EC.presence_of_element_located((By.NAME, locator_config['password_locator'])))
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['LoginButton'])))

            username_locator.send_keys(data_config['username'])
            password_locator.send_keys(data_config['password'])
            login_button.click()

        except NoSuchElementException:
            print('Some of the elements are missing!')

    def go_to_admin(self):
        admin_page = self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['admin_menu_locator'])))
        admin_page.click()

    def validate_menu(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['admin_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['pim_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['leave_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['time_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['recruitment_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['my_info_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['performance_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['dashboard_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['directory_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['maintenance_menu_locator'])))
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['buzz_menu_locator'])))
            return True
        except NoSuchElementException:
            return False

    def validate_search(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_bar_locator'])))
            return True
        except NoSuchElementException:
            return False

    def clear_search_term(self):
        self.driver.execute_script(
            "document.querySelector('#app " +
            "> div.oxd-layout " +
            "> div.oxd-layout-navigation " +
            "> aside > nav " +
            "> div.oxd-sidepanel-body " +
            "> div > div > input').value = \"\"")

    def perform_search_for_admin(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_admin'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_admin']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_admin'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_admin']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

        # searching for PIM in menu

    def perform_search_for_pim(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_pim'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_pim']
            # clearing search query
            self.clear_search_term()
            search_bar.send_keys(data_config['search_pim'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_pim']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

        # searching for Leave in menu

    def perform_search_for_leave(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_leave'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_leave']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_leave'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_leave']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

        # searching for Time in menu

    def perform_search_for_time(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_time'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_time']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_time'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_time']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

        # searching for Recruitment in menu

    def perform_search_for_recruitment(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_recruitment'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_recruitment']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_recruitment'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_recruitment']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for My_Info in menu
    def perform_search_for_my_info(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_my_info'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_my_info']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_my_info'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_my_info']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for performance in menu
    def perform_search_for_performance(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_performance'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_performance']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_performance'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_performance']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for dashboard in menu
    def perform_search_for_dashboard(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_dashboard'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_dashboard']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_dashboard'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_dashboard']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for directory in menu
    def perform_search_for_directory(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_directory'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_directory']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_directory'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_directory']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for maintenance in menu
    def perform_search_for_maintenance(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_maintenance'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_maintenance']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_maintenance'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_maintenance']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False

    # searching for buzz in menu
    def perform_search_for_buzz(self):
        try:
            search_bar = self.driver.find_element(by=By.XPATH, value=locator_config['search_bar_locator'])
            search_bar.send_keys(data_config['search_buzz'].lower())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            lower_case_result = search_result == data_config['search_buzz']
            self.clear_search_term()
            search_bar.send_keys(data_config['search_buzz'].upper())
            self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['search_result_locator'])))
            search_result = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-text')[0].textContent")
            upper_case_result = search_result == data_config['search_buzz']
            self.clear_search_term()
            return upper_case_result and lower_case_result
        except NoSuchElementException:
            return False
