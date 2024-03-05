def is_substring(str1, str2):
    string = ''
    for e in range(len(str1)):
        if str1[e] == str2[0]:
            index = len(str2) + e
            if len(str1) >= index:
                for c in range(e, index):
                    for i in range(len(str2)):
                        if str1[c] == str2[i]:
                            string += str1[c]
                            break
        if string == str2:
            return True
        else:
            string = ''
            
    return False

print(is_substring('aiaip','aip'))
