# curso.py
from abc import ABC, abstractmethod
from functools import wraps

def registrar_matricula(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Iniciando matrícula")
        resultado = func(*args, **kwargs)
        print("Matrícula finalizada")
        return resultado
    return wrapper


class Curso(ABC):
    def __init__(self, aluno, nome_curso):
        self.aluno = aluno
        self.nome_curso = nome_curso

    def exibir_dados(self):
        return f"Aluno: {self.aluno}, Curso: {self.nome_curso}"

    @abstractmethod
    def matricular(self):
        pass


class CursoPresencial(Curso):
    @registrar_matricula
    def matricular(self):
        return f"{self.aluno} matriculado presencialmente em {self.nome_curso}"


class CursoOnline(Curso):
    @registrar_matricula
    def matricular(self):
        return f"{self.aluno} matriculado online em {self.nome_curso}"

#Uma escola deseja desenvolver um sistema para gerenciar a matrícula de alunos em diferentes tipos de curso.
#Crie uma classe abstrata chamada Curso, contendo:

#os atributos aluno e nome_curso;
#um construtor para inicializar os atributos;
#um método concreto exibir_dados(), que retorna o aluno e o nome do curso cadastrados;
#um método abstrato matricular(), responsável por confirmar a matrícula do aluno.

#Em seguida, crie duas classes que herdam de Curso:

#CursoPresencial: o método matricular() deverá retornar a mensagem "<aluno> matriculado presencialmente em <nome_curso>";
#CursoOnline: o método matricular() deverá retornar a mensagem "<aluno> matriculado online em <nome_curso>".

#Crie também um decorator chamado @registrar_matricula. Esse decorator deverá exibir a mensagem "Iniciando matrícula" antes da execução do método e "Matrícula finalizada" após sua execução. O decorator deve permitir que a função decorada receba diferentes argumentos.
#Aplique o decorator ao método matricular() das classes concretas.