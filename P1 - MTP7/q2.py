def split_simplificado(frase, limitador):
    lista = []
    string = ''
    for e in frase:
        if e not in limitador:
            string += e
        elif string:
            lista.append(string)
            string = ''
    
    if string:
        lista.append(string)
    return lista

assert split_simplificado('um exemplo') == ['um','exemplo']
assert split_simplificado('um exemplo') == 'um exemplo'.split()
assert split_simplificado('testando') == 'testando'.split()