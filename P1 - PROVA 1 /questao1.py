# Programação | 2021.2
# Solução de "Altera Senha" https://p1ufcg.github.io/#/as/6293883736555520
# lucas.pereira@ccc.ufcg.edu.br

senha_atual = input()
nova_senha = input()

pos = 0
achou_coincidente = 0
for e in range(len(senha_atual)):
    pos += 1
    for letra in range(len(nova_senha)):
        if senha_atual[e] == nova_senha[letra]:
            if e == letra:
                achou_coincidente += 1
                print(f"'{nova_senha[letra]}' coincidente na posição {pos}")
    
                
if achou_coincidente > 0:
    print('Senha não alterada')
if achou_coincidente == 0:
    print('Senha alterada com sucesso')
