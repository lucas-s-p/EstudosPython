def calcula(cpf):
    i = 2
    soma = 0
    for n in range(len(cpf) - 1, -1, - 1):
        soma += int(cpf[n]) * i
        i += 1
    return (soma * 10) % 11


def calcula_digitos_verificacao(cpf):
    digito1 = calcula(cpf)

    if digito1 == 10:
        digito1 = 0

    cpf_2 = cpf + str(digito1)

    digito2 = calcula(cpf_2)

    if digito2 == 10:
        digito2 = 0

    digitos_verificadores = str(digito1) + str(digito2)

    return digitos_verificadores

print(calcula_digitos_verificacao('153245873'))
