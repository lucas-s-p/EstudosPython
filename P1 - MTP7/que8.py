def remove_abaixo_media(l1):
    soma = 0
    for i in range(len(l1)):
        soma += l1[i]

    media = soma/len(l1)
    for i in range(len(l1)-1, -1, -1):
        if l1[i] < media:
            l1.pop(i)
    return l1

l1 = [1, 1, 1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]


l1 = [1, 1, 1, -1, 1]
remove_abaixo_media(l1)
assert l1 == [1, 1, 1, 1]