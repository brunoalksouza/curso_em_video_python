a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print('O maior número é {} e o menor número é {}'.format(a,b))
elif a < b:
    print('O maior número é {} e o menor número é {}'.format(b,a))
else:
    print('Os números {} e {} são iguais'.format(b,a))