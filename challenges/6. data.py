"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""

data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]

import statistics as st

media = st.mean(data)
desvest = st.stdev(data)
print(f'La media de data es: {media} y su desviacion standar es: {desvest}')
sum = 0
for i in data:
    sum += i
media1 = sum/len(data)
s = 0
for j in data:
    s = s + (pow((j-media1), 2))
desvest1 = s/(len(data)-1)
print(media1)
print(desvest1)

# my_norm = st.NormalDist()  # Instance of class, ie, the creation of an object
# my_norm2 = st.NormalDist(2, 4)  # Disctint object of my_norm
# print(my_norm.pdf(0.5))
# print(my_norm2.stdev)  # Objeto de tipo NormalDist

# append no se puede usar solito porque es un metodo de un objeto y solo es usado para las listas
