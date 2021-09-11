'''
Write a program that asks the user to enter a
weight in kilograms. The program should convert
it to pounds, printing the answer rounded to
the nearest tenth of a pound.
'''

kilos = float(input('Enter your weight in kilograms '))

print('Your weight in pounds is:', round(kilos/0.4535, 1))
