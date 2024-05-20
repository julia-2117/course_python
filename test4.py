# Paradigms
# PROCEDURAL APPROACH
import random

#generating faces of a die
# faces = []
# for f in range(1,7):
#     faces.append(f)
#
# print(faces)
#
# """
# TE LOGIC:
# 1. WE NEED A DICE
# 2. WE ROLL THAT DICE A NUMBER OF TIMES AND RECORD THE FACE OF INTEREST
# 3.
# """
# # Vamos a repetir el dado un determinado numero de veces
#
# n = 100000
# face_selected = 5
# occurrence = 0  # Cuantas veces sale el 5 en las 100 tiradas
# for _ in range(n):
#     random_face = random.choice(faces)  # Va a escoger de la lista una cara aleatoria(del 1 al 6)
#     if face_selected == random_face:
#         occurrence += 1

# print the ratio of occurence(frequency)
#print(f'The frequency of face number {face_selected} in {n} trials is {occurrence/n}')

# Functional approach
faces = [f for f in range(1, 7)]  # Forma mas pythonic de crear una lista

# def roll_dice():
#     return random.choice(faces)  # Retorna un objeto
# Entonces puedo guardar lo que retorna en una variable
# my_random = roll_dice()
# print(my_random)
#print(roll_dice())

def rolling(r, face):
    times = 0
    for _ in range(r):
        if roll_dice() == face:
            times += 1
    return times

#print(rolling(r:5, face:1))

def frequency(r, face):
    print(f'The frequency is: {rolling(r, face) / r}')

n = int(input('How many trials do you want?: '))
user_face = int(input('What face?: '))

frequency(n, user_face)
