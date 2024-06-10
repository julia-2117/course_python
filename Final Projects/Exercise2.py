# INTERPOLACION
import numpy as np
from sympy import symbols, sympify
import matplotlib.pyplot as plt


x = symbols('x')
cn = int(input('Ingrese la cantidad de nodos a ocupar: '))
xi = []
for i in range(cn):
    d = int(input('Ingrese nodo: '))
    xi.append(d)

q = input('Ingresara funcion (1) o los datos de fxi (2)? ')
if q == '1':
    f = input(' Ingrese la funcion de primer grado deseada: ')
    f = sympify(f)
    fxi = [f.subs(x, val) for val in xi]
    print(fxi)
elif q == '2':
    fxi = []
    for i in range(cn):
        dato = float(input('Ingrese el dato para fxi: '))
        fxi.append(dato)
    print(fxi)


def interp(xi, fxi):
    n = len(xi)
    x = sympify('x')
    P = 0
    for k in range(n):
        lnk = 1
        for i in range(n):
            if i != k:
                lnk = lnk * ((x-xi[i])/(xi[k]-xi[i]))
        P = P + lnk * fxi[k]
    return P


print(f'\nxi es {xi}')
print(f'\nfxi es: {fxi}')
P = interp(xi, fxi)
print(P)
# Graficando la interpolacion
plt.scatter(xi, fxi, color='red')
x_1 = np.linspace(-10, 10)
y = [P.subs(x, _) for _ in x_1]
plt.plot(x_1, y, color='blue')
plt.show()


