import pytest

from carro import Carro, CarroPopular, CarroLuxo, CarroEletrico


def test_carro_popular_preco_final():
    carro = CarroPopular("Fusca", 20000, 10)

    assert carro.calcular_preco_final() == 18000


def test_carro_popular_desconto():
    carro = CarroPopular("Fusca", 20000, 10)

    assert carro.calcular_desconto() == 2000


def test_carro_luxo_preco_final():
    carro = CarroLuxo("BMW", 300000, 15)

    assert carro.calcular_preco_final() == 345000


def test_carro_luxo_imposto():
    carro = CarroLuxo("BMW", 300000, 15)

    assert carro.calcular_imposto() == 45000


def test_carro_eletrico_preco_final():
    carro = CarroEletrico("Tesla", 400000, 5)

    assert carro.calcular_preco_final() == 380000


def test_exibir_dados():
    carro = CarroPopular(
        "Fusca",
        20000,
        10,
        "Ar condicionado",
        "Vidros funcionando",
        cor="Amarelo",
        ano="1998"
    )

    assert carro.exibir_dados() == (
        "Modelo: Fusca | "
        "Preço: R$ 20000.00 | "
        "Desconto: 10% | "
        "Extras: ('Ar condicionado', 'Vidros funcionando') | "
        "Informações: {'cor': 'Amarelo', 'ano': '1998'}"
    )


def test_args():
    carro = CarroPopular(
        "Fusca",
        20000,
        10,
        "Ar condicionado",
        "Vidros funcionando"
    )

    assert carro.extras == (
        "Ar condicionado",
        "Vidros funcionando"
    )


def test_kwargs():
    carro = CarroPopular(
        "Fusca",
        20000,
        10,
        cor="Amarelo",
        ano="1998"
    )

    assert carro.informacoes == {
        "cor": "Amarelo",
        "ano": "1998"
    }


def test_nao_permite_instanciar_classe_abstrata():

    with pytest.raises(TypeError):
        Carro("Fusca", 20000)