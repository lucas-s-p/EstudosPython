# Modelo collections - Named Tuple
# Named Tuple -> São tupla, difernciada, onde, especificamos um  nome para a mesma e também parãmetros.

from collections import namedtuple

#Observe trẽs formas de expresssar a mesma coisa
# Forma 1 - Declarando Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declarando named Tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declarando Named tuple - Mais recomendada
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando:
ray = cachorro(idade=2, raca='chow-chow', nome='Ray')
print(ray)

#Acessando os dados:
print(ray[0]) #pegando  o elemento 0
print(ray[1]) #pegando  o elemento 1
print(ray[2]) #pegando  o elemento 2

#Forma 2 
print(ray.idade)
print(ray.raca)
print(ray.nome)


