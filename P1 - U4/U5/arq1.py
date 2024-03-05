def sequencia():
    seq = int(input())

    val = []
    for i in range(seq):
        i = int(input())
        val.append(i)
    return val

def main():
    val = sequencia()
    minimo = 0
    media = 0
    maximo = 0
    for v in range(len(val)):
        media += val[v]
        med = media / (v + 1)
        if minimo == 0 or val[v] < minimo:
            minimo = val[v]
        if val[v] > maximo:
            maximo = val[v]
        print(f'{val[v]} {minimo} {med:.2f} {maximo}')

if __name__ == "__main__":
    main()