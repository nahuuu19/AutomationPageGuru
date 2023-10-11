from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class LoggedInSuccessfullyPageSignOn(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/login.php"
    __username_locator = (By.XPATH, "//input[@name='userName']")
    __password_locator = (By.XPATH, "//input[contains(@name,'password')]")
    __header_welcome_locator = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3")
    __submit_button_locator = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/input")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # self._driver = driver

    @property
    def expected_url(self) -> str:
        return self.__actual_url

    @property
    def header(self) -> str:
        # return self._driver.find_element(self.__header__locator).text
        return super()._get_text(self.__header_welcome_locator)

    def is_logout_button_displayed(self) -> bool:
        # return self._driver.find_element(self.__log_out_button_locator).is_displayed()
        return super()._is_displayed(self.__submit_button_locator)