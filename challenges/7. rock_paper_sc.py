from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

my_choice = input(' Make a choice: r(rock), p(paper), s(scissors): ')
if my_choice == 'r':
    print(f'You choice was {rock}')
elif my_choice == 'p':
    print(f'You choice was {paper}')
else:
    print(f'You choice was {scissors}')

v = ['r', 'p', 's']
you_choice = choice(v)
if you_choice == 'r':
    print(f"The computer's choice was {rock}")
elif you_choice == 'p':
    print(f"The computer's choice was {paper}")
elif you_choice == 's':
    print(f"The computer's choice was {scissors}")

if my_choice == you_choice:
    print('It is draw')
elif my_choice == 'r' and you_choice == 'p':
    print('You lose')
elif my_choice == 'r' and you_choice == 's':
    print('You win')
elif my_choice == 'p' and you_choice == 'r':
    print('You win')
elif my_choice == 'p' and you_choice == 's':
    print('You lose')
elif my_choice == 's' and you_choice == 'r':
    print('You lose')
elif my_choice == 's' and you_choice == 'p':
    print('You win')

################ Con funciones

