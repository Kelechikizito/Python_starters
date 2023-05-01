# A PROGRAM THAT USES A LOOP TO GENERATE DISCOUNT AND RELATED CALCULATIONS
op1 = 4.95
op2 = 9.95
op3 = 14.95
op4 = 19.95
op5 = 24.95
dis = 0.6
print('ALL PRICES ARE 60% PERCENT OFF \n')
for x in op1, op2, op3, op4, op5:
    print('$',x, 'is the original price')
    disam = dis * x     # DISCOUNT AMOUNT
    print('$ {:.2f} is the discount amount'.format(disam))
    newp = x - disam    # NEW PRICES
    print('$ {:.2f} is the new price \n'.format(newp))