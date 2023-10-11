import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class LoginRegisterPage(BasePage):
    __url = "https://demo.guru99.com/test/newtours/register.php"
    __first_name = (By.NAME, "firstName")
    __last_name = (By.NAME, "lastName")
    __phone = (By.NAME, "phone")
    __email = (By.NAME, "userName")
    __address = (By.NAME, "address1")
    __city = (By.NAME, "city")
    __country = (By.NAME, "country")
    # __countrySelect = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select/option[9]")
    __province = (By.NAME, "state")
    __postal_code = (By.NAME, "postalCode")
    __user_name = (By.NAME, "email")
    __password = (By.NAME, "password")
    __confirm_password = (By.NAME, "confirmPassword")
    __send_button = (By.NAME, "submit")
    __actual_url = "https://demo.guru99.com/test/newtours/login_sucess.php"
    __msj_error = (By.XPATH, "//span[contains(.,'PAssword and con.password does not match')]")

    # def select_default_country(self, default_country):
    #     self.select_combo(self.__country, (By.XPATH, f"//select[@name='country']/option[text()='{default_country}']"))

    def __init__(self, driver: WebDriver): #inicializo el driver de tipo webdriver, necesito importarlo
        super().__init__(driver) #por herencia
        # self._driver = driver

    def open(self):     #inicializo la direccion de pagina que quiero iniciar
        super()._open_url(self.__url)
        # self._driver.get(self.__url)

    #completar formulario
    def comp_form(self, first_name, last_name, phone, email, address, city, province, postal_code, country, user_name, password, confirm_password):
        print("Completing the form")
        super()._click(self.__first_name)
        print(f"Typing the first name: {first_name}")
        time.sleep(1)
        super()._type(self.__first_name, first_name)
        super()._click(self.__last_name)
        print(f"Typing the last name: {last_name}")
        time.sleep(1)
        super()._type(self.__last_name, last_name)
        super()._click(self.__phone)
        print(f"Typing the phone: {phone}")
        time.sleep(1)
        super()._type(self.__phone, phone)
        super()._click(self.__email)
        print(f"Typing the email: {email}")
        time.sleep(1)
        super()._type(self.__email, email)
        super()._click(self.__address)
        print(f"Typing the address: {address} ")
        time.sleep(1)
        super()._type(self.__address, address)
        super()._click(self.__city)
        print(f"Typing the city: {city}")
        time.sleep(1)
        super()._type(self.__city, city)
        super()._click(self.__province)
        print(f"Typing the province: {province}")
        time.sleep(1)
        super()._type(self.__province, province)
        super()._click(self.__postal_code)
        print(f"Typing the postal code: {postal_code}")
        time.sleep(1)
        super()._type(self.__postal_code, postal_code)
        super().select_combo(self.__country, country)
        super()._click(self.__user_name)
        print(f"Typing the user name: {user_name}")
        time.sleep(1)
        super()._type(self.__user_name, user_name)
        super()._click(self.__password)
        print(f"Typing the password: {password}")
        time.sleep(1)
        super()._type(self.__password, password)
        super()._click(self.__confirm_password)
        super()._type(self.__confirm_password, confirm_password)
        print(f"Typing the confirm password: {confirm_password}")
        time.sleep(1)
        super()._wait_until_element_is_visible(self.__send_button)
        super()._click(self.__send_button)
        print("Completed form")

    def msj_error_is_displayed(self) -> bool:
        return super()._is_displayed(self.__msj_error)

    @property
    def msj_error(self) -> str:
        return super()._get_text(self.__msj_error)

