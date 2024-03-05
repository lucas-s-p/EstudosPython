valor_inteiro = int(input())
sequencia = input().split()

indice = []
for i in range(len(sequencia)):
    sequencia[i] = int(sequencia[i])
    if sequencia[i] == valor_inteiro:
        indice.append(str(i))

if indice != []:
    string = ''
    for v in range(len(indice)):
        if (len(indice) -1) != v:
            string += f'{indice[v]} '
        else:
            string += f'{indice[v]}'
    print(string)
else:
    print(-1)