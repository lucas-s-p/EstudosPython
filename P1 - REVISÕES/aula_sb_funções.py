from tkinter import Y


def dobro(x):
    return 2 * x        # Identação: São os 4 espaços 

x = dobro(10) + dobro(3)
print(x)


# debugging : Ajuda a resolver os problemas, executando em partes.
# Linhas indentadas são executas por ultimo.
def dobro(x):
    y = 2 * x
    print(f'>>>> y = {y}, x = {x}')        # todas as ocorrências durante a execução.
    return y 

a = 10
x1 = dobro(a)
x2 = dobro(dobro(3))
x = dobro(x1 + x2)
print(x, a)

def dobro(x):
    x = 2 * x
    return x

x = 123                      # VC TENDO DUAS VARIÁVEIS COM O MESMO NOME NÃO IMPLICA EM VALORES IGUAIS, E SIM SGNIFICA QUE
y = dobro(x)                 # AS  VARIÁVEIS PODEM TER VALORES DIFERENTES, NESSE CASO, O X ESTÁ DEFINIDO APENAS DENTRO DA 
print(y, x)                  # FUNÇÃO, O OUTRO X É OUTRO VALOR, ISSO É PELO FATO DO ESCOPO DE VARIÁVEIS.

def dobro():
    global x         # definindo global os dois x passam a ter os mesmos valores.
    x = 2 * x
    return x

x = 123
y = dobro()
print(y, x)


_count = 0
def dobro(x):
    global _count      # Conta o número de vezes que a  função foi executada.
    y = 2 * x
    _count += 1
    return y 

a = 10
x1 = dobro(a)
x2 = dobro(dobro(3))
x = dobro(x1 + x2)
print(x, a, _count)

a = 123
b = 123.0
c = a + b   #Quando  há uma operação de ponto flutuante e inteiro o python, python promove um dos dois, um pode virar o outro
            # normalmente int vira float. Isso é chamado de coerção. NÕ TEM COERÇÃO PARA STR.
print(c)

z = 'caso' < 'casa'  # Não é pela quantidade de carcateres e sim por quem vem primeiro no alfabeto. 
print(z)             # Ou seja, quem vem primeiro é menor, no exemplo 'a' é menor que 'o'.  

# Numero em str com texto em str:  Numero é menor que str.
s = '10' < 'a'
print(s)

# OBS:
x = 0.1 + 0.1 + 0.1    # existe uma aproximação em python de 0.1 e sua soma de 0.1 + 0.1 + 0.1 = 0.3000000004 
a = 0.3
print(x > a)  

# OBS:
e = 0.3
f = 0.3
print(e == f)