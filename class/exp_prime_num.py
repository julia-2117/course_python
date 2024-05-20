# Write a program to find and print all prime numbers between 1 and 100
for i in range(1, 101):
    div = 0
    for _ in range(1,101):
        if i % _ == 0:
            div += 1
    if div <= 2:
        print(i, end=' ')
 # else:
 #     continue

