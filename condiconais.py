## Condicionais simples

idioma = 'portugues'

if idioma == 'portugues':
    print('Idioma {} dfinido como padrão.'.format(idioma)) 


## Condicionais compostas

idioma = 'espanhol'

if idioma == 'ingles':
    print('Idioma {} dfinido como padrão.'.format(idioma)) 
else:
    print('Idioma não disponível')


## Condicionais aninhadas

idade = 19

if idade < 18:
    print('Idade insuficiente para o acesso.')
elif idade >= 18 and idade < 21:
    print('Acesso liberado, com restrição.')
else:
    print('Acesso liberado.')


pessoa = 'idosa'

if pessoa == 'mulher' or pessoa == 'crianca':
    print('Isento')
elif pessoa in 'idosa idoso':
    if pessoa == 'idosa':
        print('Entrada com desconto e tem direito a brinde.')
    else:
        print('Entrada com desconto.')
else:
    print('Valor integral')