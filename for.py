## Repetições com for

print('Início do laço.')
for i in range(10,15):
    print(i)
print('Final do laço.\n')

print('Início do laço.')
for i in range(5):
    print('Número {}'.format(i))
print('Final do laço.\n')

print('Início do laço.')
for i in range(10,20,2):
    print(i)
print('Final do laço.\n')

print('Início do laço.')
for i in range(10,0,-2):
    print(i)
print('Final do laço.\n')

print('Início do laço.')
tabuada = 7
for j in range(1,11):
    print('{} x {} = {}'.format(j, tabuada, j*tabuada))
print('Final do laço.\n')

print('Início do laço.')
for k in range(1,6):
    print('Número do laço: {}.'.format(k))
    if k == 3:
        break
print('Final do laço.\n')

print('Início do laço.')
for carac in 'laços de repetição':
    print(carac)
    if carac == 's':
        break
print('Final do laço.\n')

print('Início do laço.')
for carac in 'laços de repetição':
    if carac in 'd':
        continue
    print(carac)
print('Final do laço.\n')

print('Início do laço.')
palavra = 'laços'
tamanho = len(palavra)
for k in range(tamanho,0,-1):
    print(palavra[tamanho - 1:tamanho])
    tamanho = tamanho -1
print('Final do laço.\n')