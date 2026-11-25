from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdutosPage:
    TITULO = (By.CLASS_NAME, "title")
    ICONE_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")
    BADGE_CARRINHO = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obter_titulo(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITULO)).text

    def adicionar_ao_carrinho(self, id_produto):
        botao = (By.ID, f"add-to-cart-{id_produto}")
        self.wait.until(EC.element_to_be_clickable(botao)).click()

    def obter_quantidade_carrinho(self):
        return self.wait.until(EC.visibility_of_element_located(self.BADGE_CARRINHO)).text

    def abrir_carrinho(self):
        self.driver.find_element(*self.ICONE_CARRINHO).click()