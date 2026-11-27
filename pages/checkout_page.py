from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object do fluxo de checkout (dados, resumo e confirmação)."""

    CAMPO_NOME = (By.ID, "first-name")
    CAMPO_SOBRENOME = (By.ID, "last-name")
    CAMPO_CEP = (By.ID, "postal-code")
    BOTAO_CONTINUAR = (By.ID, "continue")
    BOTAO_FINALIZAR = (By.ID, "finish")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "[data-test='error']")
    MENSAGEM_CONFIRMACAO = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def preencher_dados(self, nome, sobrenome, cep):
        """Preenche o formulário de dados do comprador."""
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_NOME)).send_keys(nome)
        self.driver.find_element(*self.CAMPO_SOBRENOME).send_keys(sobrenome)
        self.driver.find_element(*self.CAMPO_CEP).send_keys(cep)

    def continuar(self):
        """Clica em Continue para seguir ao resumo do pedido."""
        self.driver.find_element(*self.BOTAO_CONTINUAR).click()

    def finalizar(self):
        """Clica em Finish no resumo do pedido."""
        # Espera a página do resumo carregar antes de clicar (evita condição de corrida).
        self.wait.until(EC.url_contains("checkout-step-two"))
        self.wait.until(EC.element_to_be_clickable(self.BOTAO_FINALIZAR)).click()

    def obter_mensagem_confirmacao(self):
        """Retorna o texto da tela de confirmação do pedido."""
        return self.wait.until(EC.visibility_of_element_located(self.MENSAGEM_CONFIRMACAO)).text

    def obter_mensagem_erro(self):
        """Retorna o texto do erro exibido quando falta algum dado obrigatório."""
        return self.wait.until(EC.visibility_of_element_located(self.MENSAGEM_ERRO)).text