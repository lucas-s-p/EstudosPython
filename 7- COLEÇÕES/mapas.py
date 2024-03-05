# Mapas -> Conhecidos em python como dicionários
# Dicionários em python são repressentados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave}: {receita[chave]}')

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

#Acessando as chaves
print(receita.keys())     #forma um dicionário de chaves

for chave in receita.keys():  #forma pythônica
    print(chave)

#Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários:
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

print(receita.items())         # dicionário de items contem lista e tupla.

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))