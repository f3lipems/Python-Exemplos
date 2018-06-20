## Dicionários

print('Dicionário com chave em string')
dic = {'nome':'Felipe', 'idade':30, 'peso':71.5}

print('Nome: {}'.format(dic['nome']))
print('Idade: {}'.format(dic['idade']))
print('Peso: {:.1f}'.format(dic['peso']))


print('\nDicionário com chave numérica')
dic2 = {1:'Felipe', 2:30, 3:71.5}

print('Nome: {}'.format(dic2[1]))
print('Idade: {}'.format(dic2[2]))
print('Peso: {:.1f}'.format(dic2[3]))

dic3 = dic2
dic4 = dic2.copy()

dic2[4] = 'M' 
dic2[5] = 'Casado'
del(dic3[3]) 
del(dic3[2]) 
del(dic3[1]) 

print(dic2)
print(dic3)
print(dic4)

dic4.update(dic3)
print(dic4)


for i in dic4:
    print(i)

for i in dic4.values():
    print(i)

for i, c in dic4.items():
    print('Chave: {}, Valor: {}'.format(i,c))


chaves = dic4.keys()
valores = dic4.values()

print(chaves)
print(valores)

chaves = list(dic4.keys())
valores = list(dic4.values())

print(chaves)
print(valores)

dic5 = zip(chaves,valores)
print(dic5)

dic6 = dict(zip(chaves,valores))
print(dic6)