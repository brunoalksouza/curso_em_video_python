import datetime

birthYear = int(input('Em qual ano você nasceu? '))

current_year = datetime.date.year

category = current_year - birthYear

if category <= 9:
    print('Mirim')
elif category <= 14:
    print('Infantil')
elif category <= 19:
    print('Júnior')
if category <= 20:
    print('Sênior')
else:
    print('Master')