# Funções com Parâmetro Padrão
# - Funções onde a passagem de parâmetro seja opcional

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
#print(quadrado())   # Type Error  # Parâmetro obrigatório

def exponencial(numero, potencia=2):    # Parâmetro de potência definido por padrão, OBSERVE QUE SE VC DEFINIR APENAS
    return numero ** potencia           # UM VALOR PADRÃO, SE TIVER MAIS DE UM PARAMETRO, ENT ESSE VALOR DEVE FICAR NO FINAL


print(exponencial(3, 5))
print(exponencial(3))   # Devido eu definir a potencia por padrão não precisa informar o segundo parâmetro
print(exponencial(23))
print(exponencial(3, 2))  # Obs que não tem problema usar os dois parametros, com o paramero definido diferente.

def mostra_informação(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que vc era o instrutor'
    return f'Olá {nome}'

print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação(True))
print(mostra_informação('Ozzy'))
print(mostra_informação(nome='Stefany'))

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))    # Por padrão utiliza a função soma como padrão, utilizando os vaalores destacados paraa num1 e num2
print(mat(2, 2, subtracao))  # Agr eu to dizendo para utilizar a função subratacao, utilizando num1 - num2

# Escopo - Evitar problemas e confunsões - Var globais e locais
instrutor = 'Geek'
def diz_oi():
    instrutor = 'python'   # Variável local, a local tem preferencia sobre uma global se as duas tiverem a msm nomeclatura.
    return f'oi {instrutor}'

print(diz_oi())

def incrementa():
    total = 0 # O melhor é evitar var. globais e tentar utilizar var. locais, como no exemplo q utiliza var. local, evita erros.
    total = total + 1
    return total

print(incrementa())

# OU
total = 0
def incrementa():
    global total # Mostrando que total é var. global e queremoos utilizar.
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declardas dentro de funções, e também uma forma especial de escopo de variável  
def fora():
    contador = 0
    def dentro():
        nonlocal contador    # nonlocal diz que ela não é local nem global, diz que tá na função anterior.
        contador = contador + 1
        return contador
    return dentro()

print(fora())   # sempre vai continuar em 1, pq quando a função volta ela zera
print(fora())
print(fora())

