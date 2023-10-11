from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/login_sucess.php"
    __header__locator = (By.TAG_NAME, "h3")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # self._driver = driver

    """COMPARA LA URL ESPERADA CON LA URL QUE PASA COMO PARAMETRO"""

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def header(self) -> str:
        # return self._driver.find_element(self.__header__locator).text
        return super()._get_text(self.__header__locator)

    def is_logout_button_displayed(self) -> bool:
        # return self._driver.find_element(self.__log_out_button_locator).is_displayed()
        return super()._is_displayed(self.__log_out_button_locator)
