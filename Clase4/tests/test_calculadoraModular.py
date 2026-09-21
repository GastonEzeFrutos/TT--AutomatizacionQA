import pytest

from calculadoraModular import sumar,restar,multiplicar,dividir

@pytest.mark.operador
def test_suma_correcto():
    resultado = sumar(5,3)

    assert resultado == 8

@pytest.mark.operador
def test_suma_error():
    resultado = sumar(5,3)

    assert resultado == 2

@pytest.mark.operador
def test_resta_correcto():
    resultado = restar(10,4)

    assert resultado == 6

@pytest.mark.operador
def test_resta_error():
    resultado = restar(10,4)

    assert resultado == 3

@pytest.mark.operador
def test_multiplicacion_correcto():
    resultado = multiplicar(5,3)

    assert resultado == 15

@pytest.mark.operador
def test_multiplicacion_error():
    resultado = multiplicar(5,3)

    assert resultado == 5    

@pytest.mark.operador
def test_division():
    resultado = dividir(10,2)

    assert resultado == 5

@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(50,0)



# Uso de Fixtures
# Para números enteros
@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes."""
    return 20, 5


def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 4

# Para valores flotantes
@pytest.fixture
def numeros_flotantes():
    """Prepara dos valores flotantes."""
    return 0.1, 0.2


def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert sumar(a, b) == 0.30000000000000004

# Parametrización
# Permite probar múltiples combinaciones sin duplicar funciones.

@pytest.mark.parametrize(
"a,b,esperado",
[
(1, 2, 3),
(-1, -1, -2),
(2.5, 0.5, 3),
(0, 0, 0)
]
)
def test_sumar_varios(a, b, esperado):
    assert sumar(a, b) == esperado