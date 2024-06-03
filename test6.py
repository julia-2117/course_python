#
# a = (1, 2, 3, 4)  # Packing
#
# b, c, d, e = a  # Unpacking
#
# print(e)
# # Se le asigna una letra a cada valor d ela tupla y si pido alguna letra me da el valor en a
#
# # Nos damos cuenta de que es un iterable por
# print(dir(range(7)))  # Dunder_methods

# my_range = range(7)  # Esto es un interable
# print(my_range)
# print(*my_range)  # Funciona para imprimir todos los elementos del rango
#
# print(*[1, 2, 3])  # Accede a los elementos de la lista

# * args
# ** kargs


######################

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  # Packing

# rest, school, free = days  # Error
*rest, school, free = days

print(rest)
print(school)
print(free)


#########################

from random import gauss  # Retorna un numero aleatorio de la normal
my_numbers = []

# LIBRERIAS-----Contiene modulos
# Modulos--- tiene 