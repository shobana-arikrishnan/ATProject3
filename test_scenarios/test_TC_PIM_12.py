class TestUpdateSalaryDetails:

    # TC_PIM_12 - TestCase to validate salary update on employee page

    def test_update_salary_details(self,setup_web_page):
        assert setup_web_page.edit_employee_salary_details()