def remove_multiplos_do_menor(lista):
    menor = 0
    for i in range(len(lista)-1, -1, -1):
        if menor == 0 or lista[i] < menor:
            menor = lista[i]
    
    for j in range(len(lista)-1, -1, -1):
        if lista[j] % menor == 0:
            lista.pop(i)
  

l1 = [6, 9, 10, 3, 5]
print(remove_multiplos_do_menor(l1))

