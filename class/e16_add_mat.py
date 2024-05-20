"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).
"""
matrix_1 = []
matrix_2 = []
cantidad = int(input('Ingresa la cantidad de listas que estaran en tu listas principales: '))
tam = int(input('De que tamaño seran tus listas de las listas?: '))
print('Valores para la matriz 1')
for k in range(cantidad):
    submatrix = []
    for i in range(tam):
        valor = int(input('Ingrese valor: '))
        submatrix.append(valor)
    matrix_1.append(submatrix)
print('Valores para la matriz 2')
for k in range(cantidad):
    submatrix2 = []
    for i in range(tam):
        valor2 = int(input('Ingrese valor: '))
        submatrix2.append(valor2)
    matrix_2.append(submatrix2)


# Function
def sum_of_lists(matrix1, matrix2):
    matrix_suma = []
    for j in range(len(matrix1)):
        ren_suma = []
        for n in range(len(matrix1[0])):
            suma = matrix1[j][n] + matrix2[j][n]
            ren_suma.append(suma)
        matrix_suma.append(ren_suma)
    print(f'La suma de tus listas es: {matrix_suma}')


print(f'Tu primera matriz es {matrix_1}')
print(f'Tu segunda matriz es {matrix_2}')
sum_of_lists(matrix_1, matrix_2)

# OTRA FORMA

# Con zip
# Zip ---- Hace que las listas se junten en tuplas





