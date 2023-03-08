class TestJobActivationEmployment:

    # TC_PIM_11 - TestCase to validate activate employment update on employee page

    def test_job_activation_employment(self,setup_web_page):
        assert setup_web_page.edit_employee_job_activation()