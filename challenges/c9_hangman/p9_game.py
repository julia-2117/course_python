from random import choice
from hangman_art import logo
from hangman_words import words
print(logo)
print('Welcome to the hangman game actuarial science version')

word = choice(words)
word = list(word)
print(word)
p = []
for _ in word:
    if _ != ' ':
        print('_', end='')
        p.append('_')
    else:
        print(' ', end='')
        p.append(' ')
print('\n\n',p)
g = input('\nEnter a guess: ')
for i in word:
    if g == i:



