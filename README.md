# Atividade Prática - Conexão com Banco de Dados (Northwind)

## Descrição
Este repositório contém a implementação da atividade prática para a disciplina de Banco de Dados II. O objetivo desta atividade é praticar os conceitos de conexão com banco de dados e mapeamento objeto-relacional (ORM) utilizando Python. A atividade é dividida em duas partes principais:

1. **Implementação de uma aplicação para inserir um novo pedido no banco de dados Northwind**:
    - Primeiramente, utilizando o driver de conexão `psycopg2`.
    - Posteriormente, adaptando a mesma aplicação para utilizar o ORM `SqlAlchemy`.

2. **Implementação de dois relatórios na aplicação**:
    - Um relatório com informações completas sobre um pedido específico.
    - Um relatório com o ranking dos funcionários por intervalo de tempo, baseado no total de pedidos realizados e na soma dos valores vendidos.
  
## Estrutura do Projeto

A estrutura do projeto segue o padrão MVC (Model-View-Controller) e DAO (Data Access Object):


Claro, aqui está a descrição em código Markdown:

markdown
Copiar código
# Atividade Prática - Conexão com Banco de Dados (Northwind)

## Descrição

Este repositório contém a implementação da atividade prática para a disciplina de Banco de Dados II, ministrada pela Profa. Vanessa Souza. O objetivo desta atividade é praticar os conceitos de conexão com banco de dados e mapeamento objeto-relacional (ORM) utilizando Python. A atividade é dividida em duas partes principais:

1. **Implementação de uma aplicação para inserir um novo pedido no banco de dados Northwind**:
    - Primeiramente, utilizando o driver de conexão `psycopg2`.
    - Posteriormente, adaptando a mesma aplicação para utilizar o ORM `SqlAlchemy`.

2. **Implementação de dois relatórios na aplicação**:
    - Um relatório com informações completas sobre um pedido específico.
    - Um relatório com o ranking dos funcionários por intervalo de tempo, baseado no total de pedidos realizados e na soma dos valores vendidos.

## Estrutura do Projeto

A estrutura do projeto segue o padrão MVC (Model-View-Controller) e DAO (Data Access Object):

project
│
├── models
│ ├── init.py
│ ├── base.py
│ ├── northwind_models.py
│
├── dao
│ ├── init.py
│ ├── base_dao.py
│ ├── customer_dao.py
│ ├── employee_dao.py
│ ├── order_dao.py
│ ├── order_details_dao.py
│ ├── product_dao.py
│
├── views
│ ├── init.py
│ ├── input_view.py
│ ├── output_view.py
│
├── controllers
│ ├── init.py
│ ├── order_controller.py
│
├── main_psycopg.py
├── main_sqlalchemy.py
└── requirements.txt

## Implementações

### Implementação com `psycopg2`
A aplicação `main_psycopg.py` realiza a inserção de pedidos no banco de dados Northwind utilizando o driver de conexão `psycopg2`. A arquitetura MVC e DAO é usada para separar as responsabilidades, tornando o código mais modular e de fácil manutenção.

### Implementação com `SqlAlchemy`
A aplicação `main_sqlalchemy.py` adapta a implementação anterior para utilizar `SqlAlchemy` como ORM. Isso simplifica a interação com o banco de dados, aproveitando os benefícios do mapeamento objeto-relacional.

### Relatórios
Dois relatórios são gerados pela aplicação:
- **Relatório de Pedido**: Inclui número do pedido, data do pedido, nome do cliente, nome do vendedor e itens do pedido (produto, quantidade e preço).
- **Relatório de Ranking de Funcionários**: Lista os funcionários com o total de pedidos realizados e a soma dos valores vendidos em um intervalo de tempo especificado.

## Como Executar

### Pré-requisitos

- Python 3.8+
- PostgreSQL
- Bibliotecas Python: `psycopg2-binary`, `sqlalchemy`, `sqlacodegen`


### Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/AndreMarcos/Notrhwind.git
    cd Notrhwind
    ```
2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure as credenciais de acesso ao banco de dados no arquivo `db_config.py`.

### Execução

- Para executar a aplicação com `psycopg2`:
    ```bash
    python main_psycopg.py
    ```

- Para executar a aplicação com `SqlAlchemy`:
    ```bash
    python main_sqlalchemy.py
    ```


