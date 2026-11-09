
from fastapi.testclient import TestClient

from app.main import app

from app.chamado import Chamado

import pytest 
from pydantic import ValidationError


client = TestClient(app)


def test_pagina_inicial():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Bem-vindo ao HelpDesk Pro!",
        "status": "online"
    }


def test_sobre_projeto():
    response = client.get("/sobre")

    assert response.status_code == 200
    assert response.json() == {
        "projeto": "HelpDesk Pro",
        "objetivo": "Gerenciamento de chamados",
        "responsavel": "Guilherme"
    }


def test_rota_inexistente():
    response = client.get("/rota-inexistente")

    assert response.status_code == 404

def test_criar_estrutura_chamado():
    chamado = Chamado(
        titulo="Erro no sistema",
        descricao="Não consigo acessar o sistema",
        prioridade="Alta"
    )

    assert chamado.titulo == "Erro no sistema"
    assert chamado.descricao == "Não consigo acessar o sistema"
    assert chamado.prioridade == "Alta"

def test_chamado_sem_titulo():
    with pytest.raises(ValidationError):
        Chamado(
            descricao="Não consigo acessar o sistema",
            prioridade="Alta"
        )

def test_cadastrar_chamado():
    response = client.post(
        "/chamados",
        json={
            "titulo": "Erro no sistema",
            "descricao": "Não consigo acessar o sistema",
            "prioridade": "Alta"
        }
    )

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Chamado criado com sucesso!"
    assert response.json()["chamado"]["titulo"] == "Erro no sistema"

def test_cadastrar_chamado_sem_titulo():
    response = client.post(
        "/chamados",
        json={
            "descricao": "Não consigo acessar o sistema",
            "prioridade": "Alta"
        }
    )

    assert response.status_code == 422

@pytest.mark.parametrize("campo_ausente", [
    "titulo",
    "descricao",
    "prioridade"
])
def test_chamado_com_campo_ausente(campo_ausente):
    dados = {
        "titulo": "Erro no sistema",
        "descricao": "Não consigo acessar",
        "prioridade": "Alta"
    }

    del dados[campo_ausente]

    with pytest.raises(ValidationError):
        Chamado(**dados)

@pytest.mark.parametrize("titulo", [
    "",
    " ",
    "   "
])

def test_chamado_com_titulo_vazio(titulo):
    with pytest.raises(ValidationError):
        Chamado(
            titulo=titulo,
            descricao="Não consigo acessar o sistema",
            prioridade="Alta"
        )