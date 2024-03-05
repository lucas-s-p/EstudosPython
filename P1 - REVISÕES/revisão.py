def soma(num1, num2, num3=2):
    return (num1 + num2) - num3

print(soma(2, 5))

num = []
n = 0
while n != 8:
    n = int(input('inteiro? '))
    num.append(n)

num.pop()
for valor in num:
    print(valor, valor ** 2, valor ** (1/2))

print(num)
print('fim')

string = 'lucas'
for car in string:
    print(car, end='')

print('\n')

nome = 'lucas'
soma = ''
for e in nome:
    soma += e
print(soma)

palavra =  input('Palavra? ')
for car in palavra:
    print(car, ord(car), car.upper(), ord(car.upper()))

palavra = input('Palavra? ')
for car in reversed(palavra):
    print(car, ord(car), car.upper(), ord(car.upper()))

num = int(input('inteiro? '))
print(num)
for valor in range(1, num + 1):
    print(valor, valor ** 2, valor ** (1/2))

print('fim')
