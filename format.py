# Formatações

n1 = 123
n2 = 456
n3 = 789
n4 = 5.777777777

print('Nemero 1: {:>10}'.format(n1))
print('Nemero 2: {:<10}'.format(n2))
print('Nemero 3: {:=^10}'.format(n3))
print('Nemero 4: {:.2f}'.format(n4))

# Eliminando a quebra de linha no final do print()
print('Nuemro 1: {} '.format(n1), end = '') 
print('Nuemro 2: {} '.format(n2))