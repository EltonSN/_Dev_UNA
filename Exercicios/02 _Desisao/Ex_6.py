'''Qual maior número'''
N1 = float(input('Digite o primeiro número: '))
N2 = float(input('Digite o segundo número: '))
N3 = float(input('Digite o terceiro número: '))

if (N1 > N2 and N1 > N3):
    print (''+ str(N1) + ' é o Maior Número')
elif (N2 > N1 and N2 > N3):
    print (''+ str(N2) + ' é o Maior Número')
elif (N3 > N2 and N3 > N1):
    print (''+ str(N3) + ' é o Maior Número')
else:
    print ('error números iguais')