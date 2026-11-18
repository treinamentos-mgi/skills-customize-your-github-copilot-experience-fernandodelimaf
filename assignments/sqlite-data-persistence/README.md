# 📘 Atividade: Persistência de Dados com SQLite

## 🎯 Objetivo

Use o módulo `sqlite3` do Python para armazenar e gerenciar um catálogo de livros em um banco local. Pratique criação de tabelas, comandos SQL parametrizados e operações CRUD, verificando que os dados continuam disponíveis após o programa ser encerrado.

## 📝 Tarefas

### 🛠️ Criar o Banco e a Tabela de Livros

#### Descrição
Implemente a inicialização do banco SQLite e crie uma tabela para armazenar livros. Use o caminho `books.db` no mesmo diretório do programa para que os dados não dependam da pasta de execução.

#### Requisitos
O programa concluído deve:

- Conectar ao banco `books.db` usando o módulo `sqlite3`.
- Criar uma tabela `books` caso ela ainda não exista.
- Definir `id` como chave primária autoincrementada e exigir valores para `title` e `author`.
- Fechar corretamente a conexão com o banco após a inicialização.

### 🛠️ Implementar Operações CRUD

#### Descrição
Implemente funções para adicionar, listar, atualizar e remover livros. Use parâmetros nas consultas SQL em vez de montar comandos concatenando os valores recebidos.

#### Requisitos
O programa concluído deve:

- Adicionar um livro e retornar o identificador gerado pelo banco.
- Listar os livros em ordem crescente de identificador.
- Atualizar o título e o autor de um livro a partir do seu identificador.
- Excluir um livro a partir do seu identificador.
- Informar se uma atualização ou exclusão encontrou o livro solicitado.

### 🛠️ Confirmar a Persistência dos Dados

#### Descrição
Execute as operações do programa e confira o conteúdo do banco antes e depois de encerrar e iniciar o programa novamente.

#### Requisitos
O programa concluído deve:

- Permitir adicionar pelo menos dois livros e listar seus dados e identificadores.
- Manter os livros cadastrados após o programa ser encerrado e executado novamente.
- Lidar com uma tentativa de atualizar ou excluir um identificador inexistente sem encerrar o programa com erro.
