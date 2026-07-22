#Exercício 8 - Letras únicas

#Peça uma frase ao usuário.

#Mostre:

#conjunto das letras utilizadas, quantidade de letras diferentes

frase = input(str("Digite uma frase: "))
letras = list(frase)
my_set = set(letras)
print(my_set, "\n",len(my_set))

