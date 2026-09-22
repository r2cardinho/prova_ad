from abc import ABC, abstractmethod
from functools import wraps

def registrar_transacao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Iniciando processamento do pagamento")
        resultado= func(*args, **kwargs)
        print(f"Processamento finalizado!")
        return resultado

    return wrapper

class Pagamento(ABC):

    def __init__(self, cliente, valor, *args, **kwargs): #os atributos cliente e valor;
        self.cliente = cliente
        self.valor= valor

    def exibir_dados(self):
        return f"(Cliente: {self.cliente}, Valor: {self.valor}"

    @abstractmethod
    def processar(self):
        pass

class PagamentoCartao(Pagamento):
    @registrar_transacao
    def processar(self):
        return(f"Pagamento de {self.valor} via Cartão, aprovado ao {self.cliente}")
    #PagamentoCartao: o método processar() deverá retornar a mensagem "Pagamento de <valor> no cartão aprovado para <cliente>

        
class PagamentoPix(Pagamento):
    @registrar_transacao
    def processar(self):
        return(f"Pagamento de {self.valor} via PIX, aprovado ao {self.cliente}")

pagamento_1=PagamentoPix("Pedro", 200)
print(pagamento_1.exibir_dados())
print(pagamento_1.processar())

pagamento_2=PagamentoCartao("Felipe", 200)
print(pagamento_2.exibir_dados())
print(pagamento_2.processar())



#Exercício 1 — Sistema de Pagamentos

#Uma empresa deseja desenvolver um sistema para processar diferentes formas de pagamento.
#Crie uma classe abstrata chamada Pagamento, contendo:

#os atributos cliente e valor;
#um construtor para inicializar os atributos;
#um método concreto exibir_dados(), que retorna o cliente e o valor cadastrado;
#um método abstrato processar(), responsável por realizar o processamento do pagamento.

#Em seguida, crie duas classes que herdam de Pagamento:

#PagamentoCartao: o método processar() deverá retornar a mensagem "Pagamento de <valor> no cartão aprovado para <cliente>";
#PagamentoPix: o método processar() deverá retornar a mensagem "Pagamento de <valor> via Pix aprovado para <cliente>".

#Crie também um decorator chamado @registrar_transacao. Esse decorator deverá exibir a mensagem "Iniciando processamento do pagamento" antes da execução do método e "Processamento finalizado" após sua execução. O decorator deve permitir que a função decorada receba diferentes argumentos.
#Aplique o decorator ao método processar() das classes concretas.


