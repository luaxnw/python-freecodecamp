# 📘 Exercício Integrador

## 🎯 Objetivo

Crie um programa que receba os nomes dos alunos e suas respectivas notas.

### 📥 Exemplo de entrada

```text
Maria 8
João 6
Ana 10
Pedro 7
```

## 📋 Requisitos

Armazene os dados em um **dicionário**, onde:

- A chave será o nome do aluno.
- O valor será a nota.

Ao final, exiba:

- ✅ Maior nota
- ✅ Menor nota
- ✅ Média das notas
- ✅ Nome do aluno com a maior nota

---

# 📚 Mini Projeto — Sistema de Biblioteca

## 🎯 Objetivo

Desenvolver um pequeno sistema para gerenciar uma biblioteca utilizando as quatro principais estruturas de dados do Python:

- 📋 Lista (`list`)
- 📖 Dicionário (`dict`)
- 🏷️ Conjunto (`set`)
- 📌 Tupla (`tuple`)

---

# 🏗️ Estrutura dos Dados

Cada livro será representado por um **dicionário**.

```python
{
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "categorias": {"Romance", "Literatura Brasileira"}
}
```

Todos os livros serão armazenados em uma **lista**.

```python
biblioteca = []
```

---

# 🖥️ Menu Principal

```text
1 - Cadastrar livro
2 - Listar livros
3 - Buscar por autor
4 - Mostrar categorias existentes
5 - Remover livro
6 - Estatísticas
0 - Sair
```

---

# ⚙️ Funcionalidades

## 1️⃣ Cadastrar livro

Solicitar ao usuário:

- Título
- Autor
- Ano de publicação
- Categorias (separadas por vírgula)

> **Observação:** As categorias devem ser armazenadas utilizando um **conjunto (`set`)**.

---

## 2️⃣ Listar livros

Exibir todos os livros cadastrados na biblioteca.

---

## 3️⃣ Buscar por autor

Solicitar o nome de um autor e exibir apenas os livros pertencentes a ele.

---

## 4️⃣ Mostrar categorias existentes

Percorrer todos os livros e montar um único conjunto contendo todas as categorias cadastradas, sem repetição.

### Exemplo de saída

```text
Romance
Terror
Ficção
História
Fantasia
```

---

## 5️⃣ Remover livro

Remover um livro da biblioteca utilizando seu **título**.

---

## 6️⃣ Estatísticas

Exibir as seguintes informações:

- 📚 Quantidade total de livros
- ✍️ Quantidade de autores diferentes
- 📖 Livro mais antigo
- 🚀 Livro mais recente

> **Observação:** Utilize uma **tupla** para representar o livro mais antigo e o mais recente.

Exemplo:

```python
("Dom Casmurro", 1899)
```

---

# ⭐ Desafio Extra

Implemente também as seguintes melhorias:

- 🔍 Pesquisa por categoria
- 📅 Ordenação dos livros por ano
- 🔤 Ordenação dos livros por título
- 💾 Salvar os livros em um arquivo `.txt` ou `.json`
- 📂 Carregar automaticamente os livros ao iniciar o programa
- 🚫 Impedir o cadastro de livros duplicados (mesmo título e autor)
- 📊 Mostrar a quantidade de livros cadastrados por autor

---

# 💡 Resumo Teórico

Este projeto reúne as quatro principais estruturas de dados do Python em um contexto prático.

| Estrutura | Utilização |
|-----------|------------|
| 📋 **Lista (`list`)** | Armazenar e gerenciar todos os livros da biblioteca. |
| 📖 **Dicionário (`dict`)** | Representar cada livro com seus atributos (título, autor, ano e categorias). |
| 🏷️ **Conjunto (`set`)** | Armazenar categorias sem permitir duplicidades. |
| 📌 **Tupla (`tuple`)** | Representar informações imutáveis, como o livro mais antigo e o mais recente. |

---

## 🎯 Objetivos de Aprendizagem

Ao concluir este projeto, você será capaz de:

- Utilizar listas para armazenar coleções de objetos.
- Trabalhar com dicionários para organizar dados estruturados.
- Utilizar conjuntos para eliminar duplicidades.
- Empregar tuplas para representar dados imutáveis.
- Criar menus interativos.
- Manipular arquivos (`.txt` ou `.json`).
- Desenvolver um sistema completo utilizando apenas estruturas fundamentais da linguagem Python.