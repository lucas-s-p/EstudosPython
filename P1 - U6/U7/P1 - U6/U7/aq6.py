n = int(input())

times = []
for i in range(2 * n):
    i = input()
    times.append(i)

l1 = []
l2 = []
for i in range(len(times)):
    if i % 2 == 0:
        l1.append(times[i])
    else:
        l2.append(times[i])
        

for i in range(len(l1)):
    print(f'{l1[i]} ({l2[i]})')