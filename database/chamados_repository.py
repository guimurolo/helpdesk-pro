
from database.connection import conectar


def criar_chamado(titulo, descricao, prioridade):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO chamados (titulo, descricao, prioridade)
                VALUES (%s, %s, %s)
                RETURNING id, titulo, descricao, prioridade, criado_em;
                """,
                (titulo, descricao, prioridade)
            )

            chamado = cursor.fetchone()

    return chamado


def listar_chamados():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id, titulo, descricao, prioridade, criado_em
                FROM chamados
                ORDER BY id DESC;
            """)

            chamados = cursor.fetchall()

    return chamados
