soma = 0
cont  = 0
lista = []
while True:
    cont += 1
    fornadas = int(input())
    lista.append(fornadas)
    soma += fornadas 
    if soma >= 1000: break

print(soma)
media = soma / cont
print(f'{media:.2f}')
acima_med = 0
for i in lista:
    if i > media:
        acima_med += 1
print(acima_med)





