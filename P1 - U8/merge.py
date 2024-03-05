
# Auxiliador de ordenação, a lista já é ordenada, ordena apenas o último elemento.

def merge(lista1, lista2):
    lista3 = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            lista3.append(lista1[i])
            i += 1
        else:
            lista3.append(lista2[j])
            j += 1
   
    if i == len(lista1):
        for n in range(j, len(lista2)):
            lista3.append(lista2[n])
    else:
        for n in range(i, len(lista1)):
            lista3.append(lista1[n])
    return lista3

lista1 = [3, 5, 7]
lista2 = [1, 10, 30]

print(merge(lista1, lista2))