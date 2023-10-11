import time
import pytest
from PageObjects.login_page_signon import LoginPageSignOn
from PageObjects.test_login_successfully_signon import LoggedInSuccessfullyPageSignOn


class TestPositiveScenarios:
    @pytest.mark.login_positive_signon
    def test_positive_signon(self, driver):
        login_page = LoginPageSignOn(driver)
        login_page.open()
        time.sleep(2)
        login_page.execute_login("nahu@gmail.com", "password123")
        time.sleep(2)
        logged_in_page = LoggedInSuccessfullyPageSignOn(driver)
        assert logged_in_page.header == "Login Successfully"
