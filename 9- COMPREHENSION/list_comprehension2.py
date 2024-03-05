# Lista Comprehension - Parte 2
# Nós podemos adiccionar esruturas condicionais lógicas as list comprehension

# Exemplos:
numeros = [1, 2, 3, 4, 5, 6]

pares =  [numero for numero in numeros if numero % 2 == 0]
impares =  [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer número par módulo de 2 é 0 e 0 em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer número ímpar módulo de 2 é 1, e 1 em python é True  
impares = [numero for numero in numeros if not numero % 2]

print(pares)
print(impares)

# OBS: 
numero = 1
numero % 2  # numero módulo de 2 da resto 1
numero = 4
numero % 2 # numero módulo de 2 da resto 0
# zero é falso em python, logo, para torna-se True coloca o not

res = [numero * 2 if numero % 2 == 0 else numero/2 for numero in numeros]
print(res)