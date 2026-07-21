#Dada a lista

#[3,5,2,5,7,8,2,3,10]

#Crie uma nova lista sem elementos repetidos, mantendo a ordem de aparecimento.

list = [3,5,2,5,7,8,2,3,10]

for i in list:
    aux_element = i

    for j in list:
        if aux_element == j:
            list.remove(aux_element)

print(list)
