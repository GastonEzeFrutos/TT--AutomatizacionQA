import pytest

from Clase4.test_calculadora_modular import suma,resta,multiplicacion,division

@pytest.mark.operador
def test_suma():
    resultado = suma(8,3)

    assert resultado == 8

@pytest.mark.operador
def test_resta():
    resultado = resta(10,4)

    assert resultado == 6

@pytest.mark.operador
def test_multiplicacion():
    resultado = multiplicacion(5,3)

    assert resultado == 15

@pytest.mark.operador
def test_division():
    resultado = division("10",2)

    assert resultado == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(50,0)