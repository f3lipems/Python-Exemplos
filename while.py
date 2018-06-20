# While

import random

num1, num2 = 0, 7

while num1 <= num2:
    print('Número 1: {}, Número 2: {}'.format(num1, num2))
    num1 += num2/8


# While com numeros randomicos
pares = 0
impares = 0

while pares < 10 or impares < 10 :
    n = random.randint(0,9)
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if pares == 12:
        break
    

print(pares) 
print(impares) 

x = 0

while x <= 7:
    
    x += 1
    
    if x % 2 == 0:
        continue 
    else:
        print(x)