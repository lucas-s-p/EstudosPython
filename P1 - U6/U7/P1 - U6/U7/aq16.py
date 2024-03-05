def senha_segura(senha):
        seguro = ''
        for i in range(len(senha)):
                if i % 2 == 0 and int(senha[i]) % 2 != 0:
                        seguro += f'{senha[i]}'
                if i % 2 != 0 and int(senha[i]) % 2 == 0:
                        seguro += f'{senha[i]}'
        
        if seguro == senha:
                return 'Senha segura'
        else:
                return 'Senha insegura'

assert senha_segura("11") == "Senha insegura"
assert senha_segura("125638") == "Senha segura"