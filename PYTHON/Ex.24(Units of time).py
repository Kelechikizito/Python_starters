# A PROGRAM THAT READS VARIOUS UNITS OF TIME
day = 86400
hour = 3600
minutes = 60
seconds = 1
no_of_days = int(input('Number of days? '))
no_of_hours = int(input('Number of hours? '))
no_of_minutes = int(input('Number of minutes? '))
no_of_seconds = int(input('Number of seconds? '))
total_no_of_seconds = (no_of_days * day) + (no_of_hours * hour) + (no_of_minutes * minutes) + (no_of_seconds * seconds)
print('{} is your duration represented in seconds.'.format(total_no_of_seconds))