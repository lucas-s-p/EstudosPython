def meu_insert(lista, indice, valor):
    lista.append(valor)
    for i in range(len(lista) -1, 0, -1):
        if lista[i - 1] < valor:
            lista[i - 1], lista[i] = lista[i], lista[i - 1]
        else:
            return

def noves_fora(lista):
    while True:
        if len(lista) == 1 and lista[0] < 9: break
        primeiro = lista.pop(0)
        segundo = lista.pop(0) if len(lista) > 0 else 0
        noves_fora = (primeiro + segundo) % 9
        meu_insert(lista, 0, noves_fora)
    return noves_fora

print(noves_fora([9, 7, 5, 4, 3, 1]))