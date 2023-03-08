class TestUpdateTaxExemptionsDetails:

    # TC_PIM_13 - TestCase to validate tax exemptions update on employee page

    def test_update_tax_exemptions_details(self,setup_web_page):
        assert setup_web_page.edit_employee_tax_exemptions_details()
