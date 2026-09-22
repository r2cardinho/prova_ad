
from abc import ABC, abstractmethod
from functools import wraps

def registrar_calculo_reserva(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calculando valor da reserva...")
        resultado = func(*args, **kwargs)
        print("Valor calculado")
        return resultado
    return wrapper


class Reserva(ABC):
    def __init__(self, cliente, valor_diaria):
        self.cliente = cliente
        self.valor_diaria = valor_diaria

    def exibir_dados(self):
        return f"Cliente: {self.cliente}, Valor da diária: {self.valor_diaria}"

    @abstractmethod
    def calcular_total(self):
        pass


class ReservaHotel(Reserva):
    def __init__(self, cliente, valor_diaria, quantidade_noites):
        super().__init__(cliente, valor_diaria)
        self.quantidade_noites = quantidade_noites

    @registrar_calculo_reserva
    def calcular_total(self):
        total = self.valor_diaria * self.quantidade_noites
        if self.quantidade_noites > 7:
            total = total * 0.90
        return total


class ReservaCarro(Reserva):
    def __init__(self, cliente, valor_diaria, quantidade_dias):
        super().__init__(cliente, valor_diaria)
        self.quantidade_dias = quantidade_dias

    @registrar_calculo_reserva
    def calcular_total(self):
        total = self.valor_diaria * self.quantidade_dias
        if self.quantidade_dias > 5:
            total = total * 0.85
        return total


reserva_hotel_1=ReservaHotel("Felipe", 203, 4)
print(reserva_hotel_1.exibir_dados())
print(reserva_hotel_1.calcular_total())

reserva_carro_1=ReservaCarro("Felipe", 300, 6)
print(reserva_carro_1.exibir_dados())
print(reserva_carro_1.calcular_total())

#Uma agência de viagens deseja calcular o valor final de diferentes tipos de reserva.

#Crie uma classe abstrata Reserva, contendo:

#os atributos cliente e valor_diaria;
#um construtor para inicializar os atributos;
#um método concreto exibir_dados(), que retorna o cliente e o valor da diária cadastrados;
#um método abstrato calcular_total(), responsável por calcular o valor final da reserva.

#Crie duas subclasses, cada uma com um atributo próprio adicional (usando super().__init__()):

#ReservaHotel: possui também o atributo quantidade_noites. calcular_total() deve retornar valor_diaria * quantidade_noites, mas se quantidade_noites for maior que 7, aplique 10% de desconto sobre o total.
#ReservaCarro: possui também o atributo quantidade_dias. calcular_total() deve retornar valor_diaria * quantidade_dias, mas se quantidade_dias for maior que 5, aplique 15% de desconto sobre o total.

#Crie um decorator @registrar_calculo_reserva que exiba "Calculando valor da reserva..." antes e "Valor calculado" depois, permitindo argumentos variados. Aplique-o em calcular_total() nas duas subclasses.