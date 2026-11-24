from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.reader import read_productos_json

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    driver.get("https://www.saucedemo.com/")

    login_page.login("standard_user","secret_sauce")

    # leer el primer producto del JSON
    producto = read_productos_json()[0]
    print(producto)

    # agregar producto del JSON
    inventory_page.agregar_producto(producto["nombre"])

    assert inventory_page.obtener_contador_carrito == "1"