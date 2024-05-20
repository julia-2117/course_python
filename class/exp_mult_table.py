# Generate and print the multiplication table (up to 10) for a given number
mult = 0
num = int(input('Enter a number: '))

for i in range(1,11):
    mult = num * i
    print(f'{num} x {i} = {mult}')
