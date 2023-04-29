import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)

print('o valor da hipotenusa desse triangulo é {:.2f}'.format(hip))
