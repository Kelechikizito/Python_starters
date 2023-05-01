# A PROGRAM THAT READS A DATE AND BRINGS IT APPROPRAITE HOLIDAY
month = input('Enter the month: ')
day = int(input('Enter the day: '))
if (day == 1) and (month == 'January' or month == 'january'):
    print("This is the New year's day")
elif (day == 2) and (month == 'July' or month == 'july'):
    print('This is Canada day')
elif (day == 25) and (month == 'December' or month == 'december'):
    print('This is Christmas day')
else:
    print('No holiday in Canada allocated to this date')

# MY MISTAKES WERE:
#1. NOT GROUPING MY INPUT VARIABLES IN BRACKETS/PARENTHESES
#2. NOT INCLUDING PRINT STATEMENT IN ELSE
#3. NOT SEPARATING THE OR STATEMENTS