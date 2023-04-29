age = int(input('Digite a sua idade: '))

if age < 18:
    print('Você ainda vai ter que se alistar!')
elif age == 18:
    print('Já está na hora de se alistar!')
else:
    print('Já passou o tempo de você se alistar!')