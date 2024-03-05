def dobradas(str1, str2):
    ig = [print(str1[i]) for i in range(len(str1)) if str1[i] == str2[i] ]
    return ig

print(dobradas('lucas', 'leviaa'))
