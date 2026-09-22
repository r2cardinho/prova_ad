import pytest 

from pagamento import Pagamento, PagamentoPIX, PagamentoCartao

def test_pagamento_cartao_processar():
    cartao_1= PagamentoCartao("Felipe, 500")
    resultado = cartao_1.processar()
    assert cartao_1== "Pagamento de 500 reais no cartao aprovado para Felipe"
    #Se um pagamento por cartão retorna corretamente a mensagem de aprovação.

def test_pagamento_pix_processar():
    pix_1= PagamentoPIX("Carlos, 250")
    resultado = pix_1.processar()
    assert pix_1== "Pagamento de 250 reais no PIX aprovado para Felipe"
    #Se um pagamento por Pix retorna corretamente a mensagem de aprovação.


def test_exibir_dados():
    pagamento = PagamentoCartao("Felipe", 500)
    resultado = pagamento.exibir_dados()
    assert resultado == "Cliente: Felipe, Valor: 500"
    #igual o exibir dados declarado no exercicio
    #Se exibir_dados() retorna corretamente o cliente e o valor cadastrados.

def test_nao_pode_instanciar_pagamento():
    with pytest.raises(TypeError):
        Pagamento("Felipe, 500")

#Se não é possível criar diretamente um objeto da classe abstrata Pagamento, utilizando pytest.raises.