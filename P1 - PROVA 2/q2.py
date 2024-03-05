seq = int(input())

cont_true = 0
l = []
l2 = []
cont_false = 0

for i in range(seq):
    achou = False
    string = input()
    for i in range(len(string) -1):
        if string[i] == string[i + 1]:
            cont_true += 1
            l.append(string)
            achou = True
            break
    if not achou:
        l2.append(string)
        cont_false += 1

print(f'{cont_true} palavra(s) com letras dobradas:')
for e in l:
    print(e)
print('---')
print(f'{cont_false} palavra(s) sem letras dobradas:')
for e in l2:
    print(e)
