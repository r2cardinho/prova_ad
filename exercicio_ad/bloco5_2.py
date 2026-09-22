class Pedido():
    def __init__(self, Cliente, Valor):
        self.Cliente = Cliente
        self.Valor = Valor

    def registrar(funcao):
        def wrapper(*args, **kwargs):
            print(f"Executando {funcao.__name__}")
            return funcao(*args, **kwargs)
        return wrapper


    @registrar
    def finalizar(self):
        return f"Pedido de {self.Cliente} com preço {self.Valor} finalizado"


print(Pedido("Ricardo", 250).finalizar())