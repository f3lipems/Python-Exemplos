# Caracteres

carac = 'Caracteres'
print('+-+-+-+-+-+-+-+-+-+-+')
print('|C|a|r|a|c|t|e|r|e|s|')
print('+-+-+-+-+-+-+-+-+-+-+')
print(' 0 1 2 3 4 5 6 7 8 9')

# Intervalo de Caracteres
print(carac[2:8])

# Do primeiro ao quinto Caracter
print(carac[:5])

# Do quinto ao último Caracter
print(carac[5:])

# Para nos X últimos Caracteres
print(carac[:-3])

# Inicia pelos X últimos Caracteres
print(carac[-3:])

# Intervalo de Caracteres de 2 em 2
print(carac[2:8:2])

# Intervalo de Caracteres de 3 em 3
print(carac[2::3])

print('')

# Analizando a cadeia de caracteres
print('Número de Caracteres: ',len(carac)) 
print('Contagem da letra "a": ', carac.count('a'))  
print('Contagem da letra "a" no intervalod do caracter 2 ao 8: ', carac.count('a',2,8))  
print('Contagem da sequencia "rac": ', carac.count('rac'))
print('Localização da sequencia "cte": ', carac.find('cte'))
print('Localização de uma sequencia inexistente, ex: "py": ', carac.find('py'))


print('\nVerificar se caracteres existe ou não')
print('cte' in carac)
print('py' in carac)

print('\nSubstituir Caracter')
print(carac.replace('teres','ter'))

carac2 = 'cadeia de caracteres'

print('\nLetras caixa alta')
print(carac2.upper())

print('\nLetras caixa baixa')
print(carac2.lower())

print('\nCapitalizar palavra')
print(carac2.capitalize())

print('\nCapitalizar todas as palavras da frase')
print(carac2.title())

carac3 = '     cadeia de caracteres     '

print('\nEliminar Caracter em branco no início e fim')
print(carac3)
print(carac3.strip())
#print(carac3.lstrip()) Eliminar caracteres em branco a esquerda
#print(carac3.rstrip()) Eliminar caracteres em branco a direita
