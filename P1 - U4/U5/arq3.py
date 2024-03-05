def string_menos_ultima(palavra):
    saida = ''
    for i in range(len(palavra) - 1):
        saida += palavra[i]

    return saida


s1 = input()
s2 = input()

for i in range(len(s2)):
    indices = ''
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            indices += f'{j} '
    if not indices: indices = '-1 '
    print(string_menos_ultima(indices))