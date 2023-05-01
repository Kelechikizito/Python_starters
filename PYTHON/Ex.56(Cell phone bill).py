# A PROGRAM THAT CALCULATES A PHONE BILL
fifty_airtime = fifty_text = 15.00
add_airtime = 0.25
add_text = 0.15
emergency = 0.44
tax = 0.05
min = int(input('Enter the number of minutes used in a month: '))
text = int(input('Enter the number of text messages used in a month: '))
if min <= 50:
    print('The base charge is $15.00')
elif min > 50:
    airtime_addcharge = (min - 50) * add_airtime
    print('The base charge is $15.00')
    print('The additional minutes charge is ${:.2f}'.format(airtime_addcharge))
elif text <= 50:
    print('The base charge is $15.00')
elif text > 50:
    text_addcharge = (text - 50) * add_text
    print('The base charge is $15.00')
    print('The additional text charge is ${:.2f}'.format(text_addcharge))
airtime_addcharge = (min - 50) * add_airtime
text_addcharge = (text - 50) * add_text
tax1 = tax * (fifty_airtime + emergency + airtime_addcharge + text_addcharge)
tax2 = tax * (fifty_airtime + emergency)
print('The 911 fee is ${}'.format(emergency))
if (min > 50) and (text > 50):
    tax_amnt = tax * (fifty_airtime + emergency + airtime_addcharge + text_addcharge)
    print('The tax is ${:.2f}'.format(tax_amnt))
else:
    tax_amnt2 = tax * (fifty_airtime + emergency)
    print('The tax is ${:.2f}'.format(tax_amnt2))
if (min > 50) and (text > 50):
    bill = tax1 + emergency +  airtime_addcharge + text_addcharge + fifty_airtime
    print('The total bill amount is ${:.2f}'.format(bill))
else:
    bill2 = tax2 + emergency + fifty_airtime
    print('The total bill amount is ${:.2f}'.format(bill2))