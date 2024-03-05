# Definindo funções 
# Funções são pequenos trechos de códigos que realizam tarefas específicas
# Já utilizamos várias funções: exemplos: print(), len(), max(), count(),....
# pode ou não receber entradas de dados e retornar uma saída de dados
# OBS: Se vc escrever uma função que realiza várias tarefas dentro delas é bom fazer uma verificação para que 
# a função seja simplificada.

# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Bult-in) do python print()
print(cores)

# Em python, a forma geral de definir uma função  é:
# def nome_da_funcao(parametros_de_entrada):
#    bloco_da_funcao

# onde: 
# nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto,  seprado por underline (Snake Case);
# parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
# bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste 
# bloco pode ter ou não retorno da função.

# Obs: para  definir a função, utilizamos a palavra 'def' informando ao python que estamos definindo uma função.
# Também abrimos blocos com o já conhecido dois pontos : ue é utilizado em python para definir blocos.

# Definindo a primeira função
def diz_oi():
    print('oi!')   
#Obs: podemos ter outra função dentro da função que foi definida
#obs: a função não recebe nenhum parâmetro de entrada, é possível ver pelos () vazios.
#obs: observe que não retorna nada
# Obs: se apenas definir ela não será execuda no terminal, tem q fazer a chamada de execução

# Utilizando funções
# chamada de execução
diz_oi()

# Exemplo 2:
def cantar_parabens():
    print('Parabens para vc')
    print('nesta data querida')

cantar_parabens()       # Pode executar qts vezes quiser
cantar_parabens()
cantar_parabens()

# utilizando um loop for:
for n in range(5):
    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função atráves da variável
canta = cantar_parabens       #não é muito utilizado
canta()

