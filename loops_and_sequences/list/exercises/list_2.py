#Exercício 2 - Lista de compras

#Crie um programa que permita ao usuário adicionar produtos até digitar "fim".

#Depois mostre:

#quantidade de produtos lista em ordem alfabética primeiro produto último produto

list = []


while True:
    element = str(input("Insira um produto ou ""fim"" para encerrar: "))
    
    if element == "fim":
        break

    list.append(element)



list.sort()
print(list)
print(f"primeiro produto: {list[0]}\núltimo produto: {list[-1]}\n")
