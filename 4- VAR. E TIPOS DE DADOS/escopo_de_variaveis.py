#Escopo de Variáveis

#dois casos:
# 1- Variáveis globais:
#   -variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
#2- variáveis locais:
#  -variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
#está limitado ao bloco onde foi declarda.

#Para declarar variáveis em python fazemos:

#nome_da_variavel = valor_da_variavel

#vale lembrar que python é uma linguagem de tipagem dinâmica. Isso significa que
#ao declararmos uma variável, nós não colocamos o tipo de dado dela. Este tipo é inferido
#ao atribuírmos o valor à mesma.

numero = 42  #Exemplo de variável global que tem acesso a todo processo.
print(numero)
print(type(numero))

numero = 42  
if numero > 10:  #em python abre um bloco com dois pontos
    novo = numero + 10   #exemplo de variavel local, está sendo limitada, ou seja, se numero fosse menor que 10, a variavel novo  
    print(novo)          #não existiria.
