class TestJobTerminateEmployment:

    # TC_PIM_10 - TestCase to validate terminate employment update on employee page

    def test_job_terminate_employment(self,setup_web_page):
        assert setup_web_page.edit_employee_job_termination()