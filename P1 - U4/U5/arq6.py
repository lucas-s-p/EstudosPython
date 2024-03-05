def maioridade_penal(nome, idade):
    pessoa = nome.split()
    num = idade.split()
    nomes = ''
    for i in range(len(pessoa)):
        num[i] = int(num[i])
        if num[i] >= 18:
            nomes += f'{pessoa[i]} '
    saida = ''
    for e in range(len(nomes) - 1):
        saida += nomes[e]
    return saida
print(maioridade_penal('lucas rodrigo', '18 20'))