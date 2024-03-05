# Conjuntos 
# Conjuntos em qualquer ling. de programação, fazemos referência à teoria dos conjuntos da matemática.
# No python os conjuntos são chamados de Sets.
# Sets(conjuntos) não possuem valores duplicados, nem valores ordenados.
# Elementos não são acessados via índice, ou seja, conjuntos não são indexados.
# Conjuntos são bons para utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
# Quando não precisamos se preocupar com chaves, valores e itens duplicados.
# Sets são referenciados por chaves {}
# Mapas: chave/valor       conjuntos: Apenas valor

# Definindo um conjunto:

#Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})       # Não imprime valores repitidos, pode ter e não da erros, mas não imprime
print(s)
print(type(s))

# forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#Verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem em Sets
#OBS:
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5]
print(f'lista: {lista}')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5
print(f'Tupla: {tupla}')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5], 'dict')
print(f'Dicionário: {dicionario}')


conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5}
print(f'Conjunto: {conjunto}')

# Em sets pode-se ter tipos de dados misturados
s1 = {1, 'b', True, 34.22, 44}
print(s1)
print(type(s1))

# Podemos iterar em um set:
for valor in s1:
    print(valor)

# Usos interessantes com sets:

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam
# manualmente a cidade de onde vieram.

# Nos adicionamos cada cidade em uma lista de python , já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

#Agora precisamos saber quantas cidades distanes, ou seja, únicas temos.
print(len(set(cidades)))

conj = set(cidades)
print(conj)

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
print(s)

# Remover elementos em conjuntos:
p = {1, 2, 3}
print(p)
#Forma 1
p.remove(3)
print(p)
#Forma 2
p.discard(2)
print(p)

# copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# forma 1: Deep copy   # a cópia é separada do conj. original
novo = s.copy()
print(novo)
#Forma 2: shallow copy  # a cópia se modificada, modifica o original também
novo = s
print(novo)

# Podemos remover todos os itens em conjuntos:
#s.clear()
#print(s)

# Métodos matemáticos de conjuntos:
estudantes_a = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_b = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}   # Obs que alguns elementoss se repetem nos 2 conjuntos

# Gerando um conj com nomes unicos: Forma 1: Utilizando union
unicos1 = estudantes_a.union(estudantes_b)
print(unicos1)


# Forma 2: Utilizado o caractere pipe | 
unicos_2 = estudantes_a | estudantes_b
print(unicos_2)

# Gerar um conjunto de estudantes que estão em ambos:  Usando o intersection: Forma 1
ambos1  = estudantes_a.intersection(estudantes_b)
print(ambos1)

#Forma 2
ambos2 = estudantes_a & estudantes_b
print(ambos2)

# Gerar um conjunto de estudantes de um curso que não estão no outro: usando diferrence
so_a = estudantes_a.difference(estudantes_b)
print(so_a)

so_b = estudantes_b.difference(estudantes_a)
print(so_b)

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
