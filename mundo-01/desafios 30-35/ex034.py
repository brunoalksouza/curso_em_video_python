salario = float(input('Qual o valor do seu salario: '))

if salario > 1250:
    salario = salario + salario *0.1
else:
    salario = salario + salario *0.15
    
print('Seu salario sofreu ume aumento e agora você receberá R${:.2f}'.format(salario))