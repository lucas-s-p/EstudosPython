lista = []
for i in range(5):
    num = int(input('Digite um valor: '))
    lista.append(num)

for j in range(len(lista)-1):
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)