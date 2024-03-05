from undertst import diff_simetricos

def test_comleviepedro():
    assert diff_simetricos([10, 2, 4, 8]) == [2, -2]
def test_zero():
    assert diff_simetricos([10, 10]) == [0]
def test_impar():
    assert diff_simetricos([15, 4, 10]) == [5, 4]
def test_par():
    assert diff_simetricos([15, 4, 8, 10]) == [5, -4]
def test_mais_elementos():
    assert diff_simetricos([10, 3, 4, 6, 10]) == [0, -3, 4]
def test_lista_zeros():
    assert diff_simetricos([12, 8, 4, 4, 8, 12]) == [0, 0, 0]
def test_lista_zeros_impar():
    assert diff_simetricos([12, 8, 4, 5, 4, 8, 12]) == [0, 0, 0, 5]