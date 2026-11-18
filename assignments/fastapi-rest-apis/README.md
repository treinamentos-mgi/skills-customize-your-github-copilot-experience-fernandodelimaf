# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para um catálogo de livros usando FastAPI, praticando rotas HTTP, validação de dados com Pydantic e operações CRUD.

## 📝 Tarefas

### 🛠️ Criar a API e as Rotas de Leitura e Criação

#### Descrição
Instale as dependências do arquivo `requirements.txt`, execute a aplicação inicial e implemente os endpoints para listar e cadastrar livros. A API deve manter os dados em memória durante a execução.

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Requisitos
O programa concluído deve:

- Iniciar uma aplicação FastAPI chamada `app`.
- Implementar `GET /books` para retornar todos os livros, começando com uma lista vazia.
- Implementar `POST /books` para cadastrar um livro com título e autor.
- Gerar um identificador para cada livro criado e retornar o novo recurso com status HTTP `201`.

### 🛠️ Implementar Consulta, Atualização e Exclusão

#### Descrição
Adicione endpoints para consultar, atualizar e excluir um livro pelo identificador, usando os métodos HTTP apropriados.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` para retornar um livro específico.
- Implementar `PUT /books/{book_id}` para substituir o título e o autor de um livro.
- Implementar `DELETE /books/{book_id}` para excluir um livro e retornar status HTTP `204`.
- Retornar status HTTP `404` quando o identificador solicitado não existir.

### 🛠️ Validar e Explorar a API

#### Descrição
Use a documentação interativa do FastAPI para testar as rotas e confira como a API responde a dados válidos e inválidos.

#### Requisitos
O programa concluído deve:

- Definir os dados de entrada e saída usando modelos Pydantic.
- Recusar título ou autor vazio com um erro de validação HTTP `422`.
- Permitir testar todos os endpoints em `http://127.0.0.1:8000/docs`.
