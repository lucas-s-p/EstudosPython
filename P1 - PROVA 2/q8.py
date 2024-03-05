def meu_in(frase, car):
    for i in range(len(car)):
        if car[i] ==  frase:
            return True

    return False

def vogais_primeiro(frase):
    str_e = ''
    str_vo = ''
    for i in range(len(frase)):
        if meu_in(frase[i], 'aeiou'):
            str_vo += frase[i]
        else:
            str_e += frase[i]
            
    final = str_vo + str_e

    return final

print(vogais_primeiro('exemplo'))