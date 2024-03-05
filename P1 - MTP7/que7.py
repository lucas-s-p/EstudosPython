def adiciona_maior(lista):
    maior = 0
    for i in range(len(lista) - 1):
        dif = abs(lista[i] - lista[i + 1])
        if dif > maior:
            maior = dif

    for n in range(len(lista)):
        lista[n] += maior
    

l1 = [2, 6, 5, 4, 0, 1]
print(adiciona_maior(l1))
