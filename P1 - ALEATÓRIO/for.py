pessoas = range(100)

maior = 0
for i in pessoas:
    if pessoas[i] > pessoas[maior]:
        maior = i

print(maior)

s = input()
saida = ''
for i in range(len(s)):
    if i == len(s) - 1:
        saida += '*'
    else:
        saida += s[i]
print(saida)

tamanho = input().split()
maiori = 0
for i in range(len(tamanho)):
    tamanho[i] = int(tamanho[i])

    if tamanho[i] > tamanho[maiori]:
        maiori = i
print(maiori)

pessoas = [1, 2, 5, 89, 3]
maior = 0
for altura in pessoas:
    if altura > maior:
        maior = altura
print(maior)

