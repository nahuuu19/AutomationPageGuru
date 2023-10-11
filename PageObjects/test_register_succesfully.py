
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class RegisterInSuccessfullyPage(BasePage):
    __actual_url = "https://demo.guru99.com/test/newtours/register_sucess.php"
    __note_locator = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b")
    __header__locator = (By.XPATH, "//a[@href='login.php'][text()=' sign-in ']")
    __dear_locartor = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b")

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

    @property
    def note(self) -> str:
        return super()._get_text(self.__note_locator)

    @property
    def dear(self) -> str:
        return super()._get_text(self.__dear_locartor)


