num_palavras = int(input())

palavra_dobrada = []
palavra_nao_dobrada = []
dobrada = 0
nao_dobrada = 0 
for i in range(num_palavras):
    palavra = input()
    achou = False
    for e in range(len(palavra) - 1):
        if palavra[e] == palavra[e + 1]:
            dobrada += 1
            achou = True
            palavra_dobrada.append(palavra)
            break
    if not achou:
        palavra_nao_dobrada.append(palavra)
        nao_dobrada += 1

print(f'{dobrada} palavra(s) com letras dobbradas:')
for i in range(len(palavra_dobrada)):
    print(palavra_dobrada[i])
print('---')
print(f'{nao_dobrada} palavra(s) sem letras dobradas:')
for i in range(len(palavra_nao_dobrada)):
    print(palavra_nao_dobrada[i])