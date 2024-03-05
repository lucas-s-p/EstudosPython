#FORMA ATUALIZADA, NOVA, A PARTIR  DA VERSÃO PYTHON3: 1° Forma

#print('Qual seu  nome?')
#nome = input()

#print('Seja bem-vindo {0}' .format(nome))

#FORMA ATUALIZADA, NOVA, A PARTIR  DA VERSÃO PYTHON3: 2° Forma (MAIS ATUAL)

#print('Qual seu nome?')     
#nome = input()

#essa forma que está acima pode ser abreviada para: 
nome = (input('Qual o seu nome?'))

print(f'seja bem-vindo {nome}')   #o f é como se fosse o format  da 1° forma.

#print('Qual a sua idade?')
#idade = input()

#essa forma que está acima pode ser abreviada para:
#Além disso o cast pode já ser feito aqui:
idade = int(input('Qual a sua idade?'))

#Saída
print(f'O(a) {nome} tem {idade} anos')   #LEMBRA DO f !!!!

#Observe também:
print(f'O(a) {nome} nasceu em {2022 - idade}')
#print(f'O(a) {nome} nasceu em {2022 - int(idade)}')      #int(idade) = cast

#input() -> Todo dado recebido via inupt é do tipo string
#int(idade) = cast -> Cast é a conversão de um tipo de dado para outro. Ou seja, nesse caso do exemplo é a conversão de string
#para inteiro.

#OBS: ESSA FORMA PERMITE A REALIZAÇÃAO DE CÁLCULOS


