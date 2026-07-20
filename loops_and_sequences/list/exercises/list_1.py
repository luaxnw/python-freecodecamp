#Exercício 1 - Soma dos números
#Crie uma lista com 10 números inteiros e mostre:

#a soma
#o maior número
#o menor número
#a média

numeros = [10, 5, 8, 2, 15, 20, 7, 3, 9, 11]

soma = 0
maior = numeros[0]
menor = numeros[0]
media = 0

for element in numeros:
    soma += element
    if element > maior:
        maior = element
    if element < menor:
        menor = element

media = soma / len(numeros)

print(f"soma: {soma}\nmaior: {maior}\nmenor: {menor}\nmédia: {media}")


