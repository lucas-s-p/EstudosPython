def encontra_menor(lista, pos):
    indice = 0
    menor = lista[pos]
    for i in range(pos, len(lista)):
        if lista[i] <= menor:
            menor = lista[i]
            indice = i

    return indice 

def selection_sort(lista):
    for i in range(len(lista)):
        menor = encontra_menor(lista, i)
        lista[menor], lista[i] = lista[i], lista[menor]
    return lista

lista = [15, 7, -2, 0, 18, 3, 4]
print(selection_sort(lista))
