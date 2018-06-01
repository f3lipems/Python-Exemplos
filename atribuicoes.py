# Atribuição Simples
n1 = 10
n2 = 20
nome1 = 'João'
nome2 = 'Pedro'

print('Atribuição Simples')
print('n1 = {}, n2 = {}, nome1 = {} e nome2 = {} \n'.format(n1,n2,nome1,nome2))


# Atribuição multipla
n1, n2 = 5, 15
nome1, nome2 = 'Tiago', 'Filipe'

print('Atribuição Multipla')
print('n1 = {}, n2 = {}, nome1 = {} e nome2 = {} \n'.format(n1,n2,nome1,nome2))


# Atribuição composta
n1 = n2 = n3 = n4 = 3

n1 += 2
n2 -= 2
n3 *= 2
n4 /= 2
print('Atribuição Composta')
print('n1 = {}, n2 = {}, n3 = {} e n4 = {} \n'.format(n1,n2,n3,n4))


# Atribuição Condicional
val1 = 8
val2 = 6 
status1 = 'Aprovado' if val1 >= 7 else 'Reprovado'
status2 = 'Aprovado' if val2 >= 7 else 'Reprovado'

print('Atribuição Condicional')
print ('Condição para val1 = {}'.format(status1)) 
print ('Condição para val2 = {}'.format(status2)) 