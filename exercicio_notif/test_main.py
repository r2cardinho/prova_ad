import pytest
from main import Notificacao, NotificacaoEmail, NotificacaoSMS

def test_notif_email_retorna_mensagem():
    assert (NotificacaoEmail("Rigui", "Uma Mensagem").enviar()) == "E-mail enviado para Rigui"

def test_notif_sms_retorna_mensagem():
    assert (NotificacaoSMS("Billy", "Outra Mensagem").enviar()) == "SMS enviado para Billy"

def test_exibir_dados_destinatario_mensagem_correto_email():
    assert (NotificacaoEmail("Rigui", "Testando exibir dados E-mail").exibir_dados()) == "DESTINATARIO: Rigui | MENSAGEM: Testando exibir dados E-mail"

def test_exibir_dados_destinatario_mensagem_correto_sms():
    assert (NotificacaoSMS("Billy", "Testando exibir dados SMS").exibir_dados()) == "DESTINATARIO: Billy | MENSAGEM: Testando exibir dados SMS"

def test_criar_classe_abstrata_notificacao():
    with pytest.raises(TypeError):
        Notificacao("Destinatario", "Mensagem")
