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
    
def Tan(x, N):
    return (Sin(x, N)/Cos(x, N))