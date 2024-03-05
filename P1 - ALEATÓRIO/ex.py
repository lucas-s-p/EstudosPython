num_dados = int(input())

lista = []
for i in range(num_dados):
    i = int(input())
    lista.append(i)

max = 0
for i in range(len(lista)):
    if lista[i] > max:
        max = lista[i]
print(max)

min = None
for i in lista:
    if min == None or i < min:
        min = i
print(min)


qtd = 0
media = 0
for m in range(len(lista)):
    qtd += 1
    media += (lista[m]) / qtd
    print(media)

for i in range(num_dados):
    print(lista)
