"""
Your job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1
"""
bill = 0

size = input('What is the size ? small (S), medium (M), large (L): ')
pepperoni=bool(int(input('Do you want to add pepperoni? (1) yes, (0) no: ')))
cheese=bool(int(input('Do you want to add cheese? (1) yes, (0) no: ')))
if size == 'S':
    bill = bill+15  # Is equal to bill+=15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if size == 'S' and pepperoni:
    bill += 2
elif pepperoni:  # Se le tiene que poner la condicion para que no haya contradiccion
    bill += 3

if cheese:
    bill += 1
print(bill)
