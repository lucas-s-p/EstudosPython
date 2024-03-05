def inverte3a3(s):
    l = []
    cont = 0
    string = ''
    for i in range(len(s)):
        cont += 1
        string += s[i]
        if cont % 3 == 0:
            l.append(string)
            string = ''

    saida = ''
    for e in range(len(l) -1, -1, -1):
        saida += l[e]
    
    return saida

print(inverte3a3('abcdefghijkl'))