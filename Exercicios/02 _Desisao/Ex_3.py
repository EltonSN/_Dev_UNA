'''Informar o Sexo apenas com a primeira letra'''

sexo = input('Digite (M)asculino ou (F)eminino: ')


if (sexo == 'M' or sexo == 'm'):
    print ('Você é do sexo Masculino')
elif (sexo == 'F' or sexo == 'f'):
    print ('Você é do sexo Feminino')
else:
    print ('Sexo invalido')