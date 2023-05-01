# A PROGRAM THAT COMPUTES UNITS OF TIME
print('D:HH:MM:SS WILL BE THE EQUIVALENT TIME FORMAT AFTER CONVERSION')
day = 86400
hour = 3600
min = 60 
sec = 1
no_of_seconds = int(input('Enter the number of seconds: '))
day1 = no_of_seconds // day
day2 = no_of_seconds % day
hour1 = day2 // hour
hour2 = day2 % hour
min1 = hour2 // min
min2 = hour2 % min
sec1 = min2
print('The equivalent time is {0:d}:{1:02d}:{2:02d}:{3:02d}.'.format(day1,hour1,min1,sec1))