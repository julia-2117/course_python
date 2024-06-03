import statistics as st, random, math, numpy as np
ds = np.sqrt(5)
r = int(input('Cuantos numeros aleatorios quieres?: '))
for i in range(r):
    n = random.gauss(2, 2.236067977)
if n >= 0:
    f = n/3
else:
    f = -(n+5)/6

x = random.gauss(2, 2.236067977)
print(n)
if x < 0:
    g = np.sqrt(x)
elif 0 >= x < 1:
    g = 4*math.cos(2*math.pi*x)
else:
    g = x*math.log(x*pow(math.e, x)*math.tanh(x), 2)
# map



