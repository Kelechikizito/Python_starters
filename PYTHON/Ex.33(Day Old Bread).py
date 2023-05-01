# A PROGRAM THAT COMPUTES PRICES FOR BREAD
price = 3.49
day_old_bread = price - (0.6 * price)
order = int(input('How many loaves of day old bread do you want? '))
print('The price of regular bread is {}$ per loaf.'.format(price))
price_order = price * order
discounted_price = 0.6 * price_order
print('The discount at 60% cause it is a day old is {:.2f}$'.format(discounted_price))
total_price = price_order - (discounted_price)
print('The price is {:.2f}$.'.format(total_price))