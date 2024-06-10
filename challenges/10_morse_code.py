from playsound3 import playsound
from time import sleep
import winsound
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
"""
Diccionario es una coleccion de k values--pares de valores que contiene el diccionario
my_dict = {'country': 'mexico'}
Para acceder a ello se colocan los corchetes
print(my_dict['country']) -----para acceder
my_dict['age'] = 21 ----para editar el diccionario
"""
word = input('Enter a word: ')
word = word.upper()
for _ in word:
    if _ == ' ':
        print(' ', end=' ')
    for i in MORSE_CODE_DICT:
        if _ == i:
            word1 = MORSE_CODE_DICT[i]
            sleep(0.5)
            for j in word1:
                if j == '-':
                    print(j, end='')
                    playsound('long.wav')
                else:
                    print(j, end='')
                    playsound('short.wav')
