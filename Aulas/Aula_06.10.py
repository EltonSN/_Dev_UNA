nota1 = float(input('Digite sua Primeira nota: '))
nota2 = float(input('Digite sua Segunda nota: '))
nota3 = float(input('Digite sua Terceira nota: '))
nota4 = float(input('Digite sua Quarta nota: '))


notas = [nota1[0] + nota2[1] + nota3[2] + nota4[3] + nota5[4]]

soma = 0 

for i in range(0, 4): 
    soma = soma + notas[i]

media = soma / 4

if (media >= 7):
    print('Aprovado')
else:
    print('reprovado')