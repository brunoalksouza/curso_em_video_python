n = int(input('digite um valor para ver a tabuada: '))

print('-------------')
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n*c)))
print('-------------')
