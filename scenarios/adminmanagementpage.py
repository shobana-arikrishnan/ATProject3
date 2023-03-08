import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scenarios.adminsearch import AdminSearch
from yaml_function import YAML

yaml_file = os.getcwd() + '\\config.yaml'
base_config = YAML(yaml_file).read()
data_config = base_config['Data']
locator_config = base_config['Locators']


class UserManagement(AdminSearch):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data_config['url']
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def check_dropdown_admin_page(self):
        try:
            user_management_header = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['user_management_locator'])))
            user_management_header.click()
            users_selection = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['users_selection_locator'])))
            users_selection.click()

            # To verify user role dropdown values
            time.sleep(3)
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator_config['user_role_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['user_role_dropdown_1']))).click()
            time.sleep(2)
            verify_user_role_admin = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                         'user_role_1']
            time.sleep(2)
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator_config['user_role_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['user_role_dropdown_2']))).click()
            time.sleep(2)
            verify_user_role_ess = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                       'user_role_2']
            verify_user_role = verify_user_role_admin and verify_user_role_ess

            # To verify status dropdown values
            time.sleep(2)
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator_config['user_status_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['user_status_dropdown_1']))).click()
            time.sleep(2)
            verify_user_status_enabled = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[1].textContent") == data_config[
                                             'status_1']
            time.sleep(2)
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator_config['user_status_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['user_status_dropdown_2']))).click()
            time.sleep(2)
            verify_user_status_disabled = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[1].textContent") == data_config[
                                              'status_2']
            verify_user_status = verify_user_status_enabled and verify_user_status_disabled

            return verify_user_role and verify_user_status
        except NoSuchElementException:
            return False
