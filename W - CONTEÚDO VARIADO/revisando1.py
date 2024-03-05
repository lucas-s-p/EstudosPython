def encontra_menor(num):
    menor = num[0]
    ver = [num[i] for i in range(len(num)) if num[i] < menor]
    
    return ver

print(encontra_menor([1, 2, -3, -8, 0, 100]))

num = [[1, 10, 12, 3, 345], [3, 2, 1]]
[[print(n**2) for n in lista_n if n > 9] for lista_n in num]

def maior_30(numeros):

    maior = [[numeros[i][j] for j in range(len(numeros[i])) if numeros[i][j] > 30] for i in range(len(numeros))]

    return maior

numeros = [[1, 2, 3], [34, 55, 6], [21, 34, 36]]
print(maior_30(numeros))
