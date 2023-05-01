# A PROGRAM THAT READS DISTANCE UNITS
print('''one_foot_per_inch = 12
one_foot_per_yard = 0.333 
one_foot_per_mile = 0.000189394''')
one_foot_per_inch = 12
one_foot_per_yard = 0.333 
one_foot_per_mile = 0.000189394
measurement = float(input('HOW MANY FEET WOULD YOU LIKE TO CONVERT? '))
inch_distance = measurement * one_foot_per_inch
yard_distance = measurement * one_foot_per_yard
mile_distance = measurement * one_foot_per_mile
print(inch_distance,'inches\n',yard_distance,'yards\n',mile_distance,'miles')
