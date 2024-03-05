def multiplica_lista(n,lista):
    nomes = []
    for i in range(n):
        for j in lista:
            nomes.append(j)
    return nomes

print(multiplica_lista(2, ['joao', 'pedro', 'marcos']))