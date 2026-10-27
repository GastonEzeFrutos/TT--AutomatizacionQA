from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

time.sleep(2)  # Espera 2 segundos para que la página cargue completamente

driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)  # Espera 1 segundo antes de ingresar la contraseña
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)  # Espera 1 segundo antes de hacer clic en el botón de inicio de sesión
driver.find_element(By.ID, "login-button").click()

time.sleep(2)  # Espera 2 segundos antes de cerrar el navegador
driver.quit()