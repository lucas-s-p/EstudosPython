def meu_in(pentavogalica, car):
    for e in car:
        if e == pentavogalica:
            return True
    
    return False

def encontra_penta(seq):
    palavras = seq.split()
    cont = 0
    cont_global = 0
    for i in range(len(palavras)):
        for v in range(len(palavras[i])):
            if meu_in(palavras[i][v], 'aeiou'):
                cont += 1
            if (len(palavras[i][v])-1) == v:
                if cont == 5:
                    cont_global += 1
                cont = 0
    
    return cont_global

print(encontra_penta('mandinga juazeiro cajueiro sequoia pirilampo'))


