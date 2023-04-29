n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))

average = (n1+n2)/2

if average < 5:
    print('sua média foi {} - Reprovado'.format(average))
elif average == 5 or average <= 6.9:
    print('sua média foi {} - Recuperação'.format(average))
elif average >= 7:
    print('sua média foi {} - Passou'.format(average))