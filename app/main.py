
from fastapi import FastAPI

from app.chamado import Chamado


app = FastAPI(
    title="HelpDesk Pro",
    description="Sistema de gerenciamento de chamados",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo ao HelpDesk Pro!",
        "status": "online"
    }

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