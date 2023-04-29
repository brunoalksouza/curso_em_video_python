age = int(input('Digite a sua idade: '))

if age < 18:
    time = 18 - age
    print('Você vai ter que se alistar daqui a {} anos'.format(time))
elif age == 18:
    print('Já está na hora de se alistar!')
else:
    time = age - 18
    print('Já passou {} anos que você deveria ter se alistado!'.format(time))