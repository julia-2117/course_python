
word = input('Enter a word: ')
espal = True
long = len(word)

for i in range(long):
    if word[i] != word[-i-1]:
        espal = False
        break

if espal:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')


# Si la funcion no tiene un return entonces da un None y no se puede poner con el print
# Si tiene un raturn si podemos dejar el print porque es lo que se va a imprimir

# reverse----retorna una lista y se aplica a listas directamente
# reversed----retorna un iterator y necesariamente se usa un for para acceder

# return word == word[::-1] ----retorna un valor booleano
