class TestUpdatePersonalDetails:

    # TC_PIM_05 - TestCase to validate personal details update on employee page

    def test_update_personal_details(self,setup_web_page):
        assert setup_web_page.edit_employee_personal_details()