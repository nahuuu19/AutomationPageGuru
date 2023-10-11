import time
import pytest
from PageObjects.register_login_page import LoginRegisterPage


# class TestCompleteForm:
#     @pytest.mark.register_negative
#     def test_form(self, driver):
#         register_page = LoginRegisterPage(driver)
#         register_page.open()
#         register_page.comp_form("Nahuel", "Arguello", "3584310619", "nahu@gmail.com", "Alberdi289", "Elena", "Cordoba",
#                                 "5815", "GERMANY", "nahu@gmail.com", "INCORRECTPASSWORD", "password123")
#
#         time.sleep(3)
#         assert register_page.msj_error == "PAssword and con.password does not match"
#         assert register_page.msj_error_is_displayed()
#


class TestCompleteForm:
    @pytest.mark.register_negative
    @pytest.mark.parametrize(
        "first_name, last_name, phone, email, address, city, province, postal_code, country, user_name, password, confirm_password, msj_error",
        [("Nahuel", "Arguello", "3584310619", "nahu@gmail.com", "Alberdi289", "Elena", "Cordoba", "5815", "BRAZIL",
          "nahu@gmail.com", "INCORRECTPASSWORD", "password123", "PAssword and con.password does not match")])
    def test_form(self, driver, first_name, last_name, phone, email, address, city, province, postal_code, country,
                  user_name, password, confirm_password, msj_error):
        register_page = LoginRegisterPage(driver)
        register_page.open()
        register_page.comp_form(first_name, last_name, phone, email, address, city, province, postal_code, country,
                                user_name, password, confirm_password)
        time.sleep(2)
        assert register_page.msj_error == msj_error
        assert register_page.msj_error_is_displayed()
