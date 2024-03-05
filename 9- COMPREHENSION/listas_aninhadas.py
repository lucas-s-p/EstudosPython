# Listas Aninhadas
# Algumas linguagens de programação possuem uma estrutura de dados chamada arrays:
# - Unidimensionais (Arrays/Vetores);
# - Multidimensionais (Matrizes);
# Em python nós temos as Listas:
# numeros = [1, 2, 'a', 3.233, True, 3, 4, 5]


# Exemplos:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Isso é a matriz em python
print(listas)
print(type(listas))

# Como fazer para acessar os dados ?
print(listas[0])     # observe que vai imprimir toda a primeira lista, pois é considerda como o indice zero.
print(listas[0][2])   # agora acesso a lista da posição zero e o elemento na posição dois.
# Linha zero, coluna 2

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List comprehension
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos:
# Gerando um tabuleiro/matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]  # primeiro for gera coluna, o segundo for gera linhas.
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
