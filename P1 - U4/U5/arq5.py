conjunto = []
while True:
    elemento = input()
    if elemento == 'fim': break
    conjunto.append(elemento)
nome = None
maior = 0
for i in range(len(conjunto)):
    cont = 0
    for v in range(len(conjunto[i])):
        if conjunto[i] != '---':
            cont += 1
        if cont > maior:
            maior = cont
            nome = conjunto[i]
    
separador = 1
for i in range(0, len(conjunto)):
    if conjunto[i] == '---':
        separador += 1
    if conjunto[i] == nome: break

if nome == None:
    parada = True
else:
    print(f'Conjunto {separador}: {nome} ({maior} letras)')