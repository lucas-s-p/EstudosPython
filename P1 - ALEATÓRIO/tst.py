lista = [1, 2, 3, 4, 5, 6, 30, 50, 2, 1, 1]

for i in range(len(lista) - 1):
    if lista[i] >= lista[i + 1]:
        lista[i] =  len(lista) / 2
print(lista)


while True:
    num = input().split()
    lista = []
    for i in range(len(num)):
        num[i] = int(num[i])
        lista.append(num[i])

    som = 0
    for v in range(len(lista)):
        som += lista[v]
        
    if som > 100: break