# Funções com parâmetro (de entrada)
# funções que recebem dados para serem processados dentro da mesma 
# entrada -> processamento -> Saída 

# Funções:
# - Não possuem entrada
# - Não possuem saída
# - Possuem entrada mas não possuem saída
# - Não possuem entrada mas possuem saída
# - Possuem entrada e saída

# refatorando uma função:
def quadrado(numero):
    #return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(100))

# Refatorando funções:
def cantar(aniversariante):
    print('Parabens para vc')
    print(f'Viva o {aniversariante}')

cantar('Lucas')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função quantos parâmetros
# forem necessários. eles são sseparados por vírgula.

# Exemplo:
def soma(a, b):
    return a + b

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(1, 2))
print(outra(3, 2, 'Lucas'))

def nome_com(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'


print(nome_com('Lucas', 'Pereira'))
# Parâmetro são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informálos, podemos utilizar qlq ordem
nome = 'opaió'
sobrenome = 'vanquer'

print(nome_com(sobrenome, nome))

print(nome_com(nome='Felipe', sobrenome='Spinola'))
print(nome_com(nome=nome, sobrenome=sobrenome))
print(nome_com(sobrenome='Marques', nome='Marcia'))

# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(soma_impares(lista))
