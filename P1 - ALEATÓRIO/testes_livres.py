time = input().split()
pontuacao = input().split()
num_partidas = int(input())

for pontos in range(len(pontuacao)):
    pontuacao[pontos] = int(pontuacao[pontos])

def atualiza_pontos(soma_lista, time, pontuacao):
    for i in range(len(time)):
            if soma_lista[0] == time[i] and soma_lista[1] > soma_lista[2]:
                pontuacao[i] += 3
            elif soma_lista[3] == time[i] and soma_lista[2] > soma_lista[1]:
                pontuacao[i] += 3
            elif soma_lista[0] == time[i] and soma_lista[1] == soma_lista[2]:
                pontuacao[i] += 1
            elif soma_lista[3] == time[i] and soma_lista[2] == soma_lista[1]:
                pontuacao[i] += 1
    return pontuacao

def lider_lanterna(soma_lista, time, pontuacao):
    tabela = atualiza_pontos(soma_lista, time, pontuacao)
    maior = 0
    menor = 0
    for v in range(len(tabela)):
        if maior == 0 or maior < tabela[v]:
            maior = tabela[v]
            lider = time[v]
        if menor == 0 or menor >= tabela[v]:
            menor = tabela[v]
            lanterna = time[v]   
    print(f'Líder: {lider}')
    print(f'Lanterna: {lanterna}')

def main():
    for n in range(num_partidas):
        partida = input().split('x')
        separa_resul1 = "".join(partida[0])
        separa_resul2 = "".join(partida[1])
        separa_time_placar1 = separa_resul1.split()
        separa_time_placar2 = separa_resul2.split()
        soma_lista = separa_time_placar1 + separa_time_placar2
        atualiza_pontos(soma_lista, time, pontuacao)
    lider_lanterna(soma_lista, time, pontuacao)
    
if __name__ == "__main__":
  main()