def encontra_idoso(fila, elemento):
    idoso = fila[elemento]
    for i in range(elemento, len(fila)):
        if fila[i] >= 60 and fila[i] > idoso:
            idoso = fila[i]
            break

    for i in range(len(fila)):
        if fila[i] == idoso:
            indice = i
    return indice

def idosos_inicio(fila):
    for i in range(len(fila)):
        idoso = encontra_idoso(fila, i)
        fila[idoso], fila[i] = fila[i], fila[idoso]
    return fila

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

