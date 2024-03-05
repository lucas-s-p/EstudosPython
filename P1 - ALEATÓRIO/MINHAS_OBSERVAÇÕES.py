variavel = 10
print(str(variavel))
variavel += 10

idade = int(input('Qual a sua idade: '))
print(f'A sua idade é: {idade}')

numeros = [5, 6, 7, 8, 7, 9, 10]
print(numeros.index(6))


carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto !=  'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

nome = 'prog1'
print(f'imprima prog1 ocupando 10 esspaços e complete com asteriscos os espaços vazios: {nome:*^10s}')  
print(f'imprima prog1 ocupando 10 esspaços e complete com asteriscos os espaços vazios: {nome:>10s}') 

nome = 'lucas'
print(nome.lower())
