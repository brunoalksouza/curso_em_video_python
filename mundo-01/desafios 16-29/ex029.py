vel = int(input('Digite a velocidade do seu carro: '))

if vel > 80:
    print('Seu carro foi multado')
    multa = (vel - 80)*7
    print('sua multa é {:.2f}'.format(multa))
else:
    print('não teve multa alguma') 