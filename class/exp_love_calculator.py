"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
    Take both people's names and check for the number of times the letters in the word TRUE occur.
    Then check for the number of times the letters in the word LOVE occur.
    Then combine these numbers to make a 2 digits number.
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. E.g.:
"Your score is *z*."
"""
name1 = input('What is the name 1?: ').upper()
name2 = input('What is the name 2?: ').upper()  # Para hacerlas todas mayusculas
names = name1+name2
print(names)
# Queremos saber cuantas veces esta la letra del nombre en la palabra TRUE
T = names.count('T')
R = names.count('R')
U = names.count('U')
E = names.count('E')
times_true = T+R+U+E

L = names.count('L')
O = names.count('O')
V = names.count('V')
E = names.count('E')
times_love = L+O+V+E

score = int(str(times_true) + str(times_love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 < score < 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')



#######################################################3333

while TRUE:
    name = input('Enter your name: ')
    if name == 'stop':
        # Si le pongo pass aqui, ignora el if y se sale automaticamente por el brake
        break
    age = input('Enter your age: ')
    print('Hello', name, '=>', int(age)**2')
print('out of while')