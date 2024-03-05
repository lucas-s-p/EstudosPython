# Entendendo o *args
# - O *args é um parâmetro como outro qualquer. Isso significa que vocẽ poderá chamar de qualquer coisa, desde que começe 
# com o asterisco.
# O parâmetro *args utilizado em função, coloca os valores extras informados como entrada em uma tupla. Então desde
# já lembre-se que  tuplas são imutáveis.

# Exemplos:
def soma_todos_numeros(num1=3, num2=9, num3=1):
    return num1 + num2 + num3

print(soma_todos_numeros(3, 6, 7))
print(soma_todos_numeros(2, 3))
# print(soma_todos_numeros(1, 2, 3, 4))

# Entendendo o args
def soma_todos(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos())
print(soma_todos(1))
print(soma_todos(2, 3))
print(soma_todos(4, 5, 9))
print(soma_todos(2, 5, 65, 78))

# OU
def soma_todos(*args):
  return sum(args)

print(soma_todos())
print(soma_todos(1))
print(soma_todos(2, 3))
print(soma_todos(4, 5, 9))
print(soma_todos(2, 5, 65, 78))

# OBSERVE:
def soma_todos(nome, sobrenome, *args):   # nome e sobrenome é obrigatório, já args não é.
  return sum(args)

print(soma_todos('Lucas', 'Pereira'))
print(soma_todos('Lucas', 'Pereira', 1))
print(soma_todos('Lucas', 'Pereira', 2, 3))
print(soma_todos('Lucas', 'Pereira', 4, 5, 9))
print(soma_todos('Lucas', 'Pereira', 2, 5, 65, 78))

#outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek!'
    return 'Eu não tenho certeza de quem vc é... '

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

# Exemplo 2:
def soma(*args):
    return(sum(args))

numeros = [1, 2, 3, 4, 5, 9, 50, 43]
# Desempacotador
print(soma(*numeros))    # O asterisco serve para informar ao python que estamos passando como argumento uma coleção,
                         # nesse caso, foi uma tupla. Desta forma ele saberá que deverá desempaacotar estes dados.
# Obs: Se voce não desempacotasse dessa forma teria que fazer o seguinte:

#numeros = [1, 2, 3, 4, 5, 9, 50, 43]
#num1, num2, num3, num4, num5, num6, num7, num8 = numeros
#print(soma(num1, num2, num3, num4, num5, num6, num7, num8))  # concorda que seria mais trabalhoso né 