from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdutosPage:
    """Page Object da página de produtos (/inventory.html)."""

    TITULO = (By.CLASS_NAME, "title")
    ICONE_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")
    BADGE_CARRINHO = (By.CLASS_NAME, "shopping_cart_badge")
    ORDENACAO = (By.CLASS_NAME, "product_sort_container")
    NOMES_PRODUTOS = (By.CLASS_NAME, "inventory_item_name")
    PRECOS_PRODUTOS = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obter_titulo(self):
        """Retorna o título da página (usado para confirmar que o login funcionou)."""
        return self.wait.until(EC.visibility_of_element_located(self.TITULO)).text

    def adicionar_ao_carrinho(self, id_produto):
        """Adiciona um produto ao carrinho. Ex.: 'sauce-labs-backpack'."""
        botao = (By.ID, f"add-to-cart-{id_produto}")
        self.wait.until(EC.element_to_be_clickable(botao)).click()

    def obter_quantidade_carrinho(self):
        """Retorna o número exibido no ícone do carrinho, como texto."""
        return self.wait.until(EC.visibility_of_element_located(self.BADGE_CARRINHO)).text

    def abrir_carrinho(self):
        """Clica no ícone do carrinho."""
        self.driver.find_element(*self.ICONE_CARRINHO).click()

    def ordenar_por(self, valor):
        """Escolhe a ordenação: 'az', 'za', 'lohi' ou 'hilo'."""
        dropdown = self.wait.until(EC.element_to_be_clickable(self.ORDENACAO))
        # O Select só funciona com tags <select> reais, como este dropdown.
        Select(dropdown).select_by_value(valor)

    def obter_nomes_produtos(self):
        """Retorna a lista com os nomes dos produtos, na ordem exibida."""
        elementos = self.driver.find_elements(*self.NOMES_PRODUTOS)
        return [elemento.text for elemento in elementos]

    def obter_precos_produtos(self):
        """Retorna a lista de preços como números, na ordem exibida."""
        elementos = self.driver.find_elements(*self.PRECOS_PRODUTOS)
        # Converte "$29.99" em 29.99. Como texto, "$15.99" viria antes de "$7.99".
        return [float(elemento.text.replace("$", "")) for elemento in elementos]