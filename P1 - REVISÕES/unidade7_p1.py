from operator import index


lista = [1, 2, 3, 4, 5]
for i in range(len(lista) - 1, -1, -1):
    print(lista[i])


li = []
for n in range(len(lista)):
    if lista[n] % 2 != 0:
        li.append(lista[n])
print(li)

posicao = 1
lista.append(15)
for i in range(len(lista) - 1, posicao, - 1):
    lista[i], lista[ i - 1] = lista[i - 1], lista[i]
print(lista)

def insert_ordenado(lista, elemento):
    lista.append(elemento)
    j =len(lista) - 1

    while j > 0 and lista[ j - 1] > lista[j]:
        lista[j], lista[j - 1] = lista[j - 1], lista[j]
        j -= 1
    
l = [3, 9, 15, 16, 20, 22, 25]
insert_ordenado(l, 0)
print(l)

def merge(lista1, lista2):
    lista3 = []
    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            lista3.append(lista1[i])
            i += 1
        else:
            lista3.append(lista2[j])
            j += 1
        
        if i == len(lista1):
            lista3 += lista2[j:]
        else:
            lista3 += lista1[i:]
           
    return lista3

print(merge([4, 5, 6, 7, 8], [1, 2, 3]))

def selection_sort(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
        if menor ==  lista[i]:
            indice = i
        lista[indice], lista[n] = lista[n], lista[indice]
    
    return lista

print(selection_sort([60, 44, 20, 49, 10]))

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

print(bubble_sort([20, 49, 10, 3, 5, 43, 2]))

