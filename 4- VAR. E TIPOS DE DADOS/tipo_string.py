#Tipo String
#Em python, um dado é considerado do tipo string sempre que estiver entre aspas simples, ou duplas, ou triplas simples ou duplas
# 'a' -> no python não existe caractere, isso é string
#'2345' -> tá entre aspas é string.

nome =  'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Geek Uniersity"
print(nome.upper())    #.upper é para deixar a string toda maiúscula.

nome = 'Lucas teste'
print(nome.lower())   #.lower é para deixar tudo minúsculo. ESSAS FUNÇÕES TÁ NO dir

nome = "Lucas Observe a criação de uma lista com o certo comando"
print(nome.split())   #.split cria uma lista com cada palavra após o espaço.

#exemplo inicial de vetores: 
#Observe que em 'Geek University' pode ser separado da seguinte forma:
#['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
#[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,   13,  14]  #posições
#Então:
nome = 'Geek University'
print(nome[0:4])     #lê da seguinte forma: nome que vai da posição zero até três, sempre uma posição a menos, pois começa no  zero.
                     #Chama-se esse processo de slice de tring

#para inverter:
#[::-1] -> comece no primeiro elemento, vá até o ultimo elemento e inverta
nome = 'Geek University'
print(nome[::-1])  #inversão da string

nome = 'Geek Uniiversity'
print(nome.replace('e', 'i'))  #.replace é para substituir as letras 