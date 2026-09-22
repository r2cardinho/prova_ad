# test_curso.py
import pytest
from curso import Curso, CursoPresencial, CursoOnline


def test_curso_presencial_matricular():
    curso = CursoPresencial("Ana", "Python Avançado")
    resultado = curso.matricular()
    assert resultado == "Ana matriculado presencialmente em Python Avançado"


def test_curso_online_matricular():
    curso = CursoOnline("Pedro", "Data Science")
    resultado = curso.matricular()
    assert resultado == "Pedro matriculado online em Data Science"


def test_exibir_dados():
    curso = CursoPresencial("Ana", "Python Avançado")
    resultado = curso.exibir_dados()
    assert resultado == "Aluno: Ana, Curso: Python Avançado"


def test_nao_pode_instanciar_curso():
    with pytest.raises(TypeError):
        Curso("Ana", "Python Avançado")

#Utilizando Pytest, crie testes unitários para verificar:

#Se um curso presencial retorna corretamente a mensagem de matrícula.
#Se um curso online retorna corretamente a mensagem de matrícula.
#Se exibir_dados() retorna corretamente o aluno e o nome do curso cadastrados.
#Se não é possível criar diretamente um objeto da classe abstrata Curso, utilizando pytest.raises.