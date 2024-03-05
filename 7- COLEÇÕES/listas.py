# Listas
# Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
# e também de podermos colocar QUALQUER tipo de dado.
# Dinâmico: Não possui tamanho fixo, diferente de java ou C. Até quando houver espaço de memória os valores são armazenados.
# Qualquer tipo de dado: Não possuem tipo de dado fixo.
# As listas em python são representas entre colchetes: []

lista1 = [1, 34, 12, 35, 45, 75, 12, 67, 89, 23]
lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Podemos checar facilmente ver se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o n° 8')
else:
    print('Não encontrei o n° 8')
 
#Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

#Podemos faacilmente contar o n° de ocorrências de um valor em uma lista
print(lista1.count(12))
print(lista5.count('e'))

# Adicionar elementos em listas, utilizamos a função append, mas só podemos adicionar um elemento por vez.
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([2, 28, 245])        # ai não tá sendo adicionado mais de um elemento, tá sendo adicionado uma lista. o [] representa isso.
print(lista1)

lista1.extend([123, 44, 67]) #faz a mesma coisa do append, mas os valores são adicionados individualmente e não aceita val. unico.
print(lista1)

lista1.extend('Geek')
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo valor')  # inserir na posição 2, no lugar do n°4, o seguinte: 'Novo valor'
print(lista1)                   # lembrando que o  valor 4 vai ser deslocado para proxima posição.

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

#ou
lista1.extend(lista2)
print(lista1)

#Podemos reverter os elementos de uma lista
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#ou
print(lista1[::-1])
print(lista2[::-1])

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#Podemos contar quantos elementos tem dentro de uma lista
print(len(lista2))

#Podemos remover o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento  pelo índice
lista5.pop(2)
print(lista5)

#Podemos limpar a lista toda, zerar todos os elementos
#lista5.clear()
#print(lista5)

#Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova *= 3
print(nova)

# Podemos converter uma string para uma lista, a lista é separada pelos espaços.
curso = 'Lucas testando'
print(curso)
curso = curso.split()
print(curso)

#ou
curso = 'Programação, essencial,em,python:,Essencial'
print(curso)
curso = curso.split(',')     # esse ',' tá dizendo que o separador não é mais os espaços e sim a vírgula.
print(curso)

# convertendo uma lista em uma string
lista6 = ['Programação', 'essencial', 'em', 'python:', 'Essencial']
print(lista6)       #pega a lista6, coloca espaço(mas poderia separar por qlq coisa) entre cada elemento e transforma em string.
curso = ' '.join(lista6)
print(curso)

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 12345553222] #obs: a lista pode ter qlq coisa e misturadoo..sem problemas.





