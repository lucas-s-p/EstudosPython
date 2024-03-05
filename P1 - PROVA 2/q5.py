pal1 = input()
pal2 = input()

if len(pal1) > len(pal2):
    itera = len(pal2)
else:
    itera = len(pal1)

print(f'Letras Coincidentes')
cont = 1
cont_in = 0
for i in range(itera):
    if pal1[i] == pal2[i] and i != 0:
        cont_in += 1
        cont += 1
        print(f"'{pal1[i]}' na posição {cont}")
    elif pal1[0] == pal2[0]:
        print(f"'{pal1[i]}' na posição {cont}")


por = (100 * cont_in) / (len(pal1) + len(pal2))
print(f'Total de letras coincidentes: {cont_in} ({por:.2f}%)')

