#Exercício 11 - Agenda
#Crie um dicionário onde
#chave = nome / valor = telefone
#Permita cadastrar 5 contatos.
#Depois peça um nome e informe o telefone.

lista_telefonica = {}
nome = None
telefone = None

for i in range(5):
    nome = str(input("Informe o nome do contato: "))
    telefone = str(input("Informe o telefone do contato: "))
    lista_telefonica[nome] = telefone
    
nome_pesquisa = str(input("Informe um nome para pesquisar na lista: "))

if nome_pesquisa in lista_telefonica.keys():
    print(f"Telefone de {nome_pesquisa}: {lista_telefonica[nome_pesquisa]}")
else:
    print("Nome não está presente na lista.")

