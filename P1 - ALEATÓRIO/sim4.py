palavra = input().split()

cont = 0
for i in range(len(palavra)):
    lista = [False, False, False, False, False]
    for v in range(len(palavra[i])):
        if palavra[i][v] == 'a':
            lista[0] = True
        elif palavra[i][v] == 'e':
            lista[1] = True 
        elif palavra[i][v] == 'i':
            lista[2] = True
        elif palavra[i][v] == 'o':
            lista[3] = True
        elif palavra[i][v] == 'u':
            lista[4] = True
    if lista[0] and lista[1] and lista[2] and lista[3] and lista[4]:
        cont += 1
print(f'Quantidade de pentavogalicas: {cont}')


num = int(input())
qtd = input().split()

cont = 0
for i in range(0, len(qtd) - 1):
    diferenca = abs(int(qtd[i]) - int(qtd[i + 1]))
    if diferenca > num:
        cont += 1
print(cont)

