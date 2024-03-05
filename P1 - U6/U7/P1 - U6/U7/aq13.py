def remove_mantem_modifica(lista):
    for e in range(len(lista) -1, -1, -1):
        if lista[e] % 3 == 0 and lista[e] % 4 == 0 and lista[e] % 5 == 0:
            lista[e] = 60
        elif lista[e] % 3 == 0 and lista[e] % 4 == 0:
            lista[e] = 12
        elif lista[e] % 4 == 0 and lista[e] % 5 == 0:
            lista[e] = 20
        elif lista[e] % 3 == 0 or lista[e] % 4 == 0 or lista[e] % 5 == 0:
            lista.pop(e)
        else:
            lista[e] = lista[e]

l1 = [1, 2, 3, 120, 24]
assert remove_mantem_modifica(l1) == None