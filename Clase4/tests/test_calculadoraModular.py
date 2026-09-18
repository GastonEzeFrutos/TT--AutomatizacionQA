import pytest

from calculadoraModular import sumar,restar,multiplicar,dividir

@pytest.mark.operador
def test_suma():
    resultado = sumar(5,3)

    assert resultado == 8

@pytest.mark.operador
def test_resta():
    resultado = restar(10,4)

    assert resultado == 6

@pytest.mark.operador
def test_multiplicacion():
    resultado = multiplicar(5,3)

    assert resultado == 15

@pytest.mark.operador
def test_division():
    resultado = dividir(10,2)

    assert resultado == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(50,0)