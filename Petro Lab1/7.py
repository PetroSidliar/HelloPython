'''
Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the
tip amount and the total bill with the tip included.
'''
price = float(input())
tip_pct = float(input())
tip_amount = (price/100)*tip_pct

print('Tip amount:', tip_amount)
print('Total bill', price + tip_amount)
