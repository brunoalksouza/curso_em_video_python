from math import radians, sin, cos, tan

ang = float(input('Digite o angulo que voce deseja: '))

sen = radians(sin(ang))
cos = radians(cos(ang))
tg = radians(tan(ang))

print('o seno, cosseno e tangente respectivamente do angulo {:.0f} é: {:.4f}, {:.4f}, {:.4f}'.format(
    ang, sen, cos, tg))
