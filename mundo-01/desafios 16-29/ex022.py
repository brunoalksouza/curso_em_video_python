nome = str(input('Qual seu nome completo? ')).strip()

print('Seu nome em maiúsculas é {}'.format(nome.upper()))

print('Seu nome em minusculas é {}'.format(nome.lower()))

print('a quantidade de letras ao todo é {}'.format(len(nome)-nome.count(' ')))

print('a quantidade de letras do primeiro nome é {}'.format(nome.find(' ')))

separado = nome.split()

print('seu primeiro nome é {} e possui {} letras'.format(separado[0], len(separado[0])))