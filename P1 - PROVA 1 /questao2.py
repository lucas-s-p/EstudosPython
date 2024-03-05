# Programação | 2021.2
# Solução de "Diff Simétricos" https://p1ufcg.github.io/#/as/4936329387311104
# lucas.pereira@ccc.ufcg.edu.br

def diff_simetricos(valores):
    lista = []
    itera = 0
    for i in range(len(valores) // 2):
        itera -= 1
        lista.append(valores[i] -valores[itera])
       

    if len(valores) % 2 != 0:
        lista.append(valores[itera - 1])
    
    return lista

print(diff_simetricos([2, 5, 3, 9, 4]))