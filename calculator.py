

def add(x, y):
    return x + y

def Factorial(n):
    s = 1
    for i in range(1, n+1, 1):
        s = s*i
    return s

#k = add(3, 5)
#print(k)
    
j = Factorial(10)
print(j)

from math import factorial
print(factorial(10))