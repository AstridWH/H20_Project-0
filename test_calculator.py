from calculator import add, Factorial, Sin, divide, Cos, Tan
import math as math
import pytest

tol = 1e-13

def test_add(a=1, b=2):
    n = add(a, b)
    m = a + b
    return n == m 

def add_number_and_string(a=1, b= 'hello'):
    with pytest.raises(TypeError):
        add(a,b)
    
def test_add_float(a=0.1, b=0.2):
    #print(add(a,b))
    #print(a+b)
    return abs((add(a,b)) - (a+b)) < tol

def test_add_string(a = 'Hello', b = 'World'):
    n = add(a, b)
    m = a + b
    return n == m 

@pytest.mark.parametrize("a, b", [((1.0,2.0),3.0), ((3.0,4),7), ((10,7),17), ("Hello", "World"), "Hello World"])
def test_add_para_int_float_str(a,b):
    s = add(a[0], a[1])
    assert s == b

def test_factorial(k = 10):
    n = Factorial(k)
    m = math.factorial(k)
    return abs(n-m) < tol

@pytest.mark.parametrize("a, b", [(2,2), (3, 6), (10, 3628800)])
def test_factorial_para(a, b):
    assert Factorial(a) == b

def test_sin(x=math.pi/2, N=85):
    u = math.sin(x)
    v = Sin(x, N)
    return abs(u-v) < tol

@pytest.mark.parametrize("a, b", [((0, 85), 0), ((math.pi/6, 85), 1/2), ((math.pi/2, 85), 1), ((3*math.pi/2, 85), -1)])
def test_sin_para(a, b):
    u = Sin(a[0], a[1])
    assert abs(u-b) < tol
    
def test_divide(x=34926, y=5821):
    u = x/y
    v = divide(x, y)
    return u == v

def test_divide_by_zero(x = 1, y = 0):
    with pytest.raises(ZeroDivisionError):
        divide(x,y)

@pytest.mark.parametrize("a,b", [((4, 2), 2), ((14, 7), 2), ((81, 3), 27)])
def test_divide_para(a, b):
    u = divide(a[0], a[1])
    assert u == b

def test_cos(x=math.pi/4, N=85):
    u = math.cos(x)
    v = Cos(x, N)
    return abs(u - v) < tol

@pytest.mark.parametrize("a, b", [((0, 85), 1), ((math.pi/3, 85), 1/2), ((math.pi/2, 85), 0), ((math.pi, 85), -1)])
def test_cos_para(a,b):
    u = Cos(a[0], a[1])
    assert abs(u-b) < tol


def test_tan(x=math.pi/4, N=85):
    u = math.tan(x)
    v = Tan(x, N)
    return abs(v - u) < tol

@pytest.mark.paramertize("a,b", [((0, 85), 0), ((math.pi/4, 85), 1), ((math.pi, 85), 0)])
def test_tan_para(a,b):
    u = Tan(a[0], a[1])
    assert abs(u-b) < tol 
    

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
print(test_sin())
print(test_divide())
print(test_cos())
print(test_tan())
print('5')
print(add_number_and_string())

print('6')
print(test_add_para())
