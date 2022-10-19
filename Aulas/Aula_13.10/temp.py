import biblioteca as bib

base = int(input('Digite a base do triangulo: '))
altura = int(input('Digite a altura do triangulo: '))

area = bib.area_triangulo(base, altura)

print('A area do triangulo é ' + str(area))
