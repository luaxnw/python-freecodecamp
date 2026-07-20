Aqui está uma sequência de exercícios em ordem crescente de dificuldade para praticar listas, tuplas, conjuntos e dicionários em Python, seguida de um mini projeto que utiliza todas essas estruturas.

Exercícios com Listas
Exercício 1 - Soma dos números

Crie uma lista com 10 números inteiros e mostre:

a soma
o maior número
o menor número
a média

Exemplo

numeros = [10, 5, 8, 2, 15, 20, 7, 3, 9, 11]

Exercício 2 - Lista de compras

Crie um programa que permita ao usuário adicionar produtos até digitar "fim".

Depois mostre:

quantidade de produtos
lista em ordem alfabética
primeiro produto
último produto
Exercício 3 - Removendo duplicados

Dada a lista

[3,5,2,5,7,8,2,3,10]


Crie uma nova lista sem elementos repetidos, mantendo a ordem de aparecimento.

Exercícios com Tuplas
Exercício 4 - Cadastro

Crie uma tupla contendo:

nome
idade
profissão

Mostre cada informação separadamente.

Exercício 5 - Notas

Crie uma tupla com cinco notas.

Mostre:

maior nota
menor nota
média
Exercício 6 - Coordenadas

Crie uma lista de tuplas representando coordenadas.

[(3,5), (7,2), (8,10), (0,1)]


Mostre apenas os pontos cuja soma das coordenadas seja maior que 10.

Exercícios com Conjuntos (Sets)
Exercício 7 - Alunos

Considere

python = {"Ana", "Carlos", "Pedro", "Lucas"}

java = {"Pedro", "Lucas", "Marina", "João"}


Mostre:

alunos dos dois cursos
alunos apenas de Python
alunos apenas de Java
todos os alunos
Exercício 8 - Letras únicas

Peça uma frase ao usuário.

Mostre:

conjunto das letras utilizadas
quantidade de letras diferentes
Exercício 9 - Números repetidos

Leia 15 números.

Mostre apenas os números únicos utilizando conjuntos.

Exercícios com Dicionários
Exercício 10 - Cadastro de Pessoa

Crie um dicionário contendo

{
    "nome": "...",
    "idade": ...,
    "cidade": "...",
    "profissao": "..."
}


Mostre todas as informações.

Exercício 11 - Agenda

Crie um dicionário onde

chave = nome
valor = telefone

Permita cadastrar 5 contatos.

Depois peça um nome e informe o telefone.

Exercício 12 - Contador de palavras

Leia uma frase.

Conte quantas vezes cada palavra aparece.

Exemplo:

Entrada

python é legal python é poderoso


Saída

python -> 2
é -> 2
legal -> 1
poderoso -> 1

Exercício Integrador

Crie um programa que receba nomes de alunos e suas notas.

Exemplo:

Maria 8
João 6
Ana 10
Pedro 7


Armazene em um dicionário.

Depois mostre:

maior nota
menor nota
média
aluno com maior nota
Mini Projeto — Sistema de Biblioteca 📚
Objetivo

Criar um pequeno sistema para controlar livros.

Você deverá utilizar:

Lista
Dicionário
Conjunto
Tupla
Estrutura

Cada livro será um dicionário.

Exemplo

{
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano": 1899,
    "categorias": {"Romance", "Literatura Brasileira"}
}


Todos os livros ficarão dentro de uma lista.

biblioteca = []

Menu
1 - Cadastrar livro

2 - Listar livros

3 - Buscar por autor

4 - Mostrar categorias existentes

5 - Remover livro

6 - Estatísticas

0 - Sair

Funcionalidades
1. Cadastrar livro

Cadastrar:

título
autor
ano
categorias (separadas por vírgula)

As categorias devem ser armazenadas como um conjunto (set).

2. Listar livros

Exibir todos os livros cadastrados.

3. Buscar por autor

Mostrar apenas os livros daquele autor.

4. Mostrar categorias

Percorrer todos os livros e montar um conjunto com todas as categorias cadastradas.

Exemplo

Romance

Terror

Ficção

História

Fantasia

5. Remover livro

Remover pelo título.

6. Estatísticas

Mostrar:

quantidade de livros
autores diferentes
livro mais antigo
livro mais recente

Utilize uma tupla para representar o livro mais antigo e o mais recente no formato:

("Dom Casmurro", 1899)

Desafio Extra ⭐

Implemente também:

pesquisa por categoria;
ordenação dos livros por ano;
ordenação dos livros por título;
salvar os livros em um arquivo .txt ou .json;
carregar os livros ao iniciar o programa;
impedir o cadastro de livros com o mesmo título e autor;
mostrar a quantidade de livros por autor.

Esse mini projeto reúne as quatro estruturas de dados em um contexto prático:

Lista para armazenar todos os livros.
Dicionário para representar os dados de cada livro.
Conjunto para gerenciar categorias sem repetição.
Tupla para representar resultados imutáveis, como o livro mais antigo e o mais recente.
