



# Como idetnificar un iterable----Podemos extraer un elemento de ahi
# iterable[i]
#  We can get item by item

# Sintaxis para extraer cada elemento del iterable [1,2,3,4]
# for numer in [1,2,3,4] forzosamente debe haber un iterable o un iterator

# words=['despair','phone', 'computer', 'english', 'science']  # Lista es un objeto, entonces tiene metodos y atributos
# #print(dir(words))  # Devuelve una lista que devuelve los metodos que tiene la lista
#
# # Un iterable tiene esos 2 metodos: iter y getitem
# # So, words is an iterable
# # __getitem__ es solo para la ejecucion de python
#
#
# print(words.__getitem__(0))
# print(words[0])
# print('---------------------------------')
# # Aqui el for accede a los elementos de una lista....Es diferente a los otros for de otros programas
#
# for index in range(0, len(words)):
#     # El range produce numeros enteros desde 0 hasta la longitud de la lista
#     print(words[index])
# print('---------------------------------')
# # De forma pythonic
# for letter in words:
#     print(letter)
#
# # El for convierte a un iterable en un iterator
#
# for k in range(5):
#     print(k)

# EJERCICIO 1
# i = 0
# while True:
#     num = int(input('Enter a number: '))
#     if num < 0:
#         print(i)
#         break
#     i += num

# EJERCICIO 15/04/2024
# lista = []
# while True:
#     cont = bool(int(input('Do you want to continue?: 1 yes, 0 no')))
#     if not cont:
#         break
#     num = int(input('Ingresa un numero'))
#     if num%2 == 0:
#         lista.append(num)
# print(lista)

###################################################
# while True:
#     cont = bool(int(input('Enter a password: ')))


################################################

n = int(input('Enter a number: '))
fact = 1
if n > 0:
    for x in range(1, n+1):
        fact *= x
    print(fact)
else:
    print('The number is negative, enter a positive number')


