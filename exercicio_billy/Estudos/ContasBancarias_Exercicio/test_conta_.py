# test_conta.py
import pytest
from conta import Conta, ContaCorrente, ContaPoupanca


def test_conta_corrente_abrir():
    conta = ContaCorrente("Ana", "12345-6")
    resultado = conta.abrir_conta()
    assert resultado == "Conta corrente 12345-6 aberta para Ana"


def test_conta_poupanca_abrir():
    conta = ContaPoupanca("Pedro", "98765-4")
    resultado = conta.abrir_conta()
    assert resultado == "Conta poupança 98765-4 aberta para Pedro"


def test_exibir_dados():
    conta = ContaCorrente("Ana", "12345-6")
    resultado = conta.exibir_dados()
    assert resultado == "Titular: Ana, Número da conta: 12345-6"


def test_nao_pode_instanciar_conta():
    with pytest.raises(TypeError):
        Conta("Ana", "12345-6")

#Crie também um decorator chamado @registrar_matricula. Esse decorator deverá exibir a mensagem "Iniciando matrícula" antes da execução do método e "Matrícula finalizada" após sua execução. O decorator deve permitir que a função decorada receba diferentes argumentos.
#Aplique o decorator ao método matricular() das classes concretas.

#Utilizando Pytest, crie testes unitários para verificar:

#Se um curso presencial retorna corretamente a mensagem de matrícula.
#Se um curso online retorna corretamente a mensagem de matrícula.
#Se exibir_dados() retorna corretamente o aluno e o nome do curso cadastrados.
#Se não é possível criar diretamente um objeto da classe abstrata Curso, utilizando pytest.raises.