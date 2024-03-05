#Rangers
#Precisamos conhecer o loop for para usar os ranges
#Precisamos conhecer o range para trabalhar melhor com loops for
#Rangers são utilizados para gerar sequências númericas, não de forma aleatória, mas sim de maneira especcificada.

#Formas gerais:
#range(valor_de_parada)
#Obs: valor_de_parada não inclusive (inicio padrão é 0, e passo de 1 em 1)

#Forma 1:
for num in range(11):     #se não especificar começa no zero
    print(num)

#Forma 2:
for num in range(1, 11):
    print(num)

#forma 3:
for num in range(1, 10, 2):   # 0 2 singiifica o passo, diz: vai de 1 a 10 com passo de 2 em 2,, ou seja, vai imprimir 1,3,5,7,9
    print(num)

#forma 4:
for num in range(10, 0, -1):  #decrementação de 1 em 1, ou seja, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1  #LEMBRA QUE O ÚLTIMO NÃO CONTA.
    print(num)

#Usando python para ver a lista gerada teria que ser:
# lista = list(range(10))
# lista
