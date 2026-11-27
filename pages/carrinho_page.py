from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarrinhoPage:
    """Page Object da página do carrinho (/cart.html)."""

    # O seletor usa ".cart_item" porque a classe "inventory_item_name" também
    # existe na página de produtos. Sem isso, a espera passaria na página errada.
    NOMES_ITENS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    BOTAO_CHECKOUT = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obter_nomes_itens(self):
        """Retorna a lista com os nomes dos produtos que estão no carrinho."""
        # Espera a navegação terminar antes de ler (evita condição de corrida).
        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(EC.visibility_of_element_located(self.NOMES_ITENS))
        elementos = self.driver.find_elements(*self.NOMES_ITENS)
        return [elemento.text for elemento in elementos]

    def iniciar_checkout(self):
        """Clica em Checkout para seguir ao formulário de dados."""
        self.wait.until(EC.element_to_be_clickable(self.BOTAO_CHECKOUT)).click()