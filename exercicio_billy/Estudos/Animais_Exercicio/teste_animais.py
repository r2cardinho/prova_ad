from abc import ABC, abstractmethod


class Mamifero(ABC):
    def __init__(self, nome, idade, pelagem):
        self.nome = nome
        self.idade = idade
        self.pelagem = pelagem
        self.localizacao = "Brasil"

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} anos | Pelagem: {self.pelagem}")
        print(f"O animal está andando em {self.localizacao}")

    @abstractmethod
    def emitir_som(self):
        pass


class Gato(Mamifero):
    def emitir_som(self):
        print(f"{self.nome} emite o som: Miau!")

class Cachorro(Mamifero):
    def emitir_som(self):
        print(f"{self.nome} emite o som: Au Au!")


gato = Gato("Billy", 2, "Preto")
gato.exibir_dados()
gato.emitir_som()

cachorro = Cachorro("Rex", 4, "Marrom")
cachorro.exibir_dados()
cachorro.emitir_som()

         
