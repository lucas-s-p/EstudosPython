# Módulo collections - counter
# collections -> High-performance Container Datetypes
# Counter -> Recebe um interável como parâmetro e cria um objeto do tipo collections counter que é parecido
# com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a qtd de ocorrências
# desse elemento.

# Utilizando o counter: Exemplo 1
from collections import Counter

# Poderia ser qlq iteravel: Exemplo: dicionario, tuplas, conjuntos
lista = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 7, 56, 56, 57, 45, 45, 45, 65]

#utilizando o counter
res = Counter(lista)    #ele mostra o numero de ocorrencias de cada elemento, ou seja, qts vezes ele aparece.
print(type(res))        #o counter cria uma chave com o 'elemento':número de ocorrências
print(res)

#Exemplo 2
from collections import Counter
print(Counter('Geek University'))  #'caractere':numero de ocorrencias

# Exempllo 3

texto = """Por outro lado, o texto literário é mais artístico, com uma função estética, que tem como objetivo recreativo, 
provocando diferentes emoções no leitor. Assim, os textos literários nem sempre estão ligados à realidade (no caso da ficção) 
e muitas vezes são subjetivos, podendo existir diferentes interpretações de leitores distintos. Além disso, o texto literário 
contém figuras de linguagem, sentido figurado e metafórico das palavras, que tornam o texto mais expressivo. """

palavras = texto.split()
#print(palavras)
res = Counter(palavras)
print(res)
print(res.most_common(5))       #encontrando as 5 palavras com mais ocorrẽncias.

