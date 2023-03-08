class TestAddEmployee:

    # TC_PIM_03 - TestCase to validate side menu on pim page and  creation of new employee under pim module

    def test_validate_pim_menu(self, setup_web_page):
        assert setup_web_page.validate_menu()

    def test_new_employee_creation(self, setup_web_page):
        assert setup_web_page.add_employee()
