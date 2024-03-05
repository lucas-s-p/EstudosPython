senha_atual = input()
nova_senha = input()

if len(senha_atual) > len(nova_senha):
    itera = len(nova_senha)
else:
    itera = len(senha_atual)

achou = False
for i in range(itera):
    if senha_atual[i] == nova_senha[i]:
        achou = True
        print(f"'{senha_atual[i]}' coincidente na posição {i + 1}")
       
if achou:
    print('Senha não alterada')
else:
    print('Senha alterada com sucesso')

