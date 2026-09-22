from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    def resumo(self):                 # método concreto (pronto)
        return f"Pagamento de R$ {self.valor:.2f}"

    @abstractmethod
    def processar(self):              # método abstrato (obrigação)
        pass

class Pix(Pagamento):
    def processar(self):
        return f"Pix de R$ {self.valor:.2f} aprovado"

class Cartao(Pagamento):
    def processar(self):
        return f"Cartão de R$ {self.valor:.2f} aprovado"

for valor in [Pix (100), Cartao(200)]:
    print(valor.processar())

  