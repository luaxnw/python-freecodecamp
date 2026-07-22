#Dada a lista

#[3,5,2,5,7,8,2,3,10]

#Crie uma nova lista sem elementos repetidos, mantendo a ordem de aparecimento.

list = [3,5,2,5,7,8,2,3,10]
new_list = []
my_set = set()

for i in list:
    if i not in my_set:
        my_set.add(i)
        new_list.append(i)


print(new_list)
