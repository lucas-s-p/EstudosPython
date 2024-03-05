# List comprehension
# Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.
# Sintaxe da list comprehension:
# [dado for dado in iterável]

# Exemplos:
numeros = [1, 2, 3, 4, 5]

res = [num * 10 for num in numeros] # melhor ler assim: "para cada num dentro da lista de numeros mutiplique num * 10"
print(res)                          # gerando assim uma lista.

# Usando funções:
def funcao(valor):
    return valor * valor

res = [funcao(num) for num in numeros]
print(res)

# List comprhension versos loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List comprehension
print([numero * 2 for numero in numeros])

# Exemplo:
nome = 'Geek University'
print([letra.upper() for letra in nome])

#Exemplo:
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())  # replace substitui uma parte por outra, nesse esxemplo tá transformando as 
    return nome                                    # as primeiras leetras em maiúsculas. letras na posição zero.

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])

# Exemplo:
print([numero * 3 for numero in range(1, 10 + 1)])

# Exemplo:
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo:
print([str(numero) for numero in [1, 2, 3, 4, 5]])
