# HelpDesk Pro — Sistema de Gerenciamento de Chamados

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Tests](https://img.shields.io/badge/Tests-21%20passed-success)

[![CI](https://github.com/guimurolo/helpdesk-pro/actions/workflows/tests.yml/badge.svg)](https://github.com/guimurolo/helpdesk-pro/actions/workflows/tests.yml)

## Sobre o projeto

O **HelpDesk Pro** é uma aplicação web desenvolvida para gerenciamento de chamados, permitindo cadastrar e consultar solicitações de suporte.

O projeto foi desenvolvido como parte de uma jornada prática de aprendizado em desenvolvimento de software e Quality Assurance (QA), com foco na aplicação de boas práticas de programação, testes automatizados e integração contínua.

## Funcionalidades

- Cadastro de chamados de suporte.
- Definição de prioridade: Baixa, Média e Alta.
- Validação dos dados enviados à API.
- Persistência de informações em banco de dados PostgreSQL.
- Consulta dos chamados cadastrados.
- Interface web com HTML, CSS e JavaScript.
- Retorno de mensagens de sucesso e erro na interface.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| FastAPI | Desenvolvimento da API |
| Pydantic | Validação de dados |
| PostgreSQL | Banco de dados |
| Psycopg | Conexão com PostgreSQL |
| HTML5 e CSS3 | Estrutura e estilo da interface |
| JavaScript | Interação com a API |
| Pytest | Testes automatizados |
| Pytest-HTML | Geração de relatórios |
| Git e GitHub | Versionamento |
| GitHub Actions | Integração contínua (CI) |
| Docker | Ambiente do banco de dados |

## Estrutura do projeto

```text
helpdesk-pro/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── __init__.py
│   ├── chamado.py
│   └── main.py
├── database/
│   ├── connection.py
│   ├── init_db.py
│   └── chamados_repository.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── tests/
│   ├── integration/
│   │   └── test_chamados_repository.py
│   └── test_main.py
├── .gitignore
├── pytest.ini
└── requirements.txt
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/guimurolo/helpdesk-pro.git
cd helpdesk-pro
```

### 2. Criar e ativar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar o PostgreSQL

Com o Docker instalado, execute:

```bash
docker run --name helpdesk-postgres 
  -e POSTGRES_USER=helpdesk_user 
  -e POSTGRES_PASSWORD=helpdesk123 
  -e POSTGRES_DB=helpdesk_db 
  -p 5432:5432 
  -d postgres:16
```

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=helpdesk_db
DB_USER=helpdesk_user
DB_PASSWORD=helpdesk123
```

### 5. Criar as tabelas

```bash
python -m database.init_db
```

### 6. Iniciar a aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará disponível em:

- Interface web: http://127.0.0.1:8000
- Documentação da API: http://127.0.0.1:8000/docs

## Estratégia de testes

O projeto utiliza Pytest para execução de testes automatizados, separados por finalidade.

**Testes unitários**

Validam comportamentos isolados da aplicação, incluindo endpoints, regras e validações de dados, sem depender de uma conexão real com o PostgreSQL.

```bash
python -m pytest -m unit -v
```

**Testes de integração**

Validam a comunicação com o banco de dados PostgreSQL, incluindo operações de criação e consulta de chamados.

```bash
python -m pytest -m integration -v
```

Os testes de integração utilizam fixtures para preparar os dados necessários e realizar a limpeza após a execução.

### Resultados dos testes

| Categoria | Testes aprovados |
|---|---:|
| Unitários | 19 |
| Integração | 2 |
| **Total** | **21** |

Todos os 21 testes foram aprovados na última execução validada.

## Integração contínua (CI)

O projeto utiliza GitHub Actions para automatizar a validação a cada atualização na branch `main` ou abertura de Pull Request direcionado a ela.

O pipeline executa as seguintes etapas:

1. Checkout do código.
2. Configuração do ambiente Python.
3. Instalação das dependências.
4. Inicialização de um serviço PostgreSQL.
5. Criação das tabelas do banco de dados.
6. Execução dos testes unitários.
7. Execução dos testes de integração.
8. Geração dos relatórios HTML.
9. Publicação dos relatórios como artefatos da execução.

Os relatórios permitem consultar os resultados das execuções automatizadas diretamente no GitHub Actions.

## Objetivo de aprendizado

Este projeto tem como objetivo consolidar conhecimentos em:

- Desenvolvimento de APIs com Python e FastAPI.
- Integração com banco de dados relacionais.
- Testes unitários e de integração.
- Validação de dados e tratamento de respostas.
- Organização e manutenção de projetos.
- Versionamento com Git.
- Automação de testes com GitHub Actions.
- Práticas de Quality Assurance e integração contínua.

## Autor

**Guilherme Murolo**

Projeto desenvolvido para fins de aprendizado e construção de portfólio profissional na área de tecnologia, com direcionamento para Quality Assurance (QA) e Testes de Software.

[GitHub — guimurolo](https://github.com/guimurolo)