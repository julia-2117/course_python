# Make a program that determines if a number (given by the user) is odd or even
# User's name
number=int(input('Enter a number: '))

# Test if the number is odd or even
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')


