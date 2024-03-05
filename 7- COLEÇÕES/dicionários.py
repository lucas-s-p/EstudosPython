# Dicionários
# Obs: Em algumas linguagens de programação, os dicionários python são conhecidos por mapas.
# Dicionários são coleções do tipo chave/valor
# Dicionários são representados por chaves {}
# chave e valor podem ser de qualquer tipo de dados e podem ser misturados.

#Forma mais comum:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}  # chave e valor são separados por dois pontos: chave:valor
print(paises)
print(type(paises))

#forma menos comum:
paises = dict(br = 'Brasil', eua = 'Estados Unidos', py = 'Paraguay')
print(paises)
print(type(paises))

# Acessando elementos
# forma 1 - acessando via chave
print(paises['br'])
print(paises['eua'])

#forma 2 - acessando via get - forma recomendada -  Nessa forma não gera erro, aparece None, já na forma 1 da erro.
print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print('Não encontrei o país')

# OU
pais = paises.get('ru', 'Não encontrado')    # se vocễ não encontrar print Não encontrado
print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises )
print('Estados Unidos' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Tipos de dados misturados
localidades = {
    (35.6547, 23.4534): 'Escritório em Tókio',
    (40.7128, 74.3468): 'Escritório de Nova York',
    (37.7653, 122.4196): 'Escritório de São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário:
receita = {'jan': 100, 'fev': 120, 'marc': 300}
print(receita)
print(type(receita))

#Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

#Forma 2
novo_dado = {'maio': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)

# Em dicionários não podemos ter chaves repetidas.

# Remover dados de um dicionário

#Forma 1
ret = receita.pop('marc')   #Para remover tem q informar a chave.
print(ret)         #ao remover um objeto, o valor é sempre retornado.              
print(receita)

#Forma 2
del receita['fev']   #neste caso o valor removido não é retornado.
print(receita)

# Onde usar dicionário ? Imagine um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
# Usando Listas:
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]   #nome, qtd, valor
produto2 = ['Good of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#teríamos que saber qual é o índice de qual informação do produto

# Usando Tuplas:
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Good of war 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
#teríamos que saber qual é o índice de qual informação do produto

# Usando dicionários:
carrinho = []

produto1 = {'nome': 'Playstation 4', 'qtd': 1, 'valor': 230.00}
produto2 = {'nome': 'Good of war 4', 'qtd': 1, 'valor': 300.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Desta forma facilmente adicionamos ou removemos produtos do carrinho e temos mais informações sobre cada índice

# Métodos de dicionário.
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)
#d.clear()
#print(d)

# Copiando um dicionário para outro
#Forma 1
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

#Forma 2
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)     #Ambos dicionários são alterados

# forma não usual de criação de dicionários;
outro = {}.fromkeys('a', 'b')   #chave:valor
print(outro)
print(type(outro))

#OU
usuario = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')  #fromkeys  recebe dois valores: um iterável e um valor.
print(usuario)            #ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
print(type(usuario))

#OU
veja = {}.fromkeys('teste', 'valor')   #para cada letra ele criou uma chave com o valor. Obs: em dicionárrio não tem 
print(veja)                           #repetição de chave, logo, da string 'teste' ele não repitiu o 't' e o 'e'.

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)




