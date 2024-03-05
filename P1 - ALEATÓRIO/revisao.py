num_dados = int(input())
fal = int(input())

l = []
l.append(fal)

max = fal
min = fal
sum = fal

media = sum/ len(l)

print(f'{fal} {min} {media:.2f} {max}')

for i in range(num_dados - 1):
    t = int(input())
    l.append(t)
    sum += t
    if t > max:
        max = t
    if t < min:
        min = t
    media = sum/len(l)
    print(f'{t} {min} {media:.2f} {max}')