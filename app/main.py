from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.chamado import Chamado

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
def listar_chamados():
    return {
        "chamados": [
            {"id": 1, "titulo": "Computador não liga"},
            {"id": 2, "titulo": "Erro no sistema"}
        ]

}
@app.get("/sobre")
def sobre():
    return {
    "projeto": "HelpDesk Pro",
    "objetivo": "Gerenciamento de chamados",
    "responsavel": "Guilherme"
}

@app.post("/chamados")
def criar_chamado(chamado: Chamado):
    return {
        "mensagem": "Chamado criado com sucesso!",
        "chamado": chamado
    }