import pytest
from assinatura import Assinatura, AssinaturaFamilia, AssinaturaEstudante


def test_assinatura_familia_sem_desconto():
    assinatura = AssinaturaFamilia("Ana", 40, 3)
    resultado = assinatura.calcular_fatura()
    assert resultado == 70  # 40 + (3-1)*15 = 70, sem desconto


def test_assinatura_familia_com_desconto():
    assinatura = AssinaturaFamilia("Ana", 40, 5)
    resultado = assinatura.calcular_fatura()
    # 40 + (5-1)*15 = 100 → 100 * 0.80 = 80
    assert resultado == pytest.approx(80)


def test_assinatura_estudante_com_comprovante():
    assinatura = AssinaturaEstudante("Pedro", 30, True)
    resultado = assinatura.calcular_fatura()
    assert resultado == pytest.approx(15)  # 30 * 0.5


def test_assinatura_estudante_sem_comprovante():
    assinatura = AssinaturaEstudante("Pedro", 30, False)
    resultado = assinatura.calcular_fatura()
    assert resultado == 30  # valor cheio


def test_exibir_dados():
    assinatura = AssinaturaFamilia("Ana", 40, 3)
    resultado = assinatura.exibir_dados()
    assert resultado == "Usuário: Ana, Valor mensal: 40"


def test_nao_pode_instanciar_assinatura():
    with pytest.raises(TypeError):
        Assinatura("Ana", 40)


#Utilizando Pytest, crie testes para verificar:

#1 AssinaturaFamilia com poucos membros (sem desconto de família grande).
#2 AssinaturaFamilia com 5 ou mais membros (com desconto de 20%).
#3 AssinaturaEstudante com comprovante válido (com desconto de 50%).
#4 AssinaturaEstudante sem comprovante (valor cheio).
#5 Se exibir_dados() retorna corretamente o usuário e o valor mensal.
#6 Se não é possível instanciar Assinatura diretamente.