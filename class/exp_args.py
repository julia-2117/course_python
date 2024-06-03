"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""


def sum_args(*numbers):  # Te genera una tupla
    return sum(numbers)  # Suma cada elemento de la tupla generada


print(sum_args(1, 2, 3))


"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""

def concat_strings(*words):
    print()

# Cuando pones doble asterisco es como un diccionario

"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""


def calculate_expenses(name, montly_income, *expenses, **fixed_expenses):
    print(montly_income - sum(expenses) - sum(fixed_expenses.values()))  # Una forma
    # Otra forma con 2 for

    #print(f'{name}, tu saldo despues de gastos es: {saldo}')


calculate_expenses('Julia',
                   10000,
                   45, 100, 1500, 45,
                   internet=500, food=1000, coffee=2000)
