class Veiculo:
    def __init__(self, marca, rodas):
        self.marca = marca
        self.rodas = rodas

    def descrever(self):
        return f"{self.marca} tem {self.rodas} rodas"

class Carro(Veiculo):
    def descrever(self):
        return f"Carro {self.marca} tem {self.rodas} rodas"

class Moto(Veiculo):
    pass

c1 = Carro("Fiat", 4)
m1 = Moto("Honda", 2)

print(c1.descrever())
print(m1.descrever())


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"{self.nome}, {self.idade} anos"

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome,idade)
        self.curso = curso

    def apresentar(self):
        return f"{super().apresentar()}, cursa {self.curso}"

e = Estudante("Rigui", 20, "Ciência da Computação")
print(e.apresentar())
print(e.nome, e.curso)
