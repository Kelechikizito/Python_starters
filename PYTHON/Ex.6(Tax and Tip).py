#  TAX AND TIP
from tkinter import N


cost_of_rice_ordered = int(input('Cost of food ordered: '))
tax_rate = 0.75
tax_amount = cost_of_rice_ordered * tax_rate
a = '%.2f.' %tax_amount
tip_amount = 18/100 * cost_of_rice_ordered
b = (round(tip_amount, 2))
grand_total_with_tax_and_tip = cost_of_rice_ordered + tax_amount + tip_amount
c = '%.2f.' %grand_total_with_tax_and_tip
print('The tax amount  and The tip amount is ', a, b )
print('The grand total is N',c)

  