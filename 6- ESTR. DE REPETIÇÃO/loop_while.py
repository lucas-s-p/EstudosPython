#Loop While
#Forma geral
# whilw expressão_booleana:
#     //execução do loop
# o bloco do while será  repetido enquanto a expressão booleana for  verdadeira.
#Expressão booleana é toda expressão onde o resultado é falso ou verdadeiro.

numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
    
#numero = 1
#while numero < 10:          #loop infinito, o 1 é menor do que 10, então vai imprimir o 1 sem parar.
    #print(numero)

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou jéssica ?')


