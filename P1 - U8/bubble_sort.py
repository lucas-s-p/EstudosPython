def bubble_step(lista):
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
        
    return lista

lista = [1, 10, -2, 0, 1, 4]
print(bubble_step(lista))
