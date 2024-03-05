def meu_in(elemento, lista2):
    for e in lista2:
        if e != elemento:
            return True
    if lista2 == []: return True

    return False

def intersecao_listas(lista1, lista2):
    for i in range(len(lista1) -1, -1, -1):
        elemento = lista1[i]
        if meu_in(elemento, lista2):
            lista1.pop(i)

    return lista1

lista1 = [2, 1, 3, 4]
lista2 = [2]
assert intersecao_listas(lista1, lista2) == [2]
assert lista1 == [2]

print(intersecao_listas([0, 1, 2, 4], []))