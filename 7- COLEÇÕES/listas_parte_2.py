from email.policy import strict


lista1 = [1, 34, 12, 35, 45, 75, 12, 67, 89, 23]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Interando sobre listas 

#utilizando for
soma = 0
for elemento in lista4: 
    print(elemento)
    soma += elemento
print(soma)

soma = ''
for elemento in lista2: 
    print(elemento)
    soma += elemento
print(soma)

#utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto !=  'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

#utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)
num1 = 1 
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])   # e assim por diante para as  posições 1, 2, 3.

#Fazer acessso aos elementos de  forma indexada inversa
print(cores[-1])  #é como se fosse uma roda, pega os numeros a esquerda do zero -1(ult. ele. contando pela dir.), -2, -3, -4.

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):    #len = tamanho
    print(cores[indice])      # enq o indice for menor que o tamanho, que é 4, imprima cores na posição indice
    indice += 1

# Gerar indices em um for
for indice, cor in enumerate(cores):    #enumerate vai gerar chave e valor.
    print(indice, cor)

# Listas aceitam valores repitidos
lista =[]
lista.append(42)
lista.append(42)
lista.append(43)
lista.append(43)
print(lista)

#outros métodos não tão importantes, mas também úteis:

#Encontrar o índice de um elemento na lista
#em qual índice da lista está o valor 6 ?
numeros = [5, 6, 7, 8, 7, 9, 10]
print(numeros.index(6))
#em qual índice da lista está o valor 9 ?
print(numeros.index(9))

#Obs: se tiver dois elemento iguais ele retorna o primeiro que achar.
print(numeros.index(7))

#podemos fazer busca dentro de um range, ou seja, qual o índice começar a buscar
print(numeros.index(7, 3))  #obs significa que (7, 3) deve-se achar em q indice está o valor 7, a partir, do indice 3, ou seja,
                            # para não achar o primeiro indice que tem o valor 3.

#Podemos fazer uma busca dentro de um range, inicio/fim
print(numeros.index(9, 2, 6))  #buscar o indice do valor 9, entre os índices 2 a 6
 
#Revisão de slicing
#lista[inicio:fim:passo]

#trabalhando com slicing de lista com o parâmetro 'inicio'
lista = [1, 2, 3, 4]
print(lista[1:])   #lista começando no indice 1 e pegando todos os elementos restantes [::] pegava toda lista

#trabalhando com slicing de lista com o parâetro 'fim'
print(lista[:2]) #começa em 0, e vai ate o índice 2 - 1, pois o ultimo não tá incluido.

#trabalhando com slicing de lista com o parâmetro 'passo'
print(lista[1::2])   #começa em 1, vai até o final, de 2 em 2.
#ou 
print(lista[1::-1])  #inverte 

#invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))    #soma
print(max(lista))   #máximo valor
print(min(lista))   # mínimo valor
print(len(lista))   #tamanho da lista

#Transforma uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)    # difernça inicial é a reprenstação entre [] e ()
print(tupla)
print(type(tupla))

#Desempacotamento de listas
lista = [1, 2, 3]            # numero de elementos e variáveis tem que ser igual para o desempacotamento.
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# copiando uma lista para outra (Shallow copy e Deep copy)
#forma 1 - Deep copy
lista = [1, 2, 3]
print(lista)
nova = lista.copy()   # uma copia de lista ão afeta na lista antiga... isso é Deep copy(cópia profunda)
print(nova)
nova.append(4)
print(lista)
print(nova)

#forma 2 - Shwllow copy
lista = [1, 2, 3]
print(lista)
nova = lista   # observe que nesse modelo as duas listas são modificadas...
print(nova)
nova.append(4)
print(lista)
print(nova)






