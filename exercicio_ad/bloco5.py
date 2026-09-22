from functools import wraps

def avisar(func):
    def wrapper():
        print("Começou")
        func()
        print("Terminou")
    return wrapper


@avisar
def tarefa():
    print("Rodando a Tarefa")


tarefa()

def registrar(funcao):
    @wraps(funcao)                 # copia a identidade da função original
    def wrapper(*args, **kwargs):
        print(f"Executando {funcao.__name__}")
        return funcao(*args, **kwargs)
    return wrapper

@registrar
def somar(a, b):
    return a + b

@registrar
def saudar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

print(somar(2, 3))
print(saudar("Ana", saudacao="Oi"))