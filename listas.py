# Listas

## Lista de Números
numeros = [1,2,3,4,5,6,7]

print(numeros)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[-1])

for i in range(len(numeros)):
    numeros[i] += 10
print(numeros)

for i, c in enumerate(numeros):
    numeros[i] += 10
    print(c * 2)
print(numeros)


##Lisa de Caracteres

caracteres = ['a','e','i','o','u']
print(caracteres)
print(caracteres[0])
print(caracteres[1])
print(caracteres[2])
print(caracteres[3])
print(caracteres[4])

print(caracteres[2:4])
print(caracteres[::2])

lista = list(('Python'))
print(lista)

for i in lista:
    print(i)

## funções da clase list

listaConc = numeros + caracteres + lista

print(listaConc)

listaTest = ['a','e','i'] + ['o'] + ['u']

print(listaTest)

listaTest2 = [1,2,3]
print(listaTest2)

# Adicionar item no final
listaTest2.append(4)
listaTest2.append(5)
print(listaTest2)

# Adicionar item no índice
listaTest2.insert(0,'inicio')
listaTest2.insert(3,'x')
print(listaTest2)

del(listaTest2[2])
print(listaTest2)

#listaTest2.pop()
print(listaTest2.pop())
print(listaTest2)

listaTest2.pop(0)
print(listaTest2)

listaTest2.clear()
print(listaTest2)


## Listas Embutidas

listasEmbutidas = [[1,2,3],['a','b','c']]

print(listasEmbutidas)
print(listasEmbutidas[1][1])

## Ordenação

listaTest3 = [5,8,4,6,9,1,3,2,7]
print(listaTest3)

listaTest3.reverse()
print(listaTest3)

listaTest3.sort()
print(listaTest3)

listaTest3.sort(reverse=True)
print(listaTest3)