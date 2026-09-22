def media(*args):
    if len(args) == 0:
        return 0
    return round(sum(args) / len(args), 2)

print(media(10, 8, 6))
print(media(7))
print(media())

def ficha(**kwargs):
    valores = []
    for chave, valor in kwargs.items():
        valores.append(f"{chave}={valor}")
    return " | ".join(valores)

print(ficha(nome = "Rigui", curso = "CC", periodo = 2))


def etiqueta(**kwargs):
    nome = kwargs["nome"]
    cidade = kwargs.get("cidade", "Cidade não informada")
    return f"Para: {nome} - {cidade}"

print(etiqueta(nome="Rigui", cidade="Bauru"))
print(etiqueta(nome="Ana"))
print(etiqueta(cidade="Marília", nome="Bruno", telefone="1499999"))