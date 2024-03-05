# Módulo collections - Default Dict
# Default Dict -> Ao criar um dicionário utiilizando o default dict, nós informamos um valor default, 
# podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido. Em caso de 
# acessar uma chaave que não existe, essa chave será criada e o valor default será atribuido.

dicionario = {'curso': 'Programação em python'}
print(dicionario)
print(dicionario['curso'])
#print(dicionario['outro'])   # em dicionários da erro, mas em Default dict não 

from collections import defaultdict

dicionario = defaultdict(lambda: 0)              # lambda são funções sem nome.

print(dicionario)

dicionario['curso'] = 'Programação em python'
print(dicionario)
print(dicionario['outro'])  # ele aadiciona a chave, não dá erro como no caso se fossse dicionários
print(dicionario)

