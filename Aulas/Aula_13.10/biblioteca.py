import math

def hipotenusa(a, b):
    h = math.sqrt((a * a) + (b * b ))
    return(h)

def triangulo_equi_area(h, l):
    area = (l * l) + math.sqrt(h    3)

def area_circulo(r):
    area = 3.14 * (r * r)
    return(area)

def area_retangulo(b, h):
    area = b * h
    return(area)

def area_triangulo(b, h):
    area = (b * h) /2
    return(area)
