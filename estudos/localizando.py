from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com") 

# Localizando por ID
campo_usuario = driver.find_element(By.ID, "user-name")

# Localizando por CSS Selector
campo_senha = driver.find_element(By.CSS_SELECTOR, "#password")

# Localizando por XPATH
botao_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')

# Verificando o que encontramos
print("Usuário visível?", campo_usuario.is_displayed())
print("Senha visível?", campo_senha.is_displayed())
print("Botão de login visível?", botao_login.is_displayed())
print("Texto do botão:", botao_login.get_attribute("value"))

input("Pressione Enter para fechar o navegador...")
driver.quit()   