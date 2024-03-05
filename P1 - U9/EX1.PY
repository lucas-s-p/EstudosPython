def filtra_alunos(alunos, inscritos, media):
    cont = 0
    for i in range(len(alunos) -1, -1, -1):
        if alunos[i][-1] < media:
            alunos.pop(i)
            cont += 1

    for i in range(len(alunos) -1, -1, -1):   
        for j in range(len(inscritos)):
            if alunos[i][0] == inscritos[j]:
                break
            elif len(inscritos)-1 == j:
                alunos.pop(i)
                cont += 1
                  
    return cont

inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]
