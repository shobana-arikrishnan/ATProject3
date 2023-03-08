class TestUpdateContactDetails:

    # TC_PIM_06 - TestCase to validate contact details update on employee page

    def test_update_contact_details(self,setup_web_page):
        assert setup_web_page.edit_employee_contact_details()