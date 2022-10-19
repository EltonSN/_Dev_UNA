'''Produto mais barato'''
pd1 = float(input('Informe o valor do primeiro produto: '))
pd2 = float(input('Informe o valor do segundo produto: '))
pd3 = float(input('Informe o valor do terceiro produto: '))

if (pd1 < pd2 and pd1 < pd3):
    print ('Primeiro produto é o mais indicado. ')
elif (pd2 < pd1 and pd2 < pd3):
    print ('Segundo produto é o mais indicado. ')
elif (pd3 <pd1 and pd3 < pd2):
    print ('Terceiro produto é o mais indicado. ')
else:
    print ('Nenhum produto é indicado. ')
    