palavra = input()

itera = palavra[1::]
contador = 0
soma = ''
for e in itera:
    if e == 'a' or e == 'A':
        e = '4'
        contador += 1
    elif e == 'e' or e == 'E':
        e = '3'
        contador += 1
    elif e == 'i' or e == 'I':
        e = '1'
        contador += 1
    elif e == 'o' or e == 'O':
        e = '0'
        contador += 1
    soma += e

palavra1 = input()
palavra2 = input()

reestrutura1 = palavra1[1::]
reestrutura2 = palavra2[1::]
print('Letras coincidentes')

letra = 1
if palavra1[0] == palavra2[0]:
    print(f"'{palavra1[0]}' na posição {letra}")

if palavra1[0] == palavra2[0]:
    cont = 1
else:
    cont = 0

pos = 1
for i in range(len(reestrutura1)):
    if reestrutura1[i] == reestrutura2[i]:
        pos += 1
        print(f"'{reestrutura1[i]}' na posição {pos}")
        cont += 1



porcentagem = ((cont * 100) // (len(palavra1) + len(palavra2)))