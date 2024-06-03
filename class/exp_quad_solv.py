"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""

x = lambda a, b, c: ((-b+pow(pow(b, 2) - 4*a*c, 0.5)) / (2*a), (-b-pow(pow(b, 2)-4*a*c, 0.5)) / (2*a))
print(x(2, 2, 0))

# Otra forma es
print((lambda a, b, c: ((-b+pow(pow(b, 2) - 4*a*c, 0.5)) / (2*a), (-b-pow(pow(b, 2)-4*a*c, 0.5)) / (2*a)))(2,2,0))



