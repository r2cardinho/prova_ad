from abc import ABC, abstractmethod
from functools import wraps

def registrar_acionamento(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Acionando dispositivo")
        resultado=func(*args, **kwargs)
        print(f"Dispositivo acionado")
        return resultado

    return wrapper

class Dispositivo(ABC):
    def __init__(self, nome, comodo,*args,**kwargs):
        self.nome = nome
        self.comodo = comodo

    def exibir_dados(self):
        print(f"o Dispositivo: {self.nome}, está ligado no cômodo: {self.comodo}")

    @abstractmethod
    def ligar(self):
        pass

class Lampada(Dispositivo):
    @registrar_acionamento
    def ligar(self):
        print(f"Lâmpada do(a) {self.comodo}, está ligada")

class ArCondicionado(Dispositivo):
    @registrar_acionamento
    def ligar(self):
        print(f"Ar Condicionado do {self.comodo}, está ligado")


ar_1=ArCondicionado("Samsung", "Quarto")
print(ar_1.exibir_dados())
print(ar_1.ligar())

lampada_1=Lampada("Philips Luz Neon", "Sala de Estar")
print(lampada_1.exibir_dados())
print(lampada_1.ligar())
    



        
    