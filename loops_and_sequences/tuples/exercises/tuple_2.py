#Exercício 5 - Notas

#Crie uma tupla com cinco notas.

#Mostre: maior nota menor nota média

i = 0
media = 0
maior = 0
menor = 0
soma = 0
list = []

while i != 5:
    list.append(float(input(f'Informe uma nota: {i+1}/5: ')))
    i+=1
    
my_tuple = tuple(list)
print(my_tuple)
maior = my_tuple[0]
menor = my_tuple[0]

for j in my_tuple:
    soma += j
    if j > maior:
        maior = j
    elif j < menor:
        menor = j

media = soma / len(my_tuple)
print(f"Maior: {maior}\nMenor: {menor}\nMédia: {media}\n")       
