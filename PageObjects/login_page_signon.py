from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from PageObjects.base_page import BasePage


class LoginPageSignOn(BasePage):
    __url = "https://demo.guru99.com/test/newtours/login.php"
    __username_field = (By.NAME, "userName")
    __password_field = (By.NAME, "password")
    __submit_button = (By.NAME, "submit")
    __error_message = (By.XPATH, "//span[contains(.,'Enter your userName and password correct')]")          #para cuando de un login negativo
    __header_welcome_locator = (By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3")

    def __init__(self, driver: WebDriver): #inicializo el driver de tipo webdriver, necesito importarlo
        super().__init__(driver) #por herencia
        # self._driver = driver

    def open(self):     #inicializo la direccion de pagina que quiero iniciar
        super()._open_url(self.__url)
        # self._driver.get(self.__url)

    def execute_login(self, username: str, password: str): #enciamos por parametro los localizadores a las funciones creadas en la base
        super()._type(self.__username_field, username) #estamos haciendo referencia a la clase padre, recibiendo el paramentro enviado desde base page
        super()._type(self.__password_field, password) #hacemos el ingreso del usuario
        super()._click(self.__submit_button)

        # #inicializo el tiempo de busqueda, necesito importarlo
        # wait = WebDriverWait(self._driver, 10)
        # #inicializo username, debo importar expected conditions. localizo el elemento y mando por paramentro keys
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys(username)
        # # inicializo password, debo importar expected conditions. localizo el elemento y mando por paramentro keys
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__password_field).send_keys(password)
        # #localizo el boton y hago click
        # wait.until(ec.visibility_of_element_located(self.__submit_button))
        # self._driver.find_element(self.__submit_button).click()

        #agregar metodo get de mensaje erroneo

    #este assert verifica si el mensaje de error esta siendo mostrado, despues de un intento de sesion incorrecto. Si es asi, el assert pasara sin problemas
    #si no esta siendo mostrado, fallara, y mostrara "Error message is not displayed".
    def is_error_message_displayed(self):
        super()._wait_until_element_is_visible(self.__error_message)
        return super()._is_displayed(self.__error_message)

    #Este assert verifica si el texto del mensaje de error coincide con el mensaje de error esperado. Si el texto del mensaje de error coincide con expected_error_message,
    # el assert pasará sin problemas. Si el texto no coincide, el assert fallará y mostrará el mensaje "Error message is not expected".
    # Esto te indicará que el mensaje de error no coincide con lo que se esperaba.
    def get_error_message_text(self):
        return super()._get_text(self.__error_message)