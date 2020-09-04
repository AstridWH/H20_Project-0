

def add(x, y):
    return x + y

def Factorial(n):
    s = 1
    for i in range(1, n+1, 1):
        s = s*i
    return s

def Sin(x, N):
    s = 0
    for n in range(0, N):
        s += (((-1)**n)*(x**(2*n + 1)))/(Factorial(2*n+1))
    return s

def divide(x, y):
    return x/y

def Cos(x, N):
    s = 0
    for n in range(0, N):
        s += (((-1)**n)*(x**(2*n)))/(Factorial(2*n))
    return s
    

k = add(3, 5)
print(k)
    
j = Factorial(10)
print(j)

from math import factorial
print(factorial(10))

from math import pi
print(Sin(pi/2, 85))

from math import sin 
print(sin(pi/2))

print(divide(20, 5))

print(Cos(pi/4, 85))
from math import cos
print(cos(pi/4))