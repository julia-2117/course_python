from random import choice
from hangman_art import logo, stages
from hangman_words import words
print(logo)
print('Welcome to the hangman game actuarial science version')
word = choice(words)
word = list(word)
# print(word)
p = []
for _ in word:
    if _ != ' ':
        print('_', end='')
        p.append('_')
    else:
        print(' ', end='')
        p.append(' ')
#print('\n\n', p)


def sust(list, g, s):
    indice = len(s) - 1
    for i in range(len(list)):
        if list[i] == g:
            p[i] = g
        # elif list[i] != g:
        #     print(s[indice])
        #     indice -= 1
    return p


while '_' in p:
    g = input('\nEnter a guess: ')
    print(g)
    s = stages
    print(sust(word, g, s))





