from pydantic import BaseModel


class Chamado(BaseModel):
    titulo: str 
    descricao: str
    prioridade: str