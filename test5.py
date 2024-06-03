
# x = 0
# def increment_by_n(n):
#     global x
#     x += n  # Here i am defining a new local variable x, is not the outer x
#     return x
#
# print(x, increment_by_n(5))
# print(x)
# No se pueden modificar valores de afuera

x = 0
def increment_by_n(n): return 2*n

x += increment_by_n(5)

print(x)

# Argumentos es cuando estoy usando la funcion (We use arguments when we are CALLING a function
# We use parameters when we are making a function
# CALLING is when we call to the function

# Los parametros definen que tipo de argumentos puede aceptar la funcion

# Builting function------COMPLEX

complex(4, 4)  # Tambien puede ser complex(real = 4, imag = 4)


# matplotlib, Manym (animacion en matematicas),  es libreria
# programa 3blue1brown
# numpy---paqueteria
# Tensor Flow es para inteligencia artificial ----libraria

# Modulos----funciones, clases y variables
# Libreria ---- Conjunto de modulos Is a set of modules
# Paqueteria ---- Archivo _init_.py--forma de organizar modulos relacionados
# Corre sus propios objetos o puede tener mas modulos dentro, y correr lo que le indiquemos


#### Cuando tengo *integers es que puedo meter todos los enteros que quiero
#### cuando tengo (a,b,*,rel_tol=0.3)
# quiere decir que todo despues del * debe ir tal cual


