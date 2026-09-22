from abc import ABC,abstractmethod

PI = 3.14

class Forma(ABC):
    def descrever(self):
        return f"Área: {self.area()}"

    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return PI * self.raio * self.raio

print(Quadrado(4).area())
print(Quadrado(4).descrever())
print(Circulo(2).area())