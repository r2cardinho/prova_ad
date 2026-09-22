import pytest
from bloco3 import Forma, Quadrado, Circulo

def test_area_quadrado():
    assert Quadrado(4).area() == 16

def test_area_circulo():
    assert Circulo(2).area() == 12.56

def test_nao_cria_forma():
    with pytest.raises(TypeError):
        Forma()