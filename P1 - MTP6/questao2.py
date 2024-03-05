cont_par = 0
cont_impar = 0
while True:
    num = input()
    if num == 'fim': break
    if int(num) % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

if cont_par > 0:
    print(f'pares = {cont_par}')
if cont_impar > 0:
    print(f'ímpares = {cont_impar}')
