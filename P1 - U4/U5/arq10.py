def calcula_digitos_verificacao(cpf):
    i = 2
    soma = 0
    for n in range(len(cpf) - 1, -1, - 1):
        soma += int(cpf[n]) * i
        i += 1
    
    digito1 =  (soma * 10) % 11
    cpf_2 = cpf + str(digito1)

    i = 2
    soma_2 = 0
    for n in range(len(cpf_2) - 1, -1, - 1):
        soma += int(cpf_2[n]) * i
        i += 1

    digito2 =  (soma_2 * 10) % 11

    if digito1 == 10:
        digito1 = 0
    if digito2 == 10:
        digito2 = 0

    digitos_verificadores = str(digito1) + str(digito2)

    return digitos_verificadores

print(calcula_digitos_verificacao('153245875'))
        

