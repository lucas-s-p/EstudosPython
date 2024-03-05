def encontra_nome(nomes, idade):
    list_nomes = {nomes[i]: idade[i] for i in range(len(nomes))}

    return list_nomes

print(encontra_nome(['lucas', 'levi', 'leo'], [1, 2, 3]))

def maiores_18(nome, idade):
    verifica = {nome[i]: idade[i] if sum(idade) < 100 else False for i in range(len(idade))}
    return verifica

print(maiores_18(['lucas', 'levi', 'joao'], [18, 20, 22]))
