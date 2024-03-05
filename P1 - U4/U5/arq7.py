num = int(input())
lista = input().split()
for i in range(len(lista)):
    lista[i] = int(lista[i])
    if lista[i] < num:
        num = lista[i]
        print(num)
        break
    elif i > num:
        print(-1)
