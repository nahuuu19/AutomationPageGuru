import time
import pytest
from PageObjects.login_page import LoginPage
from PageObjects.test_login_succesfully import LoggedInSuccessfullyPage


class TestPositiveScenarios:
    @pytest.mark.login_positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        #variable que haga referencia a login page y paso el driver por parametro y que haga referencia a esa pagina
        login_page.open()
        #apertura de page
        #ahora inicio los metodos y le paso los parametro de user y passw
        login_page.execute_login("nahu@gmail.com", "password123")
        time.sleep(2)
        #ahora para validar si ingrese correctamente en la pagina correcta, inicializo el otro metodo, inicio exitoso
        logged_in_page = LoggedInSuccessfullyPage(driver)
        #verifico que la pagina a la cual me redirigio es la correcta luego de hacer el submit(loggin successfully)
        # current nos dice en que paginas estamos parados luego de hacer el login succesf.
        assert logged_in_page.expected_url == logged_in_page.current_url
        # la segunda verificacion es a traves del header
        assert logged_in_page.header == "Login Successfully"
        time.sleep(2)
        driver.close()


