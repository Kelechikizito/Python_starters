#  A PROGRAM THAT READS HEIGHT UNITS
print('''One foot is 12 inches.
One inch is 2.54 centimetres.''')
one_inch = 2.54
one_foot = 12 * one_inch
feet_read = int(input('How tall are you in feet ? '))
inches_read = int(input('How tall are you in inches? '))
height = (feet_read * one_foot) + (inches_read * one_inch) 
print(height, 'is your equivalent height in centimetres.')
 
