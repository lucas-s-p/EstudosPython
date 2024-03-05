def  is_substring_expr(str1,str2):
    sep = str2.split('*')
    cont1 = len(sep[0])
    cont2 = len(sep[1])

    verifica = ''
    for i in range(cont1):
        if str1[i] == str2[i]:
            verifica += str1[i]
 
    verifica1 = ''
    for i in range(-1, -(cont2) - 1, -1):
        if str2[i] == str1[i]:
            verifica1 += str1[i]

    if cont1 == len(verifica) and cont2 == len(verifica1):
        return True
    else:
        return False

print(is_substring_expr('oicvoce','oi*voce'))
