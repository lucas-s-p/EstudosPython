# Entendendo **kwargs
# Poderiamos chamar este parâmetro de **qualquernome
# **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo: 
def cores_fav(a, b, c, **kwargs):
    print(kwargs)
    
cores_fav(1, 2, 3, marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')  #cria um dicionário

# exemplo:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')   # title(): deixa a primeira letra maiúscula.
    
cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')  #cria um dicionário.

# OBS: os parãmetros *args e **kwargs não são obrigatórios
cores_favoritas()
cores_favoritas(geek='navy')

# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você perdeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas funções podemos ter:  Se fizer  uma função tem que estar nesta ordem:
# parâmetros obrigatórios
# *args
# Parâmetros não obrigatórios
# **kwargs

def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_função(8, 'Julia')
minha_função(18, 'Felicty', 4, 'a', 3, solteiro=True)
minha_função(34, 'Felipe', eu='Não', voce='Vai')
minha_função(19, 'carla', 9, 4, 3, java=False, python=True)

# Entenda porque é importante a ordem dos parâmetros na declaração
def mostra_info(a, b,*args, instrutor='Geek', **kwargs):  # se tivesse em outra ordem não ficaria certo o código.
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor')) 

# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicty', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))   #Desempacotamento de forma simples. Igual ao *args

# exemplo:
def soma_mtp_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_mtp_numeros(*lista)
soma_mtp_numeros(*tupla)
soma_mtp_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_mtp_numeros(**dicionario)  # Obs: os nomes devem ser o mesmo dos parâmetros da função, ou seja, no ex: tem q ser a, b e c.

#dicionario = dict(e=1, f=2, c=3) # NÃO DARIA CERTO, CHAVE DIFERENTE DOS PARÂMETROS
#soma_mtp_numeros(**dicionario, lang='python') # posso até passar  outras coisas, mas teria que colcar *kwargs  no def.
