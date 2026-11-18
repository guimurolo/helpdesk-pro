from database.connection import conectar


def criar_tabela():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS chamados (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(150) NOT NULL,
                    descricao TEXT NOT NULL,
                    prioridade VARCHAR(10) NOT NULL
                        CHECK (prioridade IN ('Baixa', 'Média', 'Alta')),
                    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

    print("Tabela chamados criada com sucesso!")


if __name__ == "__main__":
    criar_tabela()