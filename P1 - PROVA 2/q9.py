limite = int(input())
vagoes = input().split()
cont = 0
for i in range(len(vagoes) -1):
    if abs(int(vagoes[i]) - int(vagoes[i + 1])) > limite:
        cont += 1

print(cont)

