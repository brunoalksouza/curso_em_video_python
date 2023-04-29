n = float(input('Qual a distância da viagem em Km? '))

if n <= 200:
    preco = n*0.5
else:
    preco = n*0.45

print('o preco da viagem é {:.2f}' .format(preco))
