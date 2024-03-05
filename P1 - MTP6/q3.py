def vogais_primeiro(frase):
    saida = ''
    saida2 = ''
    for e in frase:
        if e in "aeiou":
            saida += e
        else:
            saida2 += e
    saida_ = saida + saida2
    
    return saida_

print(vogais_primeiro('Programacao 1'))
