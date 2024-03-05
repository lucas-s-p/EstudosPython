lista = [2, 5, 7, 8, 9]
lista2 = [3, 1, 45, 67]

def ordena(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) -1):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
    
    return lista

def ordena2(lista2):
    for i in range(len(lista2) - 1):
        for j in range(len(lista2) -1):
            if lista2[i] > lista2[i + 1]:
                lista2[i + 1], lista2[i] = lista2[i], lista2[i + 1]
    return lista2

lista3 = []
i = 0
j = 0
lista = ordena(lista)
lista2 = ordena(lista2)
while len(lista) > i and len(lista2) > j:
    if lista[i] <= lista2[j]:
        lista3.append(lista[i])
        i += 1
    else:
        lista3.append(lista2[j])
        j += 1
    
if i == len(lista):
    for v in range(j, len(lista2)):
        lista3.append(lista2[v])
else:
    for n in range(i, len(lista)):
        lista3.append(lista[n])

print(lista3)