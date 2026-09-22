
from abc import ABC, abstractmethod
from functools import wraps

def registrar_fatura(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Gerando fatura...")
        resultado = func(*args, **kwargs)
        print("Fatura gerada")
        return resultado
    return wrapper


class Assinatura(ABC):
    def __init__(self, usuario, valor_mensal):
        self.usuario = usuario
        self.valor_mensal = valor_mensal

    def exibir_dados(self):
        return f"Usuário: {self.usuario}, Valor mensal: {self.valor_mensal}"

    @abstractmethod
    def calcular_fatura(self):
        pass


class AssinaturaFamilia(Assinatura):
    def __init__(self, usuario, valor_mensal, quantidade_membros):
        super().__init__(usuario, valor_mensal)
        self.quantidade_membros = quantidade_membros

    @registrar_fatura
    def calcular_fatura(self):
        total = self.valor_mensal + (self.quantidade_membros - 1) * 15
        if self.quantidade_membros >= 5:
            total = total * 0.80
        return total


class AssinaturaEstudante(Assinatura):
    def __init__(self, usuario, valor_mensal, possui_comprovante):
        super().__init__(usuario, valor_mensal)
        self.possui_comprovante = possui_comprovante

    @registrar_fatura
    def calcular_fatura(self):
        if self.possui_comprovante:
            return self.valor_mensal * 0.5
        return self.valor_mensal


assinatura_estudante_1 = AssinaturaEstudante("Felipe", 29.99, True)
print(assinatura_estudante_1.exibir_dados())
print(assinatura_estudante_1.calcular_fatura())
