from abc import ABC, abstractmethod
from functools import wraps


def registrar_calculo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando cálculo...")
        resultado = func(*args, **kwargs)
        print("Cálculo finalizado!")
        return resultado

    return wrapper


class Carro(ABC):

    def __init__(self, modelo, preco, *args, **kwargs):
        self.modelo = modelo
        self.preco = preco
        self.extras = args
        self.informacoes = kwargs

    def exibir_dados(self):
       return f"Modelo: {self.modelo} | Preço: R$ {self.preco:.2f} | Desconto: {self.desconto}% | Extras: {self.extras} | Informações: {self.informacoes}"

    @abstractmethod
    def calcular_preco_final(self):
        pass


class CarroPopular(Carro):

    def __init__(self, modelo, preco, desconto, *args, **kwargs):
        super().__init__(modelo, preco, *args, **kwargs)

        self.desconto = desconto

    def calcular_desconto(self):
        return self.preco * self.desconto / 100

    @registrar_calculo
    def calcular_preco_final(self):
        preco_final = self.preco - self.calcular_desconto()
        return preco_final


class CarroLuxo(Carro):

    def __init__(self, modelo, preco, imposto, *args, **kwargs):
        super().__init__(modelo, preco, *args, **kwargs)

        self.imposto = imposto

    def calcular_imposto(self):
        return self.preco * self.imposto / 100

    @registrar_calculo
    def calcular_preco_final(self):
        preco_final = self.preco + self.calcular_imposto()
        return preco_final


class CarroEletrico(Carro):

    def __init__(self, modelo, preco, desconto, *args, **kwargs):
        super().__init__(modelo, preco, *args, **kwargs)

        self.desconto = desconto

    def calcular_desconto(self):
        return self.preco * self.desconto / 100

    @registrar_calculo
    def calcular_preco_final(self):
        preco_final = self.preco - self.calcular_desconto()
        return preco_final


carro_1=CarroPopular("Fusca", 20000, 10, "Ar condicionado", "Vidros funcionando", cor ="Amarelo", ano= "1998")
print(carro_1.exibir_dados())
print(f"Preço final: R$ {carro_1.calcular_preco_final():.2f}")