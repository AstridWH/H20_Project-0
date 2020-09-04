from calculator import add, Factorial
import math as math

def test_add(a=1, b=2):
    n = add(a, b)
    m = a + b
    return n == m 
    
def test_add_float(a=0.1, b=0.2):
    #print(add(a,b))
    #print(a+b)
    return abs((add(a,b)) - (a+b)) < 1e-13

def test_add_string(a = 'Hello', b = 'World'):
    n = add(a, b)
    m = a + b
    return n == m 

def test_factorial(n = 10):
    n = Factorial(n)
    m = math.factorial(n)
    return abs(n-m) < 1e13





print('1')    
print(test_add())
print('2')
print(test_add(0.1, 0.2))   #Samme resultat som add_float
print(test_add_float())
print('3')
print(test_add_string())
print(test_add('Hello', 'World'))
print('4')
print(test_factorial())