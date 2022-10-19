print('Em que turno você estuda? ')

turno = input('Digite [M] para Matutino, [V] para Vespertino ou [N] para Noturno: ')

if (turno == 'M' or 'm'):
    print('Bom dia!')
elif (turno == 'V' or 'v'):
    print('Boa tarde')
elif (turno == 'N' or 'n' ):
    print('Boa Noite')
else: 
    print('Valor Invalido! ')
