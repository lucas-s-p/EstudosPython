# Funções com retorno
# 

#def quadrado_de_7():
    #print(7 * 7)

#quadrado_de_7()

#ret = quadrado_de_7()
#print(f'Retorno é de: {ret}')   # Em python quando uma função não retorna nada, nenhum valor, o retorno é NONE

# Vamos refatorar(reescrever) esta função para que ela retorne o valor.
# Em python as funções que retornam valores, devem retornar valores com a palavra reservada return.
def quadrado_de_7():
    return 7 * 7

quadrado_de_7()

ret = quadrado_de_7()
print(f'Retorno é de: {ret}')

# OBS: Não precisamos necessariamente criar uma variável para recber o retorno da função. Podemos passar a execução da função
# para outras funções.
print(f'Retorno: {quadrado_de_7()}')
#Podemos até messmo fazer operações
print(f'Retorno é {quadrado_de_7() + 1}')  # exemplo de soma

# Refatorando a primeira função
def diz_oi():
    return 'oi, '     # SE FOSSE UM PRINT NÃO TERIA COMO REUTILIZAR PARA FAZER CÁLCULOS E MUDANÇAS

print(diz_oi())
# Uma vantagem do return e não fazer apenas imprimindo direto é a possibilidade de fazer operações:
alguem = 'Lucas!'
print(diz_oi() + alguem)

# OBS: Sobre a palavra reservada return :
# - Ela finaliza a função, ou seja, ela sai sa execcução da função
# - Podemos ter, em uma função, diferents returns
# - Podemos em uma função retornar qualquer tipo de dado e até mesmo mútiplos valores

# Exemplo 1:
def diz_ola():
    print('Estou sendo executado antes do retorno')
    return 'olá!'
    print('estou sendo execuatdo após o retorno')  # NADA após o retorno é executado.

print(diz_ola())

# Exemplo 2:
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3:
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
# OU SIMPLISMENTE:
print(outra_funcao())    #Lembra que em python gera-se tuplas automaticamentes quando existe virgulas
print(type(outra_funcao()))

# Vamos criar uma função da moeda: cara ou coroa:
from random import random

def joga_moeda():
    #Gera um número pseudo-randômico((mais ou menos(pseudo))NÚMEROS ALEATÓRIOS) entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# )bservação na utilização do retorno:
def e_impar():
    numero = 3
    if numero % 2 != 0:
        return True
    return False         # Observe e evite colocar um else, pq não tem necesssidade, nesse caso, se n é uma coisa é outra.

print(e_impar())