calc = lambda x: x*3 + 1
print(calc(4))




nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

# Função strip: tira od espaços em brancos no inicio e final de uma string.
nome = 'lucas '
sobrenome = 'pereira ' # Strip tira o espaço em branco
print(nome_completo(nome, sobrenome))




itera = lambda numero: [(i + 5) for i in numero if i > 4]

print(itera([3, 2, 65, 78]))




autores = ['Isac Fontes', 'Fernando Cardoso', 'Maria Ventura Passos', 'Antônio Passos']

autores.sort(key=lambda sobrenome: sobrenome.split()[-1].lower())

print(autores)




def fun_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

print(fun_quadratica(3, 0, 1)(2))