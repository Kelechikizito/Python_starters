# A PROGRAM THAT CALCULATES THE COST OF ITEMS INCLUDING AND EXCLUDING PENNIES

a = []

while True:
    price = input('Enter the price of each item(Enter blank to exit): ')
    if price == '':
        break
    price2 = float(price)
    a.append(price2)

total_cost = sum(a) + 0.0
penny = total_cost * 100
rem = penny % 5

if rem < 2.5:
    cost = total_cost - (rem/100)
else:
    cost = total_cost + 0.5 - (rem/100)

print(total_cost)
print(cost)
