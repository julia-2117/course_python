"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""

num = int(input('Enter a number: '))  # Typecasting

cont = 0
while True:
    if num == 1:
       break
    if num % 2 == 0:
        num = num / 2  # Shared references
        cont += 1
        print(num)
    else:
        num = 3 * num + 1
        cont += 1
        print(num)
print(f'Los pasos que diste son: {cont}')