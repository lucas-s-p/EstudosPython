def meu_in(car, c):
    for e in car:
        if e == c:
            return True
    return False

def vogais_primeiro(frase):
    saida = ''
    saida2 = ''
    for c in frase:
        if meu_in('aeiou', c):
            saida += c
        else:
            saida2 += c
    saida_ = saida + saida2
    
    return saida_

print(vogais_primeiro('Arogramacao 1'))