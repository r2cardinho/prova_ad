from abc import abstractmethod, ABC
from functools import wraps

def registrar_envio(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando envio da notificação")
        resultado = func(*args, **kwargs)
        print("Envio finalizado")
        return resultado
    return wrapper


class Notificacao(ABC):
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def exibir_dados(self):
        return f"DESTINATARIO: {self.destinatario} | MENSAGEM: {self.mensagem}"

    @abstractmethod
    def enviar(self):
        pass


class NotificacaoEmail(Notificacao):

    @registrar_envio
    def enviar(self):
        return f"E-mail enviado para {self.destinatario}"

class NotificacaoSMS(Notificacao):

    @registrar_envio
    def enviar(self):
        return f"SMS enviado para {self.destinatario}"


print(NotificacaoEmail("Rigui", "Mensagem 1").enviar())
print(NotificacaoSMS("Billy", "Mensagem 2").enviar())

print(NotificacaoEmail("Rigui", "Mensagem 1").exibir_dados())
print(NotificacaoSMS("Billy", "Mensagem 2").exibir_dados())

  