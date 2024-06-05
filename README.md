## Desafio API TDD com FastAPI

### Visão Geral

Este projeto é um desafio da DIO do bootcamp Python AI Backend Developer, conforme o repositório: https://github.com/digitalinnovationone/store_api

Trata-se do desenvolvimento de uma API para gerenciamento de produtos utilizando o framework FastAPI e as práticas de TDD (Desenvolvimento Orientado por Testes). 

As funcionalidades da API incluem:

* Criar produtos
* Listar produtos
* Detalhar produtos
* Atualizar produtos
* Deletar produtos

### Tecnologias Utilizadas

* **FastAPI:** Framework web Python rápido e moderno.
* **Pydantic:** Validação de dados robusta.
* **Pytest:** Ferramenta de teste para garantir a qualidade do código.
* **MongoDB:** Banco de dados NoSQL para armazenamento de dados.
* **Uvicorn:** Servidor ASGI para executar a aplicação FastAPI.

### Funcionalidades da API

**Criar Produto:**

* **Endpoint:** `/products/`
* **Método:** `POST`
* **Request Body:**
    ```json
    {
        "name": "Nome do Produto",
        "quantity": 10,
        "price": 100.0,
        "status": "disponível"
    }
    ```
* **Respostas:**
    * 201 Created: Produto criado com sucesso.
    * 422 Unprocessable Entity: Dados inválidos.

**Listar Produtos:**

* **Endpoint:** `/products/`
* **Método:** `GET`
* **Respostas:**
    * 200 OK: Retorna a lista de produtos.

**Detalhar Produto:**

* **Endpoint:** `/products/{id}`
* **Método:** `GET`
* **Parâmetros de Rota:**
    * `id`: ID do produto.
* **Respostas:**
    * 200 OK: Retorna os detalhes do produto.
    * 404 Not Found: Produto não encontrado.

**Atualizar Produto:**

* **Endpoint:** `/products/{id}`
* **Método:** `PUT`
* **Parâmetros de Rota:**
    * `id`: ID do produto.
* **Request Body:**
    ```json
    {
        "name": "Nome Atualizado",
        "quantity": 20,
        "price": 150.0,
        "status": "indisponível"
    }
    ```
* **Respostas:**
    * 200 OK: Produto atualizado com sucesso.
    * 404 Not Found: Produto não encontrado.
    * 422 Unprocessable Entity: Dados inválidos.

**Deletar Produto:**

* **Endpoint:** `/products/{id}`
* **Método:** `DELETE`
* **Parâmetros de Rota:**
    * `id`: ID do produto.
* **Respostas:**
    * 204 No Content: Produto deletado com sucesso.
    * 404 Not Found: Produto não encontrado.

### Como Executar o Projeto

**Pré-requisitos:**

* Python 3.7+
* MongoDB

**Passos para Executar:**

1. Clone o repositório:

```bash
git clone https://github.com/gui-brito14/python_desafio_dio_API_TDD.git
cd python_desafio_dio_API_TDD
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

5. Acesse a documentação interativa da API:

Abra o navegador e vá para http://localhost:8000/docs

**Executar Testes:**

Para executar os testes, utilize o comando:

```bash
pytest
```

### Contribuição

Sinta-se à vontade para contribuir com este projeto. Você pode abrir issues e enviar pull requests.
