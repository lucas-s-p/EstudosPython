# Documentando funções com Docstrings

# Exemplos:
def diz_oi():
    """ Uma função simples que retorna a string 'oi!' """    # cria uma documentação e depois é possível acessar.
    return 'oi!'

print(diz_oi())
print(help(diz_oi()))

from docstrings import diz_oi
diz_oi.__doc__

# OBS: Podemos acesssar a documentação de uma função em python utilizando a propriedade
# especial __doc__
# Podemos ainda ter acesso a documentação com a função help()
print(diz_oi.__doc__)
print.__doc__
help.__doc__
