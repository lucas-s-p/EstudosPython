def idiff(seq1, seq2):
    if len(seq1) >= len(seq2):
        index = len(seq2)
        op = len(seq1)
    else:
        index = len(seq1)
        op = len(seq2)

    lista = []
    for i in range(index):
        if seq1[i] != seq2[i]:
            lista.append(i)
            
    if index != op:
        for j in range(index, op):
            lista.append(j)

    return lista

seq1 = [10, 20, 30, 40, 50, 60, 70]
seq2 = [10, 20, 20, 40, 80]
assert idiff(seq1, seq2) == [2, 4, 5, 6]