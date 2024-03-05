palavra1 = input()
palavra2 = input()
def organiza_palavra(palavra1, palavra2):
    reestrutura1 = palavra1[1::]
    reestrutura2 = palavra2[1::]
    return reestrutura1, reestrutura2

print('Letras coincidentes')

def verifica():
    letra = 1
    if palavra1[0] == palavra2[0]:
        print(f"'{palavra1[0]}' na posição {letra}")

    if palavra1[0] == palavra2[0]:
        cont = 1
    else:
        cont = 0
    return cont

def main():
    reestrutura1, reestrutura2 = organiza_palavra(palavra1, palavra2)
    pos = 1
    cont = verifica()
    for i in range(len(reestrutura1)):
        if reestrutura1[i] == reestrutura2[i]:
            pos += 1
            print(f"'{reestrutura1[i]}' na posição {pos}")
            cont += 1

    porcentagem = ((cont * 100) // (len(palavra1) + len(palavra2)))
    print(f'Total de letras coincidentes: {cont} ({porcentagem}%)')

if __name__ == "__main__":
    main()