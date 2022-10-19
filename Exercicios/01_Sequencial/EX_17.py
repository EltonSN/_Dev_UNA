import math

area_toal = int(input('Digite a quantidade em M2 da area a ser pintada: '))

litros = area_toal / 6

latas_18l = math.ceil(litros / 18) 
latas_3l6 = math.ceil(litros / 3.6)

valor_latas_18l = latas_18l * 80 
valor_latas_3l6 = latas_3l6 * 25

print ('Litros de tinta: ' + str(litros))
print()
print('Quantidade de latas de 18L: ' + str(latas_18l))
print('Quantidade de latas de 3.6L: ' + str(latas_3l6))
print()
print ('Valor totalpara latas de 18L: R$ ' + str(valor_latas_18l))
print ('Valor totalpara latas de 3,6L: R$ ' + str(valor_latas_3l6))