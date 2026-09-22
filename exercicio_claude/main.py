from abc import abstractmethod, ABC
from functools import wraps


# Classe abstrata Relatorio com titulo e linhas (uma lista), método concreto resumo() retornando "<titulo> — <quantidade> linhas" e método abstrato gerar().
# RelatorioCSV: gerar() retorna as linhas separadas por vírgula.
# RelatorioTexto: gerar() retorna as linhas separadas por quebra de linha.
# Decorator @registrar_geracao: imprime "Gerando relatório" antes e "Relatório pronto" depois, aplicado ao gerar() das duas classes concretas.
# Quatro testes com Pytest.




def registrar_geracao(func):
    def wrapper(*args, **kwargs):
        print("Gerando Relatório")
        resultado = func(*args, **kwargs)
        print("Relatório Gerado")

        return resultado
    return wrapper


class Relatorio(ABC):
    def __init__(self, titulo, linhas):
        self.titulo = titulo
        self.linhas = linhas


    def resumo(self):
        return f"{self.titulo} - {len(self.linhas)} linhas"

    @abstractmethod
    def gerar(self):
        pass

class RelatorioCSV(Relatorio):

    @registrar_geracao
    def gerar(self):
        return ", ".join(self.linhas)

class RelatorioTXT(Relatorio):

    @registrar_geracao
    def gerar(self):
        return "\n".join(self.linhas)


linhas = ["Ana", "Bruno", "Carla"]
csv = RelatorioCSV("Clientes", linhas)
txt = RelatorioTXT("Clientes", linhas)

print(csv.resumo())
print(csv.gerar())
print(txt.gerar())