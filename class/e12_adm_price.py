"""
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00.
Admission for all other guests is $23.00. Create a program that begins by reading the ages of all the guests in a
group from the user,with one age entered on each line.
The user will enter a blank line to indicate that there are no more guests in the group.
Then your program should display the admission cost for the group with an appropriate message.
"""

# num_inv = int(input('Enter number of members: '))
edad = 0
cont = 0
# for i in range(1, num_inv+1):
while True:
    edad = input('Enter the age: ')
    if edad == '':
        print('Los invitados han acabado')
        break
    edad = int(edad)
    if edad <= 2 and edad > 0:
        print('The person enters for free')
    elif edad >= 3 and edad < 12:
        cont += 14
    elif edad >= 65:
        cont += 18
    else:
        cont += 23

print(f'The total to pay is: {cont}')
