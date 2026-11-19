import pytest

from database.chamados_repository import criar_chamado, listar_chamados 
from database.connection import conectar


pytestmark = pytest.mark.integration

@pytest.fixture
def chamado_de_teste():
    chamado = criar_chamado(
        "Teste de integração",
        "Validando persistência no PostgreSQL",
        "Alta"
    )

    yield chamado

    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                "DELETE FROM chamados WHERE id = %s",
                (chamado[0],)
            )

def test_criar_chamado_no_banco(chamado_de_teste):
    assert chamado_de_teste[0] is not None
    assert chamado_de_teste[1] == "Teste de integração"
    assert chamado_de_teste[2] == "Validando persistência no PostgreSQL"
    assert chamado_de_teste[3] == "Alta"

def test_listar_chamados_do_banco(chamado_de_teste):
    chamados = listar_chamados()

    assert any(
        chamado[0] == chamado_de_teste[0]
        for chamado in chamados
    )