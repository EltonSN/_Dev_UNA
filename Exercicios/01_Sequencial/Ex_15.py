sal_hora = float(input('Quanto você ganha por hora? '))
qtd_horas = float(input('Quantas horas vc trabalha por Mês? '))

sal_bruto = sal_hora * qtd_horas 
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
sal_liguido = sal_bruto - sindicato

print ('Seu saário bruto é de: R$ '+ str(sal_bruto))
print ('Seu desconto do INSS é de: R$ '+ str(inss))
print ('Seu desconto do sindicato é de: R$ '+ str(sindicato))
print ('Seu salário liguido ficou em: R$ '+ str(sal_liguido))