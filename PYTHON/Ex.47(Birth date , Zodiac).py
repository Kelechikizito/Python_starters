# A PROGRAM THAT BRINGS OUT THE ZODIAC SIGN OF ITS USER
month = input('What is your birth month? ')
day = int(input('What is your birth day? '))
if (month == 'December') and (day >= 22):
    print('Your zodiac sign is Capricorn')
elif (month == 'January') and (day <= 19):
    print('Your zodiac sign is Capricorn')
elif (month == 'January') and (day >= 20):
    print('Your zodiac sign is Aquarius')
elif (month == 'February') and (day <= 18):
    print('Your zodiac sign is Aquarius')
elif (month == 'February') and (day >= 19):
    print('Your zodiac sign is Pisces')
elif (month == 'March') and (day <= 20):
    print('Your zodiac sign is Pisces')
elif (month == 'March') and (day >= 21):
    print('Your zodiac sign is Aries')
elif (month == 'April') and (day <= 19):
    print('Your zodiac sign is Aries')
elif (month == 'April') and (day >= 20):
    print('Your zodiac sign is Taurus')
elif (month == 'May') and (day <= 20):
    print('Your zodiac sign is Taurus')
elif (month == 'May') and (day >= 21):
    print('Your zodiac sign is Gemini')
elif (month == 'June') and (day <= 20):
    print('Your zodiac sign is Gemini')
elif (month == 'June') and (day >= 21):
    print('Your zodiac sign is Cancer')
elif (month == 'July') and (day <= 22):
    print('Your zodiac sign is Cancer')
elif (month == 'July') and (day >= 23):
    print('Your zodiac sign is Leo')
elif (month == 'August') and (day <= 22):
    print('Your zodiac sign is Leo')
elif (month == 'August') and (day >= 23):
    print('Your zodiac sign is Virgo')
elif (month == 'September') and (day <= 22):
    print('Your zodiac sign is Virgo')
elif (month == 'September') and (day >= 23):
    print('Your zodiac sign is Libra')
elif (month == 'October') and (day <= 22):
    print('Your zodiac sign is Libra')
elif (month == 'October') and (day >= 23):
    print('Your zodiac sign is Scorpio')
elif (month == 'November') and (day <= 21):
    print('Your zodiac sign is Scorpio')
elif (month == 'November') and (day >= 22):
    print('Your zodiac sign is Sagittarius')
elif (month == 'December') and (day <= 21):
    print('Your zodiac sign is Sagittarius')
else:
    print('''THINGS TO CROSS-CHECK:\n-MAKE SURE IT IS A VALID MONTH 
-MAKE SURE JUST THE FIRST LETTER OF YOUR BIRTH MONTH IS CAPITALISED. ''')