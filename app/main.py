
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.chamado import Chamado
from database.chamados_repository import criar_chamado, listar_chamados

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="HelpDesk Pro",
    description="Sistema de gerenciamento de chamados",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/chamados")
def listar_chamados_api():
    chamados = listar_chamados()

    return [
        {
            "id": chamado[0],
            "titulo": chamado[1],
            "descricao": chamado[2],
            "prioridade": chamado[3],
            "criado_em": chamado[4]
        }
        for chamado in chamados
    ]


@app.post("/chamados")
def cadastrar_chamado(chamado: Chamado):
    resultado = criar_chamado(
        chamado.titulo,
        chamado.descricao,
        chamado.prioridade
    )

    return {
        "mensagem": "Chamado criado com sucesso!",
        "chamado": {
            "id": resultado[0],
            "titulo": resultado[1],
            "descricao": resultado[2],
            "prioridade": resultado[3],
            "criado_em": resultado[4]
        }
    }


@app.get("/sobre")
def sobre():
    return {
        "projeto": "HelpDesk Pro",
        "objetivo": "Gerenciamento de chamados",
        "responsavel": "Guilherme"
    }
