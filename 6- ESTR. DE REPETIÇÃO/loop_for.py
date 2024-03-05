# Loop For 
# Loop -> Estrutura de repetição
# For -> Uma dessas estruturas

# Estrutura dor for em python:
# for item in interavel:
#    execução do loop

# Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
#Exemplos de iteráveis:
# -String
#   nome = 'Geek noversity'
# Lista
#   lista = [1, 3, 5, 7, 9]
# Range
#   numeros = range(1, 10)

#Exemplo de for 1 (Interando em uma string)
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:   #Significa: Para cada letra dentro dessse interável(nome) imprima esssa letra.
    print(letra)

#Exemplo de for 2 (Interando soobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (Interando sobre um range)
for numero in range(1, 10):              #range(valor_inicial, valor_final(menos a ultima posição escrita como valor final))
    print(numero)

# observe agora três formas de fazer o mesmo for:
#  #para o índice i, enumere para cada posição um caractere da variavel nome e imprima 

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome): # o "_" elimina descarta o indice. Pois o enumerate devolve dois valores: indice e letra.
    print(letra)                # nesse caso o _ descartou o indice

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0]) #como vimos tem a posição zero(a qual fica os indices) e a posição um(a qual fica os valores da variavel)
                             #então a posição zero[0] indica todos os indices e o um [1] fica o valor correspondente da variável.

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar ?'))
for n in range(1, qtd+1):             #qtd + 1: agora vai a qtd que ele informou.       
    print(f'imprimindo {n}')                 #for que reccebe os dados e vai de 1 até a qtd informada.

qtd = int(input('Quantas vezes esse loop deve rodar ?'))
soma = 0

for n in range(1, qtd+1):                 
    num = int(input(f'informe o {n}/{qtd} valor: '))      
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek Univeristy'
for letra in nome:
    print(letra, end='')    # end='' é para não pular a linha, continuar na mesma.

nome = 'Geek'
nome + 'University'   #isso é chamado de cotatenação de string com outra que será adicionado.
nome * 30                                                                                                     

#Tabela de emojis: https://apps.timwhitlock.info/emoji/tables/unicode

#original: U+1F60D
#modificado: U0001F60D    #no lugar do mais coloca tres zeros

for num in range(1, 11):
    print('\U0001F60D' * num)     # o \ é um caractere de escape, ele ignora o codigo.

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)     # o \ é um caractere de escape, ele ignora o codigo.

 