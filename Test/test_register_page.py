import pytest
from PageObjects.register_login_page import LoginRegisterPage
from PageObjects.test_register_succesfully import RegisterInSuccessfullyPage


class TestCompleteForm:
    @pytest.mark.register_positive
    def test_form(self, driver):
        register_page = LoginRegisterPage(driver)
        register_page.open()
        register_page.comp_form("Nahuel", "Arguello", "3584310619", "nahu@gmail.com", "Alberdi289", "Elena", "Cordoba",
                                "5815", "GERMANY", "nahu@gmail.com", "password123", "password123")

        register_successfully_page = RegisterInSuccessfullyPage(driver)
        assert register_successfully_page.expected_url == register_page.current_url
        assert register_successfully_page.note == "Note: Your user name is nahu@gmail.com."
        assert register_successfully_page.header == "sign-in"
        assert register_successfully_page.dear == 'Dear Nahuel Arguello,'

# class TestCompleteForm:
#     @pytest.mark.register
#     @pytest.mark.parametrize(
#         "first_name, last_name, phone, email, address, city, province, postal_code, country, user_name, password, confirm_password",
#         [("Nahuel", "Arguello", "3584310619", "nahu@gmail.com", "Alberdi289", "Elena", "Cordoba", "5815", "BRAZIL",
#           "nahu@gmail.com", "password123", "password123")])
#     def test_form(self, driver, first_name, last_name, phone, email, address, city, province, postal_code, country, user_name, password, confirm_password):
#         register_page = LoginRegisterPage(driver)
#         register_page.open()
#         register_page.comp_form(first_name, last_name, phone, email, address, city, province, postal_code, country, user_name, password, confirm_password)
#
#         register_successfully_page = RegisterInSuccessfullyPage(driver)
#         assert register_successfully_page.expected_url == register_page.current_url
#         # assert register_successfully_page.header == f"Dear {first_name} {last_name},"
#         # assert RegisterInSuccessfullyPage.note == f"Note: Your user name is {user_name}."
