# Implementa a função in
def esta_em(car, palavra):
    for e in palavra:
        if e == car:
            return True
    return False

# Exemplo usando o in
palavra = input()
for i in range(len(palavra) - 1):
    if esta_em(palavra[i + 1], 'aeiou'):
        print(palavra[i])