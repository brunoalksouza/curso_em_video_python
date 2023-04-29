a = int(input('Primeiro numero: '))
b = int(input('segundo numero: '))
c = int(input('terceiro numero: '))

# menor
menor = a
if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

# maior
maior = a
if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('---------------------\nEntre {}, {}, {}\nO menor numero é: {}\nE o maior numero é o {}'.format(
    a, b, c, menor, maior))
