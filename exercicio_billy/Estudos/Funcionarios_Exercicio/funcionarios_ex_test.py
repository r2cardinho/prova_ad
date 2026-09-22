import pytest

from funcionario import Funcionario, FuncionarioCLT, FuncionarioPJ, Estagiario


def test_funcionario_clt_salario():
    clt = FuncionarioCLT("Felipe", 6000, 500)

    assert clt.calcular_salario() == 6500


def test_funcionario_clt_bonus():
    clt = FuncionarioCLT("Felipe", 6000, 500)

    assert clt.calcular_bonus() == 500


def test_funcionario_pj_salario():
    pj = FuncionarioPJ("João", 5000, 10)

    assert pj.calcular_salario() == 5500


def test_funcionario_pj_bonus():
    pj = FuncionarioPJ("João", 5000, 10)

    assert pj.calcular_bonus() == 500


def test_estagiario_salario():
    estagiario = Estagiario("Carlos", 1800, 400)

    assert estagiario.calcular_salario() == 2200


def test_estagiario_bonus():
    estagiario = Estagiario("Carlos", 1800, 400)

    assert estagiario.calcular_bonus() == 400


def test_nao_permite_instanciar_classe_abstrata():

    with pytest.raises(TypeError):
        Funcionario("Felipe", 6000)