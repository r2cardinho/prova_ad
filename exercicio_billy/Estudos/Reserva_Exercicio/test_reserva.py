import pytest
from reserva import Reserva, ReservaHotel, ReservaCarro


def test_reserva_hotel_sem_desconto():
    reserva = ReservaHotel("Ana", 200, 3)
    resultado = reserva.calcular_total()
    assert resultado == 600  # 200 * 3, sem desconto


def test_reserva_hotel_com_desconto():
    reserva = ReservaHotel("Ana", 200, 10)
    resultado = reserva.calcular_total()
    assert resultado == pytest.approx(1800)  # (200*10) * 0.90 = 1800


def test_reserva_carro_com_desconto():
    reserva = ReservaCarro("Pedro", 100, 6)
    resultado = reserva.calcular_total()
    assert resultado == pytest.approx(510)  # (100*6) * 0.85 = 510


def test_nao_pode_instanciar_reserva():
    with pytest.raises(TypeError):
        Reserva("Ana", 200)

#Crie um decorator @registrar_calculo_reserva que exiba "Calculando valor da reserva..." antes e "Valor calculado" depois, permitindo argumentos variados. Aplique-o em calcular_total() nas duas subclasses.

#Utilizando Pytest, teste:

#1 ReservaHotel com poucas noites (sem desconto).
#2 ReservaHotel com mais de 7 noites (com desconto de 10%).
#3 ReservaCarro com mais de 5 dias (com desconto de 15%).
#4 Se não é possível instanciar Reserva diretamente.