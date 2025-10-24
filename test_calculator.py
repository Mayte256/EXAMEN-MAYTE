import pytest
from calculator import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(4, 4) == 8, "4 + 4 debería ser 8"
    assert sumar(2, 3) == 5, "2 + 3 debería ser 5"
    assert sumar(-1, 1) == 0, "-1 + 1 debería ser 0"

def test_restar():
    assert restar(10, 3) == 7
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 3) == -6

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(6, 3) == 2
    
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)