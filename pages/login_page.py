from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object da tela de login do SauceDemo."""

    URL = "https://www.saucedemo.com"

    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_LOGIN = (By.ID, "login-button")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        """Abre a página de login."""
        self.driver.get(self.URL)

    def fazer_login(self, usuario, senha):
        """Preenche usuário e senha e clica em Login."""
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_USUARIO)).send_keys(usuario)
        self.driver.find_element(*self.CAMPO_SENHA).send_keys(senha)
        self.driver.find_element(*self.BOTAO_LOGIN).click()

    def obter_mensagem_erro(self):
        """Retorna o texto da mensagem de erro exibida após um login inválido."""
        return self.wait.until(EC.visibility_of_element_located(self.MENSAGEM_ERRO)).text