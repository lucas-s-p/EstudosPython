num = int(input())

cont_adjacentes = 0
nao_adjacentes = 0
for n in range(num):
    achou = False
    senha = input()
    for e in range(len(senha) - 1):
        if senha[e] == senha[e + 1]:
            cont_adjacentes += 1
            achou = True
            break
        
nao_adjacentes = num - cont_adjacentes

print(f'com: {cont_adjacentes}')
print(f'sem: {nao_adjacentes}')