def conta_diferentes(s1, s2):
    if len(s1) > len(s2):
        index = len(s2)
    else:
        index = len(s1)

    cont = 0
    for i in range(index):
        if s1[i] != s2[i]:
            cont += 1

    return cont

assert conta_diferentes('aaa', 'bbb') == 3
assert conta_diferentes('oi', 'ola') == 1
assert conta_diferentes('ola', 'oi') == 1


