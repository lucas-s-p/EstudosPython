#Estruturas logicas: and(e), or(ou), not(não), is(é)
#Operdores unários: not.
#operaadores binários: and, or, is.

#Para o and, ambos valores precisam ser True
#Para o Or, um ou outro valor precisa ser True 
#Para o not, o valor do booleano é invertido, ou seja, se for True, vira False, se for False, vira True.
#Para o is, o valor é comparado com o segundo.

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo usuário')
else: 
    print('Você preisa ativar sua conta.')

if not ativo:    #ativo = True   #not ativo = False
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

if ativo is True:   
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(ativo is False)    #ativo é Falso?
