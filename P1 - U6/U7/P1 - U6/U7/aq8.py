num_times = int(input())

times = []
for i in range(num_times):
    time = input()
    gols = input()
    times.append([time, gols])


pos = 1
cont = 1
anterior = None
if num_times != 0:
    anterior = times[0][1]

for indice in range(len(times)):
    if times[indice][1] != anterior:
        pos = cont
        anterior = times[indice][1]
        print(f'{pos}. {times[indice][0]} ({times[indice][1]})')
    else:
        print(f'{pos}. {times[indice][0]} ({times[indice][1]})')
    cont += 1

