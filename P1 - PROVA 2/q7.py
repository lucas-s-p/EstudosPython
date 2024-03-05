def meu_in(pentavogalica, car):
    for e in car:
        if e == pentavogalica:
            return True
    
    return False

def encontra_penta(seq):
    cont = 0
    cont_global = 0
    for i in range(len(seq)):
        if seq[i] != ' ':
            if meu_in(seq[i], 'aeiou'):
                cont += 1
            if cont == 5:
                cont_global += 1
        else:
            cont = 0
    
    return cont_global

print(encontra_penta('mandinga juazeiro cajueiro sequoia pirilampo'))


