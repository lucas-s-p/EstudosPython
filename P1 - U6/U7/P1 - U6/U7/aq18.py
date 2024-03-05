def meu_in(elemento, car):
    for i in car:
        if elemento == i:
            return True

    return False

def quase_fonemas(palavra):
    lista = []
    for i in range(len(palavra) - 1):
        if meu_in(palavra[i + 1], 'aeiou'):
            if not meu_in(palavra[i], 'aeiou'):
                lista.append(f'{palavra[i]}{palavra[i + 1]}')
    return lista

assert quase_fonemas("computador") == ['co', 'pu', 'ta', 'do']
assert quase_fonemas("exemplo") == ['xe', 'lo']
assert quase_fonemas("arara") == ['ra', 'ra']