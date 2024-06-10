# METODO DE MULLER
import numpy as np
from sympy import symbols, sympify

x = symbols('x')
f = input('Ingrese una funcion: ')
f = sympify(f)
print('Las aproximaciones a continuacion deben ser de forma ascendente')
p0 = float(input('Ingrese la primer aproximacion: '))
p1 = float(input('Ingrese la segunda aproximacion: '))
p2 = float(input('Ingrese la tercera aproximacion: '))
if p0 < p1 < p2:
    y0 = f.subs(x, p0)
    y1 = f.subs(x, p1)
    y2 = f.subs(x, p2)
    print(y0, y1, y2)
    for i in range(1, 5):
        print('\nEvaluando los puntos en la funcion')
        a, b, c = symbols('a b c')
        f1 = a * pow((p0-p2), 2) + b * (p0-p2) + c
        f2 = a * pow((p1-p2), 2) + b * (p1-p2) + c
        print('Tus ecuaciones son: ')
        print(f1)
        print(f2)
        # Resolviendo el sistema de ecuaciones
        m1 = np.array([[pow((p0-p2), 2), (p0-p2)], [pow((p1-p2), 2), (p1-p2)]])
        m2 = np.array([[(y0-y2), (p0-p2)], [(y1-y2), (p1-p2)]])
        m3 = np.array([[pow((p0-p2), 2), (y0-y2)], [pow((p1-p2), 2), (y1-y2)]])
        print('\nTus matrices son: ')
        print(m1)
        print(m2)
        print(m3)
        d1 = m1[0][0]*m1[1][1] - m1[0][1]*m1[1][0]
        d2 = m2[0][0]*m2[1][1] - m2[0][1]*m2[1][0]
        d3 = m3[0][0]*m3[1][1] - m3[0][1]*m3[1][0]
        P = a * pow((x-p2), 2) + b * (x-p2) + c
        print(f'\nLa ecuacion es: {P}')
        a = a.subs(a, (d2/d1))
        b = b.subs(b, (d3/d1))
        c = c.subs(c, y2)
        print(f'\nLos valores de las variables son: a={a}, b={b}, c={c}')
        # Calcular el discriminante
        D = pow(b, 2) - 4*a*c
        if D > 0:
            x1 = (-b + pow(D, 1/2)) / (2 * a)
            x2 = (-b - pow(D, 1/2)) / (2 * a)
            print(f'\nLas soluciones son {x1}, {x2}')
            # Calcular el error para tomar el menor y definir el punto nuevo
            error1 = abs(x1 - p2)
            error2 = abs(x2 - p2)
            if error1 < error2:
                if x1 > p2:
                    p0 = p1
                    p1 = p2
                    p2 = x1
                elif p0 < x1 < p2:
                    p0 = p1
                    p1 = x1
                    p2 = p2
                elif x1 < p2 and x1 < p1:
                    p0 = x1
                    p1 = p1
                    p2 = p2
                print(f'\nTus nuevos puntos son: {p0}, {p1}, {p2}')
            elif error2 < error1:
                if x2 > p2:
                    p0 = p1
                    p1 = p2
                    p2 = x2
                elif p0 < x2 < p2:
                    p0 = p1
                    p1 = x2
                    p2 = p2
                elif x1 < p2 and x1 < p1:
                    p0 = x2
                    p1 = p1
                    p2 = p2
                print(f'\nTus nuevos puntos son: {p0}, {p1}, {p2}')
        elif D == 0:
            x = -b/(2*a)
            print(f'\nLa solucion es {x}')
        else:
            realpart = -b/(2*a)
            imagpart = pow(-D, 1/2)/(2*a)
            print(f'\nLas soluciones son {imagpart} + {realpart}, {imagpart} - {realpart}')
else:
    print('Las aproximaciones no estan escritas de forma ascendente')
