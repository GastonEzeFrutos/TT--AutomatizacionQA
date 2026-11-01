from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_exitoso():
    # Iniciar el navegador
    driver = webdriver.Chrome()

    # Abrir pagina
    driver.get("https://www.saucedemo.com/")

    # Localizar elementos
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")

    

    # Completar el formulario
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    time.sleep(2)

    # Hacer login
    boton_login.click()

    titulo = driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')

    # Validar el URL despues del login
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert titulo.text == "Products"

    driver.quit()

# arrancar con python -m pytest test_login.py