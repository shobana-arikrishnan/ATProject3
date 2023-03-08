class TestValidateEmployeePageMenu:

    # TC_PIM_04 - TestCase to validate menu on employee page under pim module

    def test_validate_employee_page_menu(self,setup_web_page):
        assert setup_web_page.validate_employee_page_menu()