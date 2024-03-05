# PROGRAMA 1:

def acumula(lista):
  soma = 0
  for num in lista:
    soma += num
  return soma

def main():
  dados = input().split()

  for i in range(len(dados)):
    dados[i] = int(dados[i])
  
  print(acumula(dados))

if __name__ == "__main__":
  main() 

# PROGRAMA 2:

def aplica_imposto(valores):
  novo = [] 
  for valor in valores:
    novo.append(valor * 1.1) 
  
  return novo

def main():
  dados = input().split()

  for i in range(len(dados)):
    dados[i] = float(dados[i])
  
  dados_impostos = aplica_imposto(dados)

  for dados in dados_impostos:
    print(f'{dados:.2f}')

if __name__ == "__main__":
  main()

# PROGRAMA 3:

def meu_minimo(lista):
  min = None
  for num in lista:
    if min == None or num < min:
      min = num
  
  return min

def main():
  dados = input().split()
  for i in range(len(dados)):
    dados[i] = int(dados[i])
  
  print(meu_minimo(dados))

if __name__ == "__main__":
  main()

# PROGRAMA 4:

def conta_vogais(executa):
  vogais = 0
  for letra in executa:    # Se liga os parâmetros passados não precisam ser iguais. dentro da função vc  precisa relacionar
    if letra in "aeiouAEIOU":  # o parâmetro, mas com outra função não necessariamente precisa ser igual.
      vogais += 1              # def conta_vogais(palavra) ou def conta_vogais(executa) funciona da mesma forma.
  
  return vogais

def main():
  cont = 0
  while True:
    palavra = input()
    if palavra == 'fim': break
    cont += conta_vogais(palavra)
  
  print(f'Num de vogais: {cont}')

if __name__ == "__main__":
  main()