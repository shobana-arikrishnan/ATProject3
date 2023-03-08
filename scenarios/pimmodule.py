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


class PIMModule(AdminSearch):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = data_config['url']
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def add_employee(self):
        pim_option = self.wait.until(EC.presence_of_element_located((By.XPATH, locator_config['pim_locator'])))
        pim_option.click()
        add_employee_option = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['add_employee_locator'])))
        add_employee_option.click()

        try:
            firstname_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, locator_config['firstname_locator'])))
            middlename_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, locator_config['middle_name_locator'])))
            lastname_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, locator_config['lastname_locator'])))

            firstname_input.send_keys(data_config['firstname'])
            middlename_input.send_keys(data_config['middlename'])
            lastname_input.send_keys(data_config['lastname'])

            create_login_details_toggle_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, locator_config['create_login_details_toggle_locator'])))

            create_login_details_toggle_button.click()
            time.sleep(3)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator_config['status_enabling_locator']))).click()
            username_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['new_username_locator'])))
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['new_password_locator'])))
            confirm_password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['confirm_password_locator'])))

            username_input.send_keys(data_config['new_username'])
            password_input.send_keys(data_config['new_password'])
            confirm_password_input.send_keys(data_config['new_password'])

            save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['save_button_locator'])))

            save_button.click()
            time.sleep(5)
            look_for = 'viewPersonalDetails/empNumber'
            actual_url = self.driver.current_url
            return look_for in actual_url

        except NoSuchElementException:
            return False

    def validate_employee_page_menu(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['personal_details_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['contact_details_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contacts_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['dependents_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['immigration_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['job_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['salary_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['tax_exemptions_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['report_to_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['qualifications_menu_locator'])))
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['memberships_menu_locator'])))
            return True
        except NoSuchElementException:
            return False

    def edit_employee_personal_details(self):
        try:
            nickname_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['nickname_locator'])))
            nickname_input.send_keys(data_config['user_nickname'])
            other_id_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['other_id_locator'])))
            other_id_input.send_keys(data_config['user_other_id'])
            driver_license_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['driver_license_locator'])))
            driver_license_input.send_keys(data_config['user_driver_license'])
            license_expiry_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['license_expiry_date_locator'])))
            license_expiry_input.send_keys(data_config['user_driver_license_expiry'])
            ssn_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['ssn_locator'])))
            ssn_input.send_keys(data_config['user_ssn'])
            sin_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['sin_number_locator'])))
            sin_input.send_keys(data_config['user_sin'])
            nationality = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['nationality_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['nationality_to_select']
                 ))).click()
            marital_status = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['marital_status_dropdown_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['marital_status_to_select']
                 ))).click()
            dob_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['date_of_birth_locator'])))
            dob_input.send_keys(data_config['user_dob'])
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['gender_locator']))).click()
            military_service_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['military_service_locator'])))
            military_service_input.send_keys(data_config['user_military_service'])
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['smoker_locator']))).click()
            time.sleep(3)
            editpage_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['edit_save_button_locator'])))
            editpage_save_button.click()
            time.sleep(3)
            blood_type_input = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['custom_field_blood_type_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['blood_type_to_select']
                 ))).click()
            time.sleep(3)
            custom_editpage_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['custom_edit_save_button_locator'])))

            custom_editpage_save_button.click()
            verify_nickname = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[4].value") == data_config['user_nickname']
            verify_driver_license = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[7].value") == data_config['user_driver_license']
            verify_ssn = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[9].value") == data_config['user_ssn']
            verify_sin = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[10].value") == data_config['user_sin']
            verify_dob = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[11].value") == data_config['user_dob']
            verify_gender = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-radio-wrapper')[1].textContent") == data_config[
                                'user_gender']
            verify_nationality = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                     'user_nationality']
            verify_marital_status = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[1].textContent") == data_config[
                                        'user_marital_status']
            verify_blood_type = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[2].textContent") == data_config[
                                    'user_blood_type']
            verify_personal_details = verify_nickname and verify_ssn and verify_driver_license and verify_sin \
                                      and verify_nationality and verify_gender and verify_dob and verify_blood_type \
                                      and verify_marital_status

            return verify_personal_details
        except NoSuchElementException:
            return False

    def edit_employee_contact_details(self):
        contact_details_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['contact_details_menu_locator'])))
        contact_details_menu.click()
        try:
            street_1_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['street_1_locator'])))
            street_1_input.send_keys(data_config['user_street1'])
            street_2_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['street_2_locator'])))
            street_2_input.send_keys(data_config['user_street2'])
            city_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['city_locator'])))
            city_input.send_keys(data_config['user_city'])
            state_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['state_locator'])))
            state_input.send_keys(data_config['user_state'])
            zipcode_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['zipcode_locator'])))
            zipcode_input.send_keys(data_config['user_zipcode'])
            country = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['country_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['country_to_select']
                 ))).click()
            home_number_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['home_number_locator'])))
            home_number_input.send_keys(data_config['user_home'])
            mobile_number_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['mobile_number_locator'])))
            mobile_number_input.send_keys(data_config['user_mobile'])
            work_number_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['work_number_locator'])))
            work_number_input.send_keys(data_config['user_work'])
            work_email_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['work_email_locator'])))
            work_email_input.send_keys(data_config['user_work_email'])
            other_email_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['other_email_locator'])))
            other_email_input.send_keys(data_config['user_other_email'])
            time.sleep(2)
            contact_editpage_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['contacts_save_button_locator'])))
            contact_editpage_save_button.click()
            time.sleep(2)
            verify_street1 = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[1].value") == data_config['user_street1']
            verify_street2 = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[2].value") == data_config['user_street2']
            verify_city = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[3].value") == data_config['user_city']
            verify_state = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[4].value") == data_config['user_state']
            verify_zipcode = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[5].value") == data_config['user_zipcode']
            verify_country = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                 'user_country']
            verify_home = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[6].value") == data_config['user_home']
            verify_mobile = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[7].value") == data_config['user_mobile']
            verify_work = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[8].value") == data_config['user_work']
            verify_work_email = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[9].value") == data_config['user_work_email']
            verify_other_email = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[10].value") == data_config['user_other_email']

            verify_contact_details = verify_street1 and verify_street2 and verify_city and verify_state \
                                     and verify_zipcode and verify_country and verify_home and verify_mobile \
                                     and verify_work and verify_work_email and verify_other_email

            return verify_contact_details
        except NoSuchElementException:
            return False

    def edit_employee_emergency_contact_details(self):
        emergency_contact_details_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['emergency_contacts_menu_locator'])))
        emergency_contact_details_menu.click()
        emergency_contact_add_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_add_locator'])))
        emergency_contact_add_button.click()
        try:
            name_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_name_locator'])))
            name_input.send_keys(data_config['emergency_name'])
            relationship_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_relationship_locator'])))
            relationship_input.send_keys(data_config['emergency_relationship'])
            home_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_home_locator'])))
            home_input.send_keys(data_config['emergency_home'])
            mobile_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_mobile_locator'])))
            mobile_input.send_keys(data_config['emergency_mobile'])
            work_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_work_locator'])))
            work_input.send_keys(data_config['emergency_work'])

            time.sleep(2)
            emergency_contact_editpage_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['emergency_contact_save_button_locator'])))
            emergency_contact_editpage_save_button.click()
            time.sleep(5)
            verify_name = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[1].textContent") == data_config[
                              'emergency_name']
            verify_relationship = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[2].textContent") == data_config[
                                      'emergency_relationship']
            verify_home = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[3].textContent") == data_config[
                              'emergency_home']
            verify_mobile = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[4].textContent") == data_config[
                                'emergency_mobile']
            verify_work = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[5].textContent") == data_config[
                              'emergency_work']

            verify_emergency_contact_details = verify_name and verify_relationship and verify_home and verify_mobile \
                                               and verify_work

            return verify_emergency_contact_details
        except NoSuchElementException:
            return False

    def edit_employee_dependents_details(self):
        dependents_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['dependents_menu_locator'])))
        dependents_menu.click()
        dependents_add_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['dependents_add_locator'])))
        dependents_add_button.click()
        try:
            name_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['dependents_name_locator'])))
            name_input.send_keys(data_config['dependents_name'])
            relationship = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['dependents_relationship_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['dependents_relationship_to_select']
                 ))).click()
            dob_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['dependents_dob_locator'])))
            dob_input.send_keys(data_config['dependents_dob'])

            time.sleep(2)
            dependents_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['dependents_save_button_locator'])))
            dependents_save_button.click()
            time.sleep(5)
            verify_name = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[1].textContent") == data_config[
                              'dependents_name']
            verify_relationship = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[2].textContent") == data_config[
                                      'dependents_relationship']
            verify_dob = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[3].textContent") == data_config[
                             'dependents_dob']

            verify_dependents_details = verify_name and verify_relationship and verify_dob

            return verify_dependents_details
        except NoSuchElementException:
            return False

    def edit_employee_job_details(self):
        job_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['job_menu_locator'])))
        job_menu.click()
        try:
            joined_date_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['job_joined_date_locator'])))
            joined_date_input.send_keys(data_config['job_joined_date'])
            job_title = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_title_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_title_to_select']
                 ))).click()
            job_category = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_category_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_category_to_select']
                 ))).click()
            job_sub_unit = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_sub_unit_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_sub_unit_to_select']
                 ))).click()
            job_location = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_location_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_location_to_select']
                 ))).click()
            job_employment_status = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_employment_status_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_employment_status_to_select']
                 ))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['job_employment_contract_toggle_locator']))).click()
            time.sleep(2)
            contract_start_date_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['job_contract_start_date_locator'])))
            contract_start_date_input.send_keys(data_config['job_contract_start_date'])
            contract_end_date_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['job_contract_end_date_locator'])))
            contract_end_date_input.send_keys(data_config['job_contract_end_date'])
            time.sleep(2)
            job_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['job_save_button_locator'])))
            job_save_button.click()
            time.sleep(5)
            verify_joined_date = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[1].value") == data_config['job_joined_date']
            verify_job_title = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                   'job_title']
            verify_job_category = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[1].textContent") == data_config[
                                      'job_category']
            verify_subunit = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[2].textContent") == data_config[
                                 'job_sub_unit']
            verify_location = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[3].textContent") == data_config[
                                  'job_location']
            verify_employment_status = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[4].textContent") == data_config[
                                           'job_employment_status']
            verify_contract_start_date = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[2].value") == data_config[
                                             'job_contract_start_date']
            verify_contract_end_date = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[3].value") == data_config[
                                           'job_contract_end_date']

            verify_job_details = verify_joined_date and verify_job_title and verify_job_category \
                                 and verify_subunit and verify_location and verify_employment_status \
                                 and verify_contract_start_date and verify_contract_end_date

            return verify_job_details
        except NoSuchElementException:
            return False

    def edit_employee_job_termination(self):
        terminate_employment_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['terminate_employment_button_locator'])))
        terminate_employment_button.click()
        try:
            terminate_date_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['termination_date_locator'])))
            terminate_date_input.send_keys(data_config['termination_date'])
            terminate_reason = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['termination_reason_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['termination_reason_to_select']
                 ))).click()
            terminate_note = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['termination_note_locator'])))
            terminate_note.send_keys(data_config['termination_note'])
            time.sleep(2)
            termination_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['termination_save_button_locator'])))
            termination_save_button.click()
            time.sleep(5)
            verify_termination_date = self.driver.execute_script(
                "return document.getElementsByClassName('orangehrm-terminate-date')[0].textContent") == data_config[
                                          'terminated_on']
            verify_activate_employment_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['activate_employment_button_locator'])))

            verify_termination_details = verify_termination_date and verify_activate_employment_button

            return verify_termination_details
        except NoSuchElementException:
            return False

    def edit_employee_job_activation(self):
        activate_employment_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['activate_employment_button_locator'])))
        activate_employment_button.click()
        try:
            time.sleep(3)
            verify_terminate_employment_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['terminate_employment_button_locator'])))

            verify_activation_details = verify_terminate_employment_button

            return verify_activation_details
        except NoSuchElementException:
            return False

    def edit_employee_salary_details(self):
        time.sleep(3)
        salary_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['salary_menu_locator'])))
        salary_menu.click()
        time.sleep(2)
        salary_add_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['salary_add_button_locator'])))
        salary_add_button.click()
        try:
            salary_component_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['salary_component_locator'])))
            salary_component_input.send_keys(data_config['salary_component'])
            pay_grade = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_grade_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_grade_to_select']
                 ))).click()
            pay_frequency = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_frequency_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_frequency_to_select']
                 ))).click()
            time.sleep(3)
            pay_currency = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_currency_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['pay_currency_to_select']
                 ))).click()
            time.sleep(3)
            pay_amount_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['pay_amount_locator'])))
            pay_amount_input.send_keys(data_config['pay_amount'])
            comments_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['comments_locator'])))
            comments_input.send_keys(data_config['comments'])
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, locator_config['direct_deposit_details_toggle_button_locator']))).click()
            time.sleep(2)
            account_number_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['account_number_locator'])))
            account_number_input.send_keys(data_config['account_number'])
            account_type = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['account_type_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['account_type_to_select']
                 ))).click()
            routing_number_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['routing_number_locator'])))
            routing_number_input.send_keys(data_config['routing_number'])
            amount_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['amount_locator'])))
            amount_input.send_keys(data_config['amount'])

            salary_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['salary_save_button_locator'])))
            salary_save_button.click()
            time.sleep(5)

            verify_salary_component = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[1].textContent") == data_config[
                                          'salary_component']
            verify_pay_frequency = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[4].textContent") == data_config[
                                       'pay_frequency']
            verify_pay_currency = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[3].textContent") == data_config[
                                      'pay_currency']
            verify_pay_amount = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[2].textContent") == data_config[
                                    'pay_amount']
            verify_amount = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-table-cell')[5].textContent") == data_config[
                                'amount']

            verify_salary_details = verify_salary_component and verify_pay_frequency and verify_pay_currency \
                                    and verify_pay_amount and verify_amount

            return verify_salary_details
        except NoSuchElementException:
            return False

    def edit_employee_tax_exemptions_details(self):
        tax_exemptions_menu = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['tax_exemptions_menu_locator'])))
        tax_exemptions_menu.click()
        try:
            federal_tax_status = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['federal_tax_status_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['federal_tax_status_to_select']
                 ))).click()
            federal_tax_exemptions_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['federal_tax_exemptions_locator'])))
            federal_tax_exemptions_input.send_keys(data_config['federal_tax_exemptions'])
            state_tax_state = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_state_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_state_to_select']
                 ))).click()
            state_tax_status = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_status_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_status_to_select']
                 ))).click()
            state_tax_exemptions = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['state_tax_exemptions_locator'])))
            state_tax_exemptions.send_keys(data_config['state_tax_exemptions'])
            state_tax_unemployment_state = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_unemployment_state_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_unemployment_state_to_select']
                 ))).click()
            state_tax_work_state = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_work_state_locator']))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, locator_config['state_tax_work_state_to_select']
                 ))).click()
            time.sleep(3)

            tax_exemptions_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['tax_exemptions_save_button_locator'])))
            tax_exemptions_save_button.click()
            time.sleep(3)

            verify_federal_tax_status = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[0].textContent") == data_config[
                                            'federal_tax_status']

            verify_federal_tax_exemptions = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[1].value") == data_config[
                                                'federal_tax_exemptions']
            verify_state_tax_state = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[1].textContent") == data_config[
                                         'state_tax_state']
            verify_state_tax_status = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[2].textContent") == data_config[
                                          'state_tax_status']
            verify_state_tax_exemptions = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-input')[2].value") == data_config[
                                              'state_tax_exemptions']
            verify_state_tax_unemployment_state = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[3].textContent") == data_config[
                                                      'state_tax_unemployment_state']
            verify_state_tax_work_state = self.driver.execute_script(
                "return document.getElementsByClassName('oxd-select-text-input')[4].textContent") == data_config[
                                              'state_tax_work_state']

            verify_tax_exemptions_details = verify_federal_tax_status and verify_federal_tax_exemptions \
                                            and verify_state_tax_state and verify_state_tax_status \
                                            and verify_state_tax_exemptions and verify_state_tax_unemployment_state \
                                            and verify_state_tax_work_state

            return verify_tax_exemptions_details
        except NoSuchElementException:
            return False

    def delete_employee(self):
        pim_option = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['pim_menu_locator'])))
        pim_option.click()
        time.sleep(3)
        employee_name_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator_config['employee_name_locator'])))
        employee_name_input.click()
        employee_name_input.send_keys(data_config['firstname'] + ' ' + data_config['lastname'])
        time.sleep(3)
        search_button = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, locator_config['search_locator'])))
        search_button.click()
        time.sleep(3)
        try:
            delete_icon = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['delete_icon_locator'])))
            delete_icon.click()
            delete_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locator_config['delete_button_locator'])))
            delete_button.click()

        except NoSuchElementException:
            print('User not deleted!')
