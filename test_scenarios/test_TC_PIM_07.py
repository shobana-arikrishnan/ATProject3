class TestUpdateEmergencyContactDetails:

    # TC_PIM_07 - TestCase to validate emergency contact details update on employee page

    def test_update_emergency_contact_details(self,setup_web_page):
        assert setup_web_page.edit_employee_emergency_contact_details()