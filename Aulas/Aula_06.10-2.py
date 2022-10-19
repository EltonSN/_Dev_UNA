'''def gravar_arquivo(arquivo, texto): 
    arq = open(arquivo, 'w')
    arq.writelines(texto)
    arq.close

gravar_arquivo('teste1', 'texto dentro do arquivo')
gravar_arquivo('teste2', 'texto dentro do arquivo')


#--------------------------------------------------------
import math

def hipotenusa(cateto1, cateto2):
    
    soma = (cateto1 * cateto1) + (cateto2 * cateto2)
    hipot = math.sqrt(soma)
    return(hipot)

resultado = hipotenusa(3, 4)
print (resultado)
'''
import math 

def calq_raio(raio):
    area = 3.14 * (raio * raio)
    return(area)
    
result = calq_raio(8)
print(result)

def calq_triangulo(b, h):
    areat = (b * h) / 2
    return(areat)

print(calq_triangulo(2, 2))