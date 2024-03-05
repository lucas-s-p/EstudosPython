def adiciona_maior(lista):
    maior_dif_absoluta = 0
    for i in range(len(lista) -1):
        dif_absoluta = abs(lista[i] - lista[i+1])
        if dif_absoluta > maior_dif_absoluta:
            maior_dif_absoluta = dif_absoluta

    for i in range(len(lista)):
        lista[i] += maior_dif_absoluta

l1 = [2, 6, 5, 4, 0, 1]
assert adiciona_maior(l1) == None
assert l1 == [6, 10, 9, 8, 4, 5]

