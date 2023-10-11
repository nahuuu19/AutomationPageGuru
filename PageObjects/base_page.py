from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


#va a tener todas las funciones que va a tener la pagina

class BasePage:

    #instacio el metodo driver
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        #localiza cualquier elemento de la pagina
        # * porque al mandar una tupla, puede ser mas de un elemento
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)         #hace visible cualquier elemento, le pasa un tiempo limite de busqueda
        self._find(locator).send_keys(text) #si se encuentra el locator, se envia el texto que es recibido en loginpage por executelogin

    def select_combo(self, locator: tuple, value: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()
        self._find((By.XPATH, f"//select[@name='country']/option[text()='{value}']")).click()

    def _clear(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):      #define si un elemento esta visible y le agrega un tiempo de espera
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):      #define si un elemento esta visible y le agrega un tiempo de espera
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_until_element_is_invisibility(self, locator: tuple, time: int = 10):      #define si un elemento esta visible y le agrega un tiempo de espera
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def _open_url(self, url: str):
        self._driver.maximize_window()
        self._driver.get(url)           #permite poder abrir la url


    @property
    #conserva los atributos de url que instancia y sirven para comparar.
    # currenturl junto con el driver obtiene la url actual en ese momento de la ejecucucion
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:  #para ver si esta disponible o no, y returna un t o f de acuerdo a lo que encuentre
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _get_text(self, locator: tuple, time: int = 10) -> str:        #la clase base contiene todas las funciones, ya sea por login pos o neg, esta funcion devuelve el texto
        self._wait_until_element_is_visible(locator, time)          #que se genera en el momento a traves de un tiempo de espera
        return self._find(locator).text



#todas estas funciones las puedo utilizaar por herencia en las clases hijas de loginpage

