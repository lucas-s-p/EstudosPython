saidas = []
while True:
    cont = 0
    cont_zera = 0
    lista = ''
    seq = input()
    if seq == '.F.F.F.F.F': break
    for i in range(len(seq)):
        if seq[i] == 'F':
            cont += 1
            cont_zera += 1
        if seq[i] == '.' and cont_zera != 0:
            lista += f'{cont_zera} + '
            cont_zera -= cont_zera
    if seq[-1] == 'F':
        lista += f'{cont_zera} + '

    if lista != '': 
        saida = ''
        for e in range(len(lista) - 2):
            saida += lista[e]
        saidas.append(f'{cont} falha(s): {saida}')
    else:
        saidas.append(f'{cont} falhas')

for s in saidas:
    print(s)