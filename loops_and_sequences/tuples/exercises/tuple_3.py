#Exercício 6 - Coordenadas

#Crie uma lista de tuplas representando coordenadas.

#[(3,5), (7,2), (8,10), (0,1)]

#Mostre apenas os pontos cuja soma das coordenadas seja maior que 10

coordenadas = [(3,5), (7,2), (8,10), (0,1)]

for x,y in coordenadas:
    if x + y > 10:
        print(x,y)
