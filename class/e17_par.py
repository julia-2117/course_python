ra = range(1, 10, 2)  # Using positional-only---solo es un vector posicional porque no se le pone start = 1
# Range --- builting function

# Defininf a function with positional-only

def func1(value1, value2, value3, /):  # Si no le pongo la / entonces tengo que usarlos como keyword-arguments
    # Todos keyword o todos posicionales
    print(value1/value3+value2)

func1(1, 2, 3)

# Positional-or-keyword with a built-in

com = complex(imag=5, real=1)
com2 = complex(real=1, imag=5)
com2 = complex(5, 4)
com4 = complex(10)  # Se le asigna automaticamente al valor real
print(com4)

# Definir a function with positional-or-keyword


def func2(r, i=0):
    print(f'{r}+{i}j')


func2(i=4, r=8)  # O tambien func2(4)


# keyword-only

def func3(pos1, *, live, student = ' '):
    print(live + student + str(pos1))


func3(5, live='true', student='jake')


def some(obs, k_or_guess, iter = '20', /, thresh='1e-05', check_finite='True', *, seed='None'):
    print(obs + k_or_guess+thresh+check_finite+seed)


some('hola', 'adios', seed='example')




def f(*var, v1, v2):
    print(var, v1, v2)


f(1,2,3,4, v1=2,v2=3)





