def meu_in(elemento, lista):
    cont = 0
    for e in lista:
        if elemento == e:
            cont += 1
    return cont

def remove_trios(lista):
    l = []
    for i in range(len(lista)):
        elemento = lista[i]
        cont = meu_in(elemento, lista)
        l.append(cont)
    print(l)
    for n in range(len(l) -1, -1, -1):
        if l[n] == 3:
            lista.pop(n)

    return lista

print(remove_trios([1, 1, 2, 2, 2, 1]))
