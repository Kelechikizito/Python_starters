# A PROGRAM THAT READS DATES AND COMPUTES IT IMMEDIATE SUCCESSOR

jan = 1
feb = 2
mar = 3
apr = 4
may = 5
jun = 6
jul = 7
aug = 8
sept = 9
oct = 10
nov = 11
dec = 12
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
f = year % 400

# A LEAP YEAR
if ((f % 4 == 0) or (f == 0)) and (month == 2) and (day == 29):
    print('The next day is {}/{}/{}'.format(year,3,1))
if ((f % 4 == 0) or (f == 0)) and (month == 2) and (day < 29):
    print('The next day is {}/{}/{}'.format(year,month,day+1))

# A NORMAL YEAR
elif (not(f % 4 == 0) or (f == 0)) and (month == 2) and (day == 28):
    print('The next day is {}/{}/{}'.format(year,3,1))
elif (not(f % 4 == 0) or (f == 0)) and (month == 2) and (day < 28):
    print('The next day is {}/{}/{}'.format(year,month,day+1))

# 31 DAYS MONTH
elif (month == sept or month == apr or month == jun or month == nov) and day == 30:
    print('The next day is {}/{}/{}'.format(year,month+1,1))

# 30 DAYS MONTH
elif (month == jan or month == mar or month == may 
    or month == jul or month == aug or month == oct ) and day == 31:
    print('The next day is {}/{}/{}'.format(year,month+1,1))

# A NEW YEAR
elif month == dec and day == 31:
    print('The next day is {}/{}/{}\nHAPPY NEW YEAR!'.format(year+1,jan,1))

# 30 DAYS MONTH
elif (month == sept or month == apr or month == jun or month == nov) and day < 30:
    print('The next day is {}/{}/{}'.format(year,month,day+1))

#31 DAY MONTH
elif (month == jan or month == mar or month == may 
    or month == jul or month == aug or month == oct or month == dec) and day < 31:
    print('The next day is {}/{}/{}'.format(year,month,day+1))