import pytest
from main import Relatorio, RelatorioCSV, RelatorioTXT

LINHAS = ["Ana", "Bruno", "Carla"]


def test_csv_gera_separado_por_virgula():
    assert RelatorioCSV("Clientes", LINHAS).gerar() == "Ana, Bruno, Carla"


def test_texto_gera_com_quebra_de_linha():
    assert RelatorioTXT("Clientes", LINHAS).gerar() == "Ana\nBruno\nCarla"


def test_resumo_mostra_titulo_e_quantidade():
    assert RelatorioCSV("Clientes", LINHAS).resumo() == "Clientes - 3 linhas"


def test_nao_instancia_relatorio_abstrato():
    with pytest.raises(TypeError):
        Relatorio("Clientes", LINHAS)