from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarrinhoPage:
    NOMES_ITENS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obter_nomes_itens(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(EC.visibility_of_element_located(self.NOMES_ITENS))
        elementos = self.driver.find_elements(*self.NOMES_ITENS)
        return [elemento.text for elemento in elementos]