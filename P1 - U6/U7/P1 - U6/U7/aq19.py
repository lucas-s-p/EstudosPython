def intersecao_listas(lista1, lista2):
    for i in range(len(lista1) -1, -1, -1):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]: break
            elif (len(lista2) -1) == j:
                lista1.pop(i)

    return lista1



lista1 = [2, 1, 3, 4]
lista2 = [2]
intersecao_listas(lista1, lista2)
assert lista1 == [2]

lista1 = [1, 3, 4]
lista2 = [4, 3]
intersecao_listas(lista1, lista2)
assert lista1 == [3, 4]

lista1 = [2, 4, 1]
lista2 = [1, 3, 4]
intersecao_listas(lista1, lista2)
assert lista1 == [4, 1]

