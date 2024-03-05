def remove_caracteres(frase, caracteres):
    string = ''
    for c in range(len(frase)):
        for e in range(len(caracteres)):
            if caracteres[e] == frase[c]:
                break
            elif (len(caracteres) - 1) == e:
                string += frase[c]
    return string

print(remove_caracteres("Apalavrados", "sodA"))