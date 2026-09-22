import pytest
from dispositivo import Dispositivo, Lampada, ArCondicionado


def test_acender_lampada_ligar():
    lampada_1 = Lampada("Philips", "Quarto")
    resultado = lampada_1.ligar()
    assert resultado == "Lâmpada do(a) Quarto ligada"


def test_ar_condicionado_ligar():
    arcondicionado_1 = ArCondicionado("Samsung", "Sala de Estar")
    resultado = arcondicionado_1.ligar()
    assert resultado == "Ar-condicionado do(a) Sala de Estar ligado"


def test_exibir_dados():
    dispositivo = Lampada("Philips", "Quarto")
    resultado = dispositivo.exibir_dados()
    assert resultado == "o Dispositivo: Philips, está ligado no cômodo: Quarto"


def test_nao_pode_instanciar_dispositivo():
    with pytest.raises(TypeError):
        Dispositivo("Philips", "Quarto")


#Por fim, utilizando Pytest, crie testes unitários para verificar:

#1- Se a lâmpada retorna corretamente a mensagem ao ser ligada.
#2- Se o ar-condicionado retorna corretamente a mensagem ao ser ligado.
#3- Se exibir_dados() retorna corretamente o nome e o cômodo cadastrados.
#4- Se não é possível criar diretamente um objeto da classe abstrata Dispositivo, utilizando pytest.raises.