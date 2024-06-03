from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

le = int(input('How many letters would you like in your password?: '))
n = int(input('How many numbers would you like in your password?: '))
s = int(input('How many symbols would you like in your password?: '))
list = []
for i in range(le):
    list.append(choice(letters))
for j in range(n):
    list.append(choice(numbers))
for k in range(s):
    list.append(choice(symbols))
shuffle(list)

list1 = ''
for _ in list:
    list1 += _
print(f'You password is {list1}')


