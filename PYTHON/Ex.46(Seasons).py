# A PROGRAM THAT READS DATE AND BRINGS AN OUTPUT OF THE RESPECTIVE SEASON
month = input('Enter the month: ')
day = int(input('Enter the day of the month: '))
if (month == 'January' or month == 'February') and (day <= 31):
    print('The season of the date is winter')
elif (month == 'December') and (day >= 21):
    print('The season of the date is winter')
elif (month == 'March') and (day <= 19):
    print('The season of the date is winter')
elif (month == 'April' or month == 'May') and (day <= 31):
    print('The season of the date is spring')
elif (month == 'March') and (day >= 20):
    print('The season of the date is spring')
elif (month == 'June') and (day < 21):
    print('The season of the date is spring')
elif (month == 'July' or month == 'August') and (day <= 31):
    print('The season of the date is summer')
elif (month == 'June') and (day >= 21):
    print('The season of the date is summer')
elif (month == 'September') and (day < 22):
    print('The season of the date is summer')
elif (month == 'October' or month == 'November') and (day <= 31):
    print('The season of the date is fall')
elif (month == 'September') and (day >= 22):
    print('The season of the date is fall')
elif (month == 'December') and (day < 21):
    print('The season is fall')
else:
    print('Make sure the first letter of the month provided starts with a capital letter.')