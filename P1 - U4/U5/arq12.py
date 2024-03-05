conjunto = []
while True:
    elemento = input()
    if elemento == 'fim': break
    conjunto.append(elemento)

if conjunto != []:
    compara = []
    cont = 0
    for i in conjunto:
        if i != '---' and int(i) % 2 == 0:
            cont += 1
        if i == '---' and cont != 0:
            compara.append(cont)
            
    if compara != []:
        val_final = []
        val_final.append(compara[0])
        for n in range(len(compara) - 1):
            dif = compara[n + 1] - compara[n]
            val_final.append(dif)

        maior = 0
        i = 1
        for v in range(len(val_final)):
            if val_final[v] > maior:
                maior = val_final[v]
                i += v
        print(f'conjunto {i}: {maior} par(es)')