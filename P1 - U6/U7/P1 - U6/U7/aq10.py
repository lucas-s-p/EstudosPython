def meu_in(elemento, lista2):
    for e in lista2:
        if e == elemento:
            return True
    return False

def diferenca_listas(lista1, lista2):
    for i in range(len(lista1) -1, -1, -1):
        elemento = lista1[i]
        if meu_in(elemento, lista2):
            lista1.pop(i)
    
    return lista1

print(diferenca_listas([1, 4, 6, 8, 10], [2, 4, 5, 10]))

print(diferenca_listas([1, 4, 6, 8, 10], []))
