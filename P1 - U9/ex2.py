def matriz_menor(M1, M2):
    M3 = []
    for i in range(len(M1)):
        M_auxiliar = []
        for j in range(len(M1[i])):
            if M1[i][j] <= M2[i][j]:
                M_auxiliar.append(M1[i][j])
            else:
                M_auxiliar.append(M2[i][j])
        if len(M_auxiliar) == 3:
            M3.append(M_auxiliar)
            M_auxiliar = []
    
    return M3 

M1 = [[1,2,3],
      [13,14,15],
      [7,8,9]]

M2= [[10,11,12],
     [4,5,6],
     [7,8,9]]

M3= [[1,2,3],
     [0,0,0],
     [7,8,9]]

print(matriz_menor(M1, M2))