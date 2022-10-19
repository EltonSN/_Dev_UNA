salario = float(input('Digite o salário: '))

if (salario <= 280):
    reajuste = 0.2
elif (salario <= 700):
    reajuste = 0.15
elif (salario <= 1500):
    reajuste = 0.10
else: 
    reajuste = 0.05

valor_reajustado = salario * reajuste
salario_reajustado = salario + valor_reajustado

print ('Salário é igual a: ' + str(salario))
print ('Percentual do reajuste: ' + str(reajuste))
print ('valor do reajuste: ' + str(valor_reajustado))
print ('Salário reajustado: ' + str(salario_reajustado))