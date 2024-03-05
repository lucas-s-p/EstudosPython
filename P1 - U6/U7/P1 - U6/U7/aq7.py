tipo_servico = input()
if tipo_servico == '1' or tipo_servico == '2':
    m3 = float(input())

if tipo_servico == '3':
    print('R$ 50.00')
elif tipo_servico == '1':
    valor = m3 * 80
    if valor >= 200:
        print(f'R$ {valor:.2f}')
        print('Brinde!')
    else:
        print(f'R$ {valor:.2f}')
elif tipo_servico == '2':
    valor = m3 * 50
    if valor >= 200:
        print(f'R$ {valor:.2f}')
        print('Brinde!')
    else:
        print(f'R$ {valor:.2f}')