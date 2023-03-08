class TestUpdateDependentsDetails:

    # TC_PIM_08 - TestCase to validate dependents details update on employee page

    def test_update_dependents_details(self,setup_web_page):
        assert setup_web_page.edit_employee_dependents_details()