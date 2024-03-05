
def diff_simetricos(valores):
    lista = []
    iterador = -1
    for i in range(len(valores) // 2):
        lista.append(valores[i] - valores[iterador])
        iterador -= 1

    if len(valores) % 2 != 0:
        lista.append(valores[i + 1])

    return lista

print(diff_simetricos([2, 5, 3, 9, 4]))

def test_exemplo_1():
    lista1 = [2, 5, 3, 9]
    assert diff_simetricos(lista1) == [-7, 2]
    assert lista1 == [2, 5, 3, 9]

def test_exemplo_2():
    lista2 = [2, 5, 3, 9, 4]
    assert diff_simetricos(lista2) == [-2, -4, 3]
    assert lista2 == [2, 5, 3, 9, 4]