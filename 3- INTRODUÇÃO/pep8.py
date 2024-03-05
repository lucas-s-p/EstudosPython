#from platform import python_branch
#PEP8 - propostas de melhorias para linguagem python
#A ideia da PEP8 é que possamos escrever códigos python de forma pythônica.



#Utilize camel case para nomes de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


#utilize nomes em minusculo, separados por underline para funções ou variáveis.


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5


#utilize 4 espaços para IDENTAÇÃO. São os 4 espaços necessários, por ex na função print.


if 'a' in 'banana':
    print('tem')


#linhas em branco. Duas linas vazia após definir uma classe.

#Import devem ser feitas em linhas separadas 
import sys
import os
#exeções para import de mesmo pacote
from types import StringType, ListType
#caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
from types import(
    StryngType,
    ListType,
    SetType,
    OutroType
)

#imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e 
# antes de constanntes ou variáveis globais.

#não deixe espaços em instruções e expressões.
#termine sempre uma instrução com uma nova linha.