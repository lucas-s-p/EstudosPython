def split_simplificado(frase, limitador):
    lista = []
    string = ''
    for e in range(len(frase)):
        if frase[e] != ' ':
            string += frase[e]
            if len(frase) -1 == e:
                lista.append(string)

        else:
            if string != '':
                lista.append(string)
                string = ''
    return lista

print(split_simplificado(' lucas testando', ' '))