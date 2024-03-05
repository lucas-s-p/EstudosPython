# Auxiliador de ordenação, a lista já é ordenada, ordena apenas o último elemento.

def insere_ordenado(lista, elemento):
    lista.append(elemento)
    j = len(lista) -1
    while j > 0 and lista[j - 1] > lista[j]:
        lista[j], lista[j - 1] = lista[j - 1], lista[j]
        j -= 1
    return lista

lista = [1, 4, 7, 8, 12, 15]
elemento = 3

print(insere_ordenado(lista, elemento))
