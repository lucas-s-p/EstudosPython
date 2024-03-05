# Módulo collections - Deque
# Podemos dixer que o deque é uma lista de alta performace.

from collections import deque

# Criando deques
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')  # Adiciona no começo
print(deq)

print(deq.pop())    #Remove o ultimo elemento e retorna
print(deq)

print(deq.popleft())  #Remove e retorna o primeiro elemento
print(deq)
