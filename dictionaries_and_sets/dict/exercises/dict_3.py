#exercício 12 - Contador de palavras
#Leia uma frase.
#Conte quantas vezes cada palavra aparece.
#Exemplo:
#Entrada
#python é legal python é poderoso
#Saída
#python -> 2 é -> 2 legal -> 1 poderoso -> 1

frase = str(input())

my_dict = {}

for i in frase.split():
    my_dict[i] = frase.count(i)
    
print(my_dict)