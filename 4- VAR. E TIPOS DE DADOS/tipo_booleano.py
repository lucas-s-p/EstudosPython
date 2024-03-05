#Tipo Booleano
#Esse nome vem da álgebra booleana, crriada por George Boole
# 2 constantes: Verdadeiro ou Falso

#Com letra inicial maiúscula: True: é verdadeiro e False: é Falso

ativo = False
print(ativo)

#Operações básicas:

#Negação (not):
#Fazendo a negação, se o valor booleano for veradeiro o resultado será falso,
#se for falso o resultado será verdadeiro.

print(not ativo) #faz o processo inverso.

#Ou (or):
#é uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser veradeiro.

#True or True ->  True
#True or False -> True
#False or True -> True
#False or False -> False

logado = False
print(ativo or logado)

#E (and):
#Também é umaa operação binária. Ou seja, depende de dois valores

#True and True -> True
#True and False -> False
#False and True -> False
#False and false -> False


