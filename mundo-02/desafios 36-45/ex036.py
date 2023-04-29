houseValue = float(input('Qual o valor da casa? '))
wage = float(input('Qual o seu salario? '))
time = float(input('Em quantos anos você quer pagar? '))

time = time*12
provision = houseValue/time

if provision > 0.3*wage:
    print('Emprestimos negado')
else:
    print('Emprestimo aprovado!')