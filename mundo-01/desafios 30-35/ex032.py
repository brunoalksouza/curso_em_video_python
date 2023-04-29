from datetime import date

year = int(input('Que ano quer analizar? '))
 
if year == 0:
    year = date.today().year
    
if year % 4 == 0 and year % 100 != 0 or year != 400:
    print('O ano {} é bissexto!'.format(year))
else:
    print('O ano {} não é bissexto!'.format(year))
    