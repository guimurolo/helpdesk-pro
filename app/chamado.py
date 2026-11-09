from pydantic import BaseModel, Field, ConfigDict


class Chamado(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    titulo: str = Field(min_length=1)
    descricao: str
    prioridade: str