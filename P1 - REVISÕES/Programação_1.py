carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto !=  'sair':
        carrinho.append(produto)


for i, produto in enumerate(carrinho):
    print(i, produto)

import math

num = math.sqrt(36) + 2       # sqrt retorna a raiz quadrada de um numero
print(num)

num_2 = math.ceil(9.97)       # faz aproximação para maior
print(num_2)

num_3 = math.floor(4.5)      # faz aproximação para menor
print(num_3)

num_4 = math.sin(90)
print(num_4)

num_5 = math.cos(90)
print(num_5)

num_6 = math.tan(90)
print(num_6)

nome =  'joRge'
print(nome.capitalize())      # primeira letra maiuscula 

nome =  'jorge'
print(nome.upper())      # nome todo maiuscula 

nome =  'jorge'
print(nome.lower())      # todo minusculo

nome =  'jorgee'
print(nome.count('e'))      # conta o núumero de repeticoes de numeros e carcteres

num = 12 + abs(-5)              # mfunção modular
print(num)


nome = 'lucas teste ola'
lista = nome.split(' ')
print(lista)
lista[1] = 'eu sou mudável'  # da para atribuir em listas, strings não funciona(strings são imutáveis)
print(lista)
