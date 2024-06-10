# METODO DE NEWTON
import numpy as np
from sympy import symbols, solve, diff, sympify
import pandas as pd
import matplotlib.pyplot as plt
# Funcion
x = symbols('x')
f = input('Ingrese una funcion: ')
raices = solve(f, x)
print(raices)
r = int(input('Elija una raiz: '))
print(f'La raiz elegida es {raices[r-1]}')

# Aproximacion inicial y derivada de la funcion
p0 = float(input('Escriba una aproximacion inicial de acuerdo a la raiz elegida: '))
df = diff(f, x)
df = sympify(df)
dif = 1
i = 1
f = sympify(f)
aprox = []
vi = []
vx = []
ve = []

# Newton
while dif != 0:
    p_0 = p0
    p0 = p0-float(f.subs(x, p0))/float(df.subs(x, p0))
    dif = p0-p_0
    i += 1
    vi.append(i)
    vx.append(p0)
    ve.append(abs(p0))

# Tabulacion
T = pd.DataFrame({'Iteracion': vi, 'Aproximacion': vx, 'Error': ve})
print(T)

# Graficar la funcion, las raices y aproximaciones
x_1 = np.linspace(-10, 10, 1000)
y = [f.subs(x, _) for _ in x_1]
plt.plot(x_1, y, color='blue')
plt.scatter(raices, [0]*len(raices), color='red')
plt.scatter(vx, [0]*len(vx), color='black')
plt.grid(True)
plt.title('Grafica de aproximaciones por el metodo Newton')
plt.show()
