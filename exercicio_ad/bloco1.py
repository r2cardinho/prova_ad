class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def passou(self):
        if self.nota >= 7:
            return True
        else:
            return False


a1 = Aluno("Ana", 8.5)
a2 = Aluno("Bruno", 4.0)

print(f"{a1.nome} passou? {a1.passou()}")
print(f"{a2.nome} passou? {a2.passou()}")

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return self.saldo
        else:
            return ("Saldo Insuficiente!")
        


c = Conta("Rigui", 100)
print(c.depositar(50))
print(c.sacar(30))
print(c.sacar(500))
print(c.saldo)