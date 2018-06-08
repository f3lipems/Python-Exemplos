idade = 19

if idade < 18:
    print('Idade insuficiente para o acesso.')
elif (idade >= 18 and idade < 21):
    print('Acesso liberado, com restrição.')
else:
    print('Acesso liberado.')

pessoa = 'crianca'

if pessoa == 'mulher' or pessoa == 'crianca':
    print('Isento')
else:
    print('Cobrar entrada')
