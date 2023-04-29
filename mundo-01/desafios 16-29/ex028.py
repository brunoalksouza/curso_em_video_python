# modulo de condicionais 

from random import randint

n = randint(0,5)
 
nDigitado = int(input('Adivinhe um numero entre 0 e 5: '))

if nDigitado == n:
    print('VOce acertou!')
else:
    print('voce errou!')