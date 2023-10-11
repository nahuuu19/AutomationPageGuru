import pytest
import time
from PageObjects.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.negative_login
    def test_login_negative(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        time.sleep(1)
        login_page.execute_login("nahuel", "incorrectpassword")
        time.sleep(1)
        assert login_page.is_error_message_displayed(), "Error message is not displayed, but it should be"
        assert login_page.get_error_message_text(), "Enter your username and password correct"