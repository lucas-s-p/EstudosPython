# Tuplas (tuple)
# Tuplas se parecem com listas, existem basicamente duas difernças basicas:
# Tuplas são represenadas por parênteses ()
# As tuplas são imutáveis: Isso signfica que ao criar uma tupla ela não muda. toda operação em uma tupla gera uma nova tupla.

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6             #python considera mesmo sem () essa sqn como uma tupla
print(tupla2)
print(type(tupla2))

tupla3 = (4)              #python não considera um elemento como tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)            #mas tendo a vírgula é tupla. Conclui-se que tuplas são definidas por vírgula.
print(tupla4)
print(type(tupla4))

tupla =  tuple(range(11))   # tupla a partir de ranger
print(tupla)

#Desempacotamento de tuplas:
tupla_A = ('Geek university', 'Programação em python: Essencial')
escola, curso = tupla_A
print(escola)
print(curso)

# Obs: valores para adição e remocão de elementos não existem, pois tuplas são imutáveis
# Ou seja, valores de sum, masx, min, fazem isso se forem valores reais ou inteiros.

#contatenação de tuplas
tupla_B = (1, 2, 3)
tupla_C = (4, 5, 6)
print(tupla_B + tupla_C)
print(tupla_B)
print(tupla_C)

tupla_B += tupla_C
print(tupla_B)

# verificar se determinado número está na tupla
tupla_D = (1, 2, 3)
print(3 in tupla_D)

# Iterando sobre uma tupla
tupla_E = (1, 2, 3)
for n in tupla_E:
    print(n)

for azul, valor in enumerate(tupla_E):   #coloquei azul para perceber que: não precisa ser indice, o programa entende que esse 
    print(azul, valor)                 # nome antes da virgula é o INDICE.

# contando elementos dentro de uma tupla
tupla_F = ('a', 'b', 'c', 'd', 'a', 'a', 'b')
print(tupla_F.count('a'))

escola = tuple('Geek University')      #converter uma string para tupla
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisamos modificar os dados contidos em  uma seleção

#Exemplo 1
meses = ('janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acessso de elementos de uma tupla é semelhante a uma lista:
print(meses[5])

#Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Índice de uma tupla;
print(meses.index('Junho'))

#Slicing   tupla[inicio:fim:passo]
print(meses[0:])
print(meses[5:])
print(meses[5:9])

# Obs: tuplas são mais rápidas do que listas
# obs: tuplas deixam seu código mais seguro

# copiando uma tupla para outra
tupla_G = (1, 2, 3)
print(tupla_G)
nova = tupla_G
print(nova)
