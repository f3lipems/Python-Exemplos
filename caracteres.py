'''
+-+-+-+-+-+-+-+-+-+-+
|C|a|r|a|c|t|e|r|e|s|
+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9
'''

Carac = 'Caracteres'
print('+-+-+-+-+-+-+-+-+-+-+')
print('|C|a|r|a|c|t|e|r|e|s|')
print('+-+-+-+-+-+-+-+-+-+-+')
print(' 0 1 2 3 4 5 6 7 8 9')

# Intervalo de Caracteres
print(Carac[2:8])

# Do primeiro ao quinto Caracter
print(Carac[:5])

# Do quinto ao último Caracter
print(Carac[5:])

# Para nos X últimos Caracteres
print(Carac[:-3])

# Inicia pelos X últimos Caracteres
print(Carac[-3:])

# Intervalo de Caracteres de 2 em 2
print(Carac[2:8:2])

# Intervalo de Caracteres de 3 em 3
print(Carac[2::3])