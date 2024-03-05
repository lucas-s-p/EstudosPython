def pivot(numeros):
    for i in range(len(numeros)):
        if numeros[0] == True:
            if numeros[i] < numeros[0]:
                numeros[i], numeros[0] = numeros[0], numeros[i]
    
    return numeros

numeros = [6, 4, 8, 1, 7, 3]
print(pivot(numeros))