import pytest

@pytest.fixture
def numeros():
    return [10,20,30]

def test_suma_fixture(numeros):
    assert sum(numeros) == 60

def test_resta(numeros):
    resultado = numeros [0] - numeros [1] - numeros [2]
    assert resultado == -40

@pytest.mark.parametrize ("a,b,resultado", [
    (10,20,30),
    (5,5,10),
    (20,30,50)
])
def test_suma_parametrize(a,b,resultado):
    assert a + b == resultado

    