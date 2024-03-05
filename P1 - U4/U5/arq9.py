def quantos_comeram(N, fila_pedidos):
    refeicao = int(N)
    soma = 0
    for i in range(len(fila_pedidos)):
        refeicao -= fila_pedidos[i]
        if refeicao < 0: break
        else:
            soma += fila_pedidos[i]
    return soma

print(quantos_comeram(5, [2, 3, 5]))
