# conta.py
from abc import ABC, abstractmethod
from functools import wraps

def registrar_abertura(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando abertura de conta")
        resultado = func(*args, **kwargs)
        print("Abertura finalizada")
        return resultado
    return wrapper


class Conta(ABC):
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta

    def exibir_dados(self):
        return f"Titular: {self.titular}, Número da conta: {self.numero_conta}"

    @abstractmethod
    def abrir_conta(self):
        pass


class ContaCorrente(Conta):
    @registrar_abertura
    def abrir_conta(self):
        return f"Conta corrente {self.numero_conta} aberta para {self.titular}"


class ContaPoupanca(Conta):
    @registrar_abertura
    def abrir_conta(self):
        return (f"Conta poupança {self.numero_conta} aberta para {self.titular}")




#Exercício B — Sistema de Contas Bancárias

#Um banco deseja desenvolver um sistema para gerenciar diferentes tipos de conta.
#Crie uma classe abstrata chamada Conta, contendo:

#os atributos titular e numero_conta;
#um construtor para inicializar os atributos;
#um método concreto exibir_dados(), que retorna o titular e o número da conta cadastrados;
#um método abstrato abrir_conta(), responsável por confirmar a abertura da conta.

#Em seguida, crie duas classes que herdam de Conta:

#ContaCorrente: o método abrir_conta() deverá retornar a mensagem "Conta corrente <numero_conta> aberta para <titular>";
#ContaPoupanca: o método abrir_conta() deverá retornar a mensagem "Conta poupança <numero_conta> aberta para <titular>".

#Crie também um decorator chamado @registrar_abertura. Esse decorator deverá exibir a mensagem "Iniciando abertura de conta" antes da execução do método e "Abertura finalizada" após sua execução. O decorator deve permitir que a função decorada receba diferentes argumentos.
#Aplique o decorator ao método abrir_conta() das classes concretas.