def tem_afinidade(l1, l2):
    cont = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                cont += 1
                break
    if cont >= 3:
        return True
    else:
        return False

print(tem_afinidade(['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2'], ['zeze', 'joao', 'u2', 'jquest']))