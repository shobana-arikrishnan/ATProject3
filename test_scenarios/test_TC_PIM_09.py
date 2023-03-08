class TestUpdateJobDetails:

    # TC_PIM_09 - TestCase to validate job details update on employee page

    def test_update_job_details(self,setup_web_page):
        assert setup_web_page.edit_employee_job_details()