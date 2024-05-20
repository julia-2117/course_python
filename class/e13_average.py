"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""

prom = 0
cont = 0
while True:
    num = float(input('Enter a number: '))
    if num == 0 and cont == 0:
        print('Existe un error ya que tu primer numero ha sido cero, ingresa otro numero')
        continue
    if num == 0:
        break
    cont += 1
    prom += num
print(f'Tu promedio es: {prom/cont}')

# Otra forma

# prom = 0
# cont = 0
# while True:
#     num = float(input('Enter a number: '))
#     if num == 0 and cont == 0:
#         print('Existe un error ya que tu primer numero ha sido cero, ingresa otro numero')
#         continue
#     elif num == 0:
#         break
#     else:
#         cont += 1
#         prom += num
# print(f'Tu promedio es: {prom/cont}')
