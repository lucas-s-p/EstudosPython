par = 0
impar = 0
lista_par = []
lista_impar = []
verifica = 0
while True:
    num = int(input())
    if num % 2 == 0:
        par += 1
        lista_par.append(num)
    else:
        impar += 1
        lista_impar.append(num)
    
    if impar > (par + 2):
        verifica = 1
        break
    if par > (impar + 2 ):
        verifica = 2
        break

if verifica == 1:
    print('IMPARES em maior quantidade')
elif verifica == 2:
    print('PARES em maior quantidade')

print('PARES:')
for i in lista_par:
    print(i)
print('IMPARES:')
for i in lista_impar:
    print(i)

