from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

wait = WebDriverWait(driver, 10) # espera no máximo 10 segundos

wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

titulo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title"))).text
print("Título da página após login:", titulo)       

input("Pressione Enter para fechar o navegador...")
driver.quit()