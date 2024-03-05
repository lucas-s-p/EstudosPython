# Módulo Collections: Ordered Dict

# Em dicionários a ordem não é garantida, diferentemente de ordered dict que mantem a ordem

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
for chave, valor in dicionario.items():
    print(f'chave = {chave}:Valor = {valor}')


