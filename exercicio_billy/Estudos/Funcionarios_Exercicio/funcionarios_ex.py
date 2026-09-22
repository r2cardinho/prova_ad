from abc import ABC, abstractmethod
from functools import wraps


# DECORATOR
def registrar_pagamento(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando cálculo do salário...")
        resultado = func(*args, **kwargs)
        print("Cálculo finalizado!")
        return resultado

    return wrapper


# CLASSE ABSTRATA
class Funcionario(ABC):

    def __init__(self, nome, salario, *args, **kwargs):
        self.nome = nome
        self.salario = salario
        self.extras = args
        self.informacoes = kwargs

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")

    @abstractmethod
    def calcular_salario(self):
        pass


# FUNCIONÁRIO CLT
class FuncionarioCLT(Funcionario):

    def __init__(self, nome, salario, bonus, *args, **kwargs):
        super().__init__(nome, salario, *args, **kwargs)
        self.bonus = bonus

    def calcular_bonus(self):
        return self.bonus

    @registrar_pagamento
    def calcular_salario(self):
        salario_final = self.salario + self.bonus
        return salario_final


# FUNCIONÁRIO PJ
class FuncionarioPJ(Funcionario):

    def __init__(self, nome, salario, comissao, *args, **kwargs):
        super().__init__(nome, salario, *args, **kwargs)
        self.comissao = comissao

    def calcular_bonus(self):
        return self.salario * self.comissao / 100

    @registrar_pagamento
    def calcular_salario(self):
        salario_final = self.salario + self.calcular_bonus()
        return salario_final


# ESTAGIÁRIO
class Estagiario(Funcionario):

    def __init__(self, nome, salario, vale, *args, **kwargs):
        super().__init__(nome, salario, *args, **kwargs)
        self.vale = vale

    def calcular_bonus(self):
        return self.vale

    @registrar_pagamento
    def calcular_salario(self):
        salario_final = self.salario + self.vale
        return salario_final


# CRIANDO OS OBJETOS

clt = FuncionarioCLT("Felipe",6000, 500,  "Vale alimentação", "Plano de saúde", cargo="Analista", setor="TI")

pj = FuncionarioPJ( "João",5000, 10 , "Home Office", cargo="Programador", setor="Desenvolvimento")

estagiario = Estagiario( "Carlos", 1800, 400, "Vale transporte", cargo="Estagiário", setor="TI")

# TESTANDO CLT

clt.exibir_dados()
print(f"Bônus: R$ {clt.calcular_bonus():.2f}")
print(f"Salário final: R$ {clt.calcular_salario():.2f}")

print()


# TESTANDO PJ

pj.exibir_dados()
print(f"Comissão: R$ {pj.calcular_bonus():.2f}")
print(f"Salário final: R$ {pj.calcular_salario():.2f}")

print()


# TESTANDO ESTAGIÁRIO

estagiario.exibir_dados()
print(f"Vale: R$ {estagiario.calcular_bonus():.2f}")
print(f"Salário final: R$ {estagiario.calcular_salario():.2f}")