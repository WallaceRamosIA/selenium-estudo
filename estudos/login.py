from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com") 

# Preenchendo os campos
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Clicando no botão de login
driver.find_element(By.ID, "login-button").click()

# Lendo o resultado da página após o login
Titulo = driver.find_element(By.CLASS_NAME, "title").text
print("Título da página após login:", Titulo)
print("URL atual:", driver.current_url)

input("Pressione Enter para fechar o navegador...")


